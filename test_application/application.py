import time
import os
import csv
import grequests

from filter_params import *
from request_formation import *


def build_csv(row_list):
    with open('naqa_system_test.csv', 'a', encoding="utf8", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
        writer.writerows(row_list)


def filter_accreditation(criteria_list):
    accreditation_list = collect_accreditation_id(get_all_accreditation_by_area())

    accreditation_requests = [f"https://public.naqa.gov.ua/api/v1/Accreditation/{i}/Get" for i in accreditation_list]
    response = (grequests.get(url, verify=False) for url in accreditation_requests)
    accreditation_response_list = grequests.map(response)

    matched_accreditation = []
    for index, accreditation_id in enumerate(accreditation_response_list):
        print(f"Current accreditation id: {accreditation_id}")

        response_body = accreditation_id.json()
        matched = False

        row_in_csv = []
        for i in criteria_list:
            filter_criteria = i[0]

            if str(filter_criteria(response_body)) == i[1]:
                matched = True
                print(f"Matched: {i[1]}")
                row_in_csv.append(i[1])
            else:
                matched = False
                print(f"Filtration was failed.")
                break

        if matched:
            print(f"Accreditation with id={accreditation_list[index]} is fits the filtration!")
            matched_accreditation.append(accreditation_list[index])

            # Build csv table
            build_csv([row_in_csv])

    print(f"matched accreditation: {matched_accreditation}")
    print(f"accreditation list {accreditation_list}")


def prepare_filtration_criteria():
    # all filtration criteria
    print(f"Input for test: 5329 2248/АС-21 50265")
    exp_id_program = input("Enter expected id program: ")
    exp_acccr_number = input("Enter exp accreditation number: ")
    exp_id_edebo = input("Enter exp id EDEBO: ")

    csv_headers = []

    criteria_list = []
    if exp_id_program:
        criteria_list.append([get_id_program, exp_id_program])
        csv_headers.append("ID")
    if exp_acccr_number:
        criteria_list.append([get_request_number, exp_acccr_number])
        csv_headers.append("Номер AC")
    if exp_id_edebo:
        criteria_list.append([get_id_from_edebo, exp_id_edebo])
        csv_headers.append("ID програми в ЄДЕБО")

    print(f"criteria list: {criteria_list}")
    print(f"scv headers: {csv_headers}")
    build_csv([csv_headers])
    return criteria_list


if __name__ == '__main__':
    # need to delete old .csv file
    if 'naqa_system_test.csv' in os.listdir():
        os.remove('naqa_system_test.csv')

    dictionary = prepare_filtration_criteria()

    start = time.time()
    filter_accreditation(dictionary)

    end = time.time()
    print(f"Execution time: {end - start}")
