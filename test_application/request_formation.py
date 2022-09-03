import requests


#  Get Accreditation list(all available)
#  https://public.naqa.gov.ua/api/v1/Accreditation/Get

#  Get Concrete Accreditation
#  https://public.naqa.gov.ua/api/v1/Accreditation/{id}/Get

def get_all_accreditation_by_area(area="04"):
    # "accreditationId": xxxx - is actual id could be found
    #req = requests.get("https://public.naqa.gov.ua/api/v1/Accreditation/Get", verify=False)
    req = requests.get(f"https://public.naqa.gov.ua/api/Accreditation/Get?$count=true&$skip=0&$orderBy=id%20desc&$filter=contains(tolower(area),%20%27{area}%27)", verify=False)
    json_data = req.json()
    return json_data


def get_accreditation_by_id(id):
    req = requests.get(f"https://public.naqa.gov.ua/api/v1/Accreditation/{id}/Get", verify=False)
    json_data = req.json()
    return json_data


def collect_accreditation_id(all_accreditation):
    program_list = []
    for i in all_accreditation["items"]:
        program_list.append(i["accreditationId"])

    return program_list
