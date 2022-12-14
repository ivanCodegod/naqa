import os
import grequests
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

RETRY_COUNT = 5
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
    """Collect accreditation id from all accreditations."""
    return [accreditation["accreditationId"] for accreditation in all_accreditation["items"]]
