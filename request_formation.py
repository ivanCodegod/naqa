import os
import logging
import requests

from requests.adapters import HTTPAdapter
from requests import Response
from urllib3.util import Retry
from concurrent.futures import ThreadPoolExecutor, as_completed

from project_settings import ProjectSettingsManager


class CustomRetry(Retry):
    """
    CustomRetry is a subclass of the Retry class from the urllib3 library, providing custom retry behavior
    with enhanced logging for HTTP requests.

    CustomRetry extends the Retry class by adding enhanced logging for request retries based on different scenarios,
    including response status codes and errors encountered during the request.

    Attributes:
        See the parent class Retry for attributes and their descriptions.

    Usage:
    To use the CustomRetry class, create an instance of CustomRetry with the desired retry configuration,
    and use it as the retry parameter when creating an HTTPAdapter instance for a requests session.
    """

    def increment(self, method=None, url=None, response: Response = None, error=None, _pool=None, _stacktrace=None):
        """
        Increment the retry count and log additional information about the retry attempt.
        Overrides the parent class's increment method to provide custom logging.

        Returns:
            Retry: The updated Retry instance.

        Note:
            The method overrides the parent class's increment method to add logging capabilities for
            different retry scenarios, such as response status codes and request errors.
        """
        if response and response.status_code:
            logging.debug(f"Retrying {response.url} - Response Code: {response.status_code}")
        elif error:
            logging.debug(f"Retrying {url} - Error: {error}")
        return super().increment(
            method=method,
            url=url,
            response=response,
            error=error,
            _pool=_pool,
            _stacktrace=_stacktrace
        )


class AccreditationAPIClient:
    def __init__(self,
                 retry_count: int = ProjectSettingsManager.RETRY_COUNT,
                 pool_max_size: int = ProjectSettingsManager.POOL_MAX_SIZE,
                 timeout_count: int = ProjectSettingsManager.TIMEOUT_COUNT
                 ):
        self.s = requests.Session()
        self.custom_retry = CustomRetry(
            total=retry_count,
            backoff_factor=ProjectSettingsManager.BACKOFF_FACTOR,
            raise_on_redirect=True,
            raise_on_status=True
        )
        self.s.mount('https://', HTTPAdapter(max_retries=self.custom_retry, pool_maxsize=pool_max_size))
        self.timeout_count = timeout_count

    @staticmethod
    def collect_accreditation_id(all_accreditation: dict) -> list:
        """Collect accreditation id from all accreditations."""
        return [accreditation["accreditationId"] for accreditation in all_accreditation["items"]]

    @staticmethod
    def get_response_json(response: Response) -> dict:
        """Return response in json format."""
        return response.json()

    def get_all_accreditation_by_area(self) -> Response:
        """Get all accreditation cases depends on area specified."""
        if os.environ.get("KNOWLEDGE_AREA") is not None:
            area = os.environ.get("KNOWLEDGE_AREA")
        else:
            area = ProjectSettingsManager.DEFAULT_KNOWLEDGE_AREA

        all_accreditation = self.s.get(
            f"https://public.naqa.gov.ua/api/Accreditation/Get?$count=true&$skip=0&$orderBy=id%20desc"
            f"&$filter=contains(tolower(area),%20%27{area}%27)",
            verify=False,
            timeout=ProjectSettingsManager.TIMEOUT_COUNT
        )
        return all_accreditation

    def get_accreditation_response_list(self, accreditation_ids: list[str]) -> list[Response]:
        """
        Retrieves accreditation data concurrently for a list of accreditation IDs by making API requests.

        This function constructs API URLs using the accreditation IDs from the input list and sends concurrent
        HTTP GET requests utilizing ThreadPoolExecutor. It collects the responses in a list in the order they complete.
        When all requests have finished, the function returns the accumulated list of accreditation responses.

        :param accreditation_ids: A list of accreditation IDs for which the accreditation data needs to be retrieved.
        :return: A list of Response objects containing the accreditation data for each accreditation ID.
        """
        # Generate the list of URLs for accreditation requests
        accreditation_requests = [
            f"https://public.naqa.gov.ua/api/v1/Accreditation/{acr_id}/Get" for acr_id in accreditation_ids
        ]

        # Run requests concurrently
        with ThreadPoolExecutor() as executor:
            accreditations_futures = {executor.submit(self.process_accreditation_response, url): url for url in
                                      accreditation_requests}
            accreditation_response_list = []

            for future in as_completed(accreditations_futures):
                result = future.result()
                accreditation_response_list.append(result)

        return accreditation_response_list

    def process_accreditation_response(self, url: str) -> Response | None:
        """
        Sends an HTTP GET request to the specified URL and handles the response.

        This function performs an HTTP GET request to the given 'url'.
        In case of a successful request, it logs the response's status code and content, if the status code is not 200.
        If any exception occurs during the request, it logs the error message and returns None.
        This function is designed to be used within a ThreadPoolExecutor for concurrent requests.

        :param url: The URL to send the HTTP GET request.
        :return: A Response object if the request is successful, otherwise None.
        """
        try:
            response = self.s.get(url, verify=False, timeout=ProjectSettingsManager.TIMEOUT_COUNT)

            logging.debug(f"Response {url} - Status Code: {response.status_code}")
            if response.status_code != 200:
                logging.debug(f"Response Content: {response.content}")

            return response

        except requests.exceptions.RequestException as e:
            logging.error(f"Request {url} failed with exception: {e}")

        return None

    def parse_all_accreditation_by_area(self) -> dict:
        """
        Parse all accreditation cases within the specified knowledge area.

        Returns:
            dict: A dictionary containing the parsed accreditation information.
        """
        all_accreditation_json = self.get_response_json(self.get_all_accreditation_by_area())
        return all_accreditation_json
