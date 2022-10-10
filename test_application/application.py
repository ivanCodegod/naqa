import time
import logging

from request_formation import \
    collect_accreditation_id, \
    parse_all_accreditation_by_area, \
    get_accreditation_response_list, \
    get_response_json
from manipulate_csv import \
    delete_old_csv, \
    build_csv, \
    CSV_FILE_NAME
from prepare_filter_criteria import \
    prepare_filter_criteria, \
    get_input_criteria
from interface import user_interface

# Set logging level
# TODO: Configure this information with help of Poetry(in .toml file)
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


def filter_accreditation(filtration_criteria_list):
    """Filter accreditation cases by criteria list."""
    all_accreditation = parse_all_accreditation_by_area()
    accreditation_ids_list = collect_accreditation_id(all_accreditation)
    accreditation_response_list = get_accreditation_response_list(accreditation_ids_list)

    matched_accreditation_count = 0
    for accr_index, accreditation in enumerate(accreditation_response_list):
        logging.debug("Current accreditation id: %s", accreditation_ids_list[accr_index])
        matched = False

        row_in_csv = []
        for i in filtration_criteria_list:
            filter_criteria, current_filter_value = i[0], i[1]

            # if filtration parameter could be parsed only from all accreditation request
            if "from_all" in str(filter_criteria).split()[1]:
                logging.debug("'From all' option. id=%s", accreditation_ids_list[accr_index])
                logging.debug("function name=%s", str(filter_criteria).split()[1])
                try:
                    current_filter_criteria = str(filter_criteria(all_accreditation, accr_index))
                except (TypeError, AttributeError, IndexError):
                    matched = False
                    logging.debug("There no such info/path in json body.")
                    break
            else:
                logging.debug("'NOT from all' option. id=%s", accreditation_ids_list[accr_index])
                logging.debug("function name=%s", str(filter_criteria).split()[1])
                try:
                    current_filter_criteria = str(filter_criteria(get_response_json(accreditation)))
                except (TypeError, AttributeError, IndexError):
                    logging.debug("There no such info/path in json body.")
                    matched = False
                    break
            if current_filter_value == 'default_criteria':
                matched = True
                row_in_csv.append(current_filter_criteria)
            elif current_filter_criteria == current_filter_value:
                matched = True
                row_in_csv.append(current_filter_value)
            elif "get_last_name_of_expert" in str(filter_criteria):
                # not standard filtration. Need to filtrate specifically for last name of expert.
                if current_filter_value in current_filter_criteria:
                    matched = True
                    row_in_csv.append(current_filter_value)
                else:
                    matched = False
                    break
            elif "get_time_na_meeting" in str(filter_criteria):
                # not standard filtration. Need to filtrate specifically for time NA meeting.
                current_acrr_datetime = current_filter_criteria
                start_datetime = current_filter_value[0]
                end_datetime = current_filter_value[1]

                if start_datetime <= current_acrr_datetime <= end_datetime:
                    matched = True
                    row_in_csv.append(current_filter_criteria)
                else:
                    matched = False
                    break
            else:
                matched = False
                logging.debug(
                    "Filtration was failed for accreditation with id=%s.",
                    accreditation_ids_list[accr_index])
                break
        if matched:
            logging.info(
                "Accreditation with id=%s is fits the filtration!",
                accreditation_ids_list[accr_index])
            matched_accreditation_count += 1

            # Build csv table
            build_csv([row_in_csv])

    return matched_accreditation_count, len(accreditation_ids_list)


def main():
    """Main function with logic of filtration and console interface for user."""
    user_interface("welcome")
    while True:
        user_command = input()

        if user_command in ("filter", "f"):
            user_interface("filter")
            delete_old_csv()

            input_criteria_list = get_input_criteria()
            criteria_list = prepare_filter_criteria(input_criteria_list)

            start = time.time()
            matched_accr_count, all_accr_count = filter_accreditation(criteria_list)

            # Time the current filtration
            end = time.time()
            time_result = end - start
            logging.debug("Filtration time: %.4f", time_result)

            logging.info("Усього акредитаційних справ було знайдено: %s", all_accr_count)
            logging.info("Знайдено акредитаційних справ щодо фільтрації: %s", matched_accr_count)
            logging.info(f"Файл {CSV_FILE_NAME} було сформовано.")

            user_interface("help")
        elif user_command in ("help", "h"):
            user_interface("help")
        elif user_command in ("exit", "e"):
            user_interface("exit")
        else:
            user_interface("no_such_command")


if __name__ == '__main__':
    main()
