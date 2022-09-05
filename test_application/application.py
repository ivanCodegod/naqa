import time
import logging

from request_formation import collect_accreditation_id, get_all_accreditation_by_area, \
    get_accreditation_response_list, get_response_json
from manipulate_csv import delete_old_csv, build_csv
from prepare_filter_criteria import prepare_filter_criteria

# Set logging level
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


def filter_accreditation(filtration_criteria_list):
    """Filter accreditation cases by criteria list."""
    all_accreditation = get_all_accreditation_by_area()
    accreditation_ids_list = collect_accreditation_id(all_accreditation)
    accreditation_response_list = get_accreditation_response_list(accreditation_ids_list)
    logging.debug(f"accreditation response list: {accreditation_response_list}")

    matched_accreditation = []
    for accr_index, accreditation in enumerate(accreditation_response_list):
        logging.debug("Current accreditation id: %s", accreditation_ids_list[accr_index])

        response_body = get_response_json(accreditation)
        logging.debug(f"response_body: {response_body}")
        matched = [False]

        row_in_csv = []
        for i in filtration_criteria_list:
            filter_criteria = i[0]
            current_filter_value = i[1]

            # if filtration parameter could be parsed only from all accreditation request
            if "from_all" in str(filter_criteria).split()[1]:
                logging.debug("all option - id=%s", accreditation_ids_list[accr_index])
                logging.debug("func name-%s", str(filter_criteria).split()[1])
                response_body = all_accreditation
                try:
                    current_filter_criteria = str(filter_criteria(response_body, accr_index))
                except TypeError:
                    matched[0] = False
                    break
            else:
                logging.debug("NOT all option - id=%s", accreditation_ids_list[accr_index])
                try:
                    current_filter_criteria = str(filter_criteria(get_response_json(accreditation)))
                except TypeError:
                    matched[0] = False
                    break

            if current_filter_value == 'default_criteria':
                matched[0] = True
                row_in_csv.append(current_filter_criteria)
            elif current_filter_criteria == i[1]:
                matched[0] = True
                row_in_csv.append(i[1])
            else:
                matched[0] = False
                logging.debug("Filtration was failed for accreditation with id=%s.", accreditation_ids_list[accr_index])
                break

        if matched[0]:
            logging.info("Accreditation with id=%s is fits the filtration!", accreditation_ids_list[accr_index])
            matched_accreditation.append(accreditation_ids_list[accr_index])

            # Build csv table
            build_csv([row_in_csv])

    logging.debug("Matched accreditation list: %s", matched_accreditation)
    logging.debug("Full accreditation list: %s", accreditation_ids_list)


if __name__ == '__main__':
    delete_old_csv()
    criteria_list = prepare_filter_criteria()

    start = time.time()
    filter_accreditation(criteria_list)
    end = time.time()
    time_result = end - start
    logging.debug("Program execution time: %.4f", time_result)
