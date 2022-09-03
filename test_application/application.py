import time
import logging

from filter_params import *
from request_formation import collect_accreditation_id, get_all_accreditation_by_area, \
    get_accreditation_response_list, get_response_json
from manipulate_csv import delete_old_csv, build_csv

# Set logging level
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


def filter_accreditation(filtration_criteria_list):
    """Filter accreditation cases by criteria list."""
    accreditation_ids_list = collect_accreditation_id(get_all_accreditation_by_area())
    accreditation_response_list = get_accreditation_response_list(accreditation_ids_list)

    matched_accreditation = []
    for accr_index, accreditation in enumerate(accreditation_response_list):
        logging.debug("Current accreditation id: %s", accreditation_ids_list[accr_index])

        response_body = get_response_json(accreditation)
        matched = False

        row_in_csv = []
        for i in filtration_criteria_list:
            filter_criteria = i[0]

            if str(filter_criteria(response_body)) == i[1]:
                matched = True
                row_in_csv.append(i[1])
            else:
                matched = False
                logging.debug("Filtration was failed for accreditation with id=%s.", accreditation_ids_list[accr_index])
                break

        if matched:
            logging.info("Accreditation with id=%s is fits the filtration!", accreditation_ids_list[accr_index])
            matched_accreditation.append(accreditation_ids_list[accr_index])

            # Build csv table
            build_csv([row_in_csv])

    logging.debug("Matched accreditation list: %s", matched_accreditation)
    logging.debug("Full accreditation list: %s", accreditation_ids_list)


def prepare_filtration_criteria():
    """
    Prepare input criteria for filtration of accreditation cases.
    You could specify the value for criteria to be filtered or pass an empty value to skip filtration for current
    criteria

    :return: List of criteria
    """

    # Collect all filtration criteria from user
    logging.info("Input for test: 5329 2248/АС-21 50265")
    exp_id_program = input("Enter expected id program: ")
    exp_acccr_number = input("Enter exp accreditation number: ")
    exp_id_edebo = input("Enter exp id EDEBO: ")
    # TODO: Add remaining filtration criteria

    # Construct table headers for csv file
    csv_table_headers = []
    criteria = []

    # Check if user specified criteria for filtration
    if exp_id_program:
        criteria.append([get_id_program, exp_id_program])
        csv_table_headers.append("ID")
    if exp_acccr_number:
        criteria.append([get_request_number, exp_acccr_number])
        csv_table_headers.append("Номер AC")
    if exp_id_edebo:
        criteria.append([get_id_from_edebo, exp_id_edebo])
        csv_table_headers.append("ID програми в ЄДЕБО")

    logging.info("Criteria list: %s", criteria)
    logging.info("Scv table headers: %s", csv_table_headers)

    # TODO: It maybe a good idea: To add 6 default table headers(ID, Номер AC, ID Програми в ЄДЕБО, Назва університету,
    #  Рівень вищої освіти, Галузь знань)
    build_csv([csv_table_headers])
    return criteria


if __name__ == '__main__':
    delete_old_csv()
    criteria_list = prepare_filtration_criteria()

    start = time.time()
    filter_accreditation(criteria_list)
    end = time.time()
    time_result = end - start
    logging.debug("Program execution time: %.4f", time_result)
