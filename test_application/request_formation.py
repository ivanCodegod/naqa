import os
import grequests
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import logging

from filter_params import get_id_program

RETRY_COUNT = 20
DEFAULT_KNOWLEDGE_AREA = "04"
TIMEOUT_COUNT = 60

s = requests.Session()
retries = Retry(total=RETRY_COUNT, backoff_factor=1, raise_on_redirect=True,
                raise_on_status=True)
s.mount('http://', HTTPAdapter(max_retries=retries, pool_maxsize=2000))
s.mount('https://', HTTPAdapter(max_retries=retries, pool_maxsize=2000))


def get_all_accreditation_by_area():
    """Get all accreditation cases depends on area specified."""
    if os.environ.get("KNOWLEDGE_AREA") is not None:
        area = os.environ.get("KNOWLEDGE_AREA")
    else:
        area = DEFAULT_KNOWLEDGE_AREA

    all_accreditation = requests.get(
        f"https://public.naqa.gov.ua/api/Accreditation/Get?$count=true&$skip=0&$orderBy=id%20desc"
        f"&$filter=contains(tolower(area),%20%27{area}%27)", verify=False)

    return all_accreditation


def get_self_estimation_response_list(accr_response_list, accr_versions):
    self_estim_ids = []
    for accr in accr_response_list:
        self_estim_id = get_id_program(get_response_json(accr))
        self_estim_ids.append(self_estim_id)
        logging.debug(f"self_estim_id: {self_estim_id}")

    self_estimation_requests = [
        f"https://public.naqa.gov.ua/api{version}/SelfEstimation/{id}/Get" for version, id in
        zip(accr_versions, self_estim_ids)
    ]
    self_estimation_response = (grequests.get(url, verify=False, timeout=TIMEOUT_COUNT) for url in
                                self_estimation_requests)
    self_estimation_response_list = grequests.map(self_estimation_response)
    return self_estimation_response_list


def parse_all_accreditation_by_area():
    """Parse all accreditation cases."""
    all_accreditation_json = get_response_json(get_all_accreditation_by_area())
    return all_accreditation_json


def get_accreditation_response_list(accr_ids):
    """Get generated responses of accreditation cases."""
    accreditation_requests = [
        f"https://public.naqa.gov.ua/api/v1/Accreditation/{acr_id}/Get" for acr_id in accr_ids
    ]
    accreditation_response = (grequests.get(url, verify=False, timeout=TIMEOUT_COUNT) for url in accreditation_requests)
    accreditation_response_list = grequests.map(accreditation_response)

    return accreditation_response_list


def get_response_json(response):
    """Return response in json format."""
    return response.json()


def collect_accreditation_id(all_accreditation):
    """
    Collect accreditation id from all accreditations.
    "accreditationId" from json body.
    """
    return [accreditation["accreditationId"] for accreditation in all_accreditation["items"]]


def collect_accreditation_versions(all_accreditation):
    """
    Collect accreditation version from all accreditations.
    "version" from json body.
    """
    acr_versions_list = [accreditation["version"] for accreditation in all_accreditation["items"]]

    for ind, accreditation in enumerate(acr_versions_list):
        if accreditation == "v0":
            acr_versions_list[ind] = ""
        else:
            acr_versions_list[ind] = "/v1"

    return acr_versions_list
