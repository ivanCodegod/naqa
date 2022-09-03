import grequests
import requests


def get_all_accreditation_by_area(area="04"):
    """Get all accreditation cases depends on area specified."""
    # TODO: Add logic with area defining. Not here
    all_accreditation = requests.get(
        f"https://public.naqa.gov.ua/api/Accreditation/Get?$count=true&$skip=0&$orderBy=id%20desc"
        f"&$filter=contains(tolower(area),%20%27{area}%27)", verify=False)

    all_accreditation_json = get_response_json(all_accreditation)
    return all_accreditation_json


def get_accreditation_response_list(accreditation_ids):
    """Get generated responses of accreditation cases."""
    # TODO: Error handling and retry, timeout
    accreditation_requests = [
        f"https://public.naqa.gov.ua/api/v1/Accreditation/{acr_id}/Get" for acr_id in accreditation_ids
    ]
    accreditation_response = (grequests.get(url, verify=False) for url in accreditation_requests)
    accreditation_response_list = grequests.map(accreditation_response)

    return accreditation_response_list


def get_response_json(response):
    """Return response in json format."""
    return response.json()


def collect_accreditation_id(all_accreditation):
    """Collect accreditation id from all accreditations."""
    return [accreditation["accreditationId"] for accreditation in all_accreditation["items"]]
