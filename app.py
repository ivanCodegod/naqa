import time
import logging
from requests import Response
from typing import Callable

from logging_config import LoggingConfigurator
from project_settings import ProjectSettingsManager

from request_formation import AccreditationAPIClient
from manipulate_csv import \
    delete_old_csv, \
    build_csv
from prepare_filter_criteria import \
    map_filter_criteria, \
    get_input_values_for_filtration, prepare_csv_table

from interface import AppInterface, AppInterfaceConstants


def apply_filter_criteria(filter_criteria: Callable, accreditation: Response, api_client: AccreditationAPIClient,
                          all_accreditation: dict, accr_index: int):
    """
    Apply the specified filter criteria to the given accreditation.

    Args:
        filter_criteria (function): The filter criteria function to apply.
        accreditation (Response): The accreditation information.
        api_client (AccreditationAPIClient): The API client instance.
        all_accreditation (dict): All accreditation data.
        accr_index (int): The index of the current accreditation.

    Returns:
        str: The result of applying the filter criteria.
    """
    try:
        if "from_all" in str(filter_criteria).split()[1]:
            return str(filter_criteria(all_accreditation, accr_index))
        else:
            return str(filter_criteria(api_client.get_response_json(accreditation)))
    except (KeyError, TypeError, AttributeError, IndexError):
        return None


def filter_accreditation(filtration_criteria_list: list):
    """Filter accreditation cases by criteria list."""
    api_client = AccreditationAPIClient()
    all_accreditation = api_client.parse_all_accreditation_by_area()
    accreditation_ids_list = api_client.collect_accreditation_id(all_accreditation)
    accreditation_response_list = api_client.get_accreditation_response_list(accreditation_ids_list)

    matched_accreditation_count = 0
    for accr_index, accreditation in enumerate(accreditation_response_list):
        logging.debug("Current accreditation id: %s", accreditation_ids_list[accr_index])
        matched = True
        row_in_csv = []

        for filter_criteria, current_filter_value in filtration_criteria_list:
            logging.debug("Filter criteria: %s", filter_criteria)
            current_filter_criteria = apply_filter_criteria(
                filter_criteria, accreditation, api_client, all_accreditation, accr_index
            )

            if current_filter_criteria is None:
                matched = False
                logging.debug("There is no such info/path in the JSON body.")
                break

            if current_filter_value == 'default_criteria' or current_filter_criteria == current_filter_value:
                row_in_csv.append(current_filter_criteria)
            elif "get_last_name_of_expert" in str(filter_criteria):
                # not standard filtration, specifically for the last name of an expert.
                if current_filter_value in current_filter_criteria:
                    row_in_csv.append(current_filter_value)
                else:
                    matched = False
                    break
            elif "get_time_na_meeting" in str(filter_criteria):
                # not standard filtration, specifically for the time of NA meeting.
                start_datetime = current_filter_value[0]
                end_datetime = current_filter_value[1]
                current_acrr_datetime = current_filter_criteria

                if start_datetime <= current_acrr_datetime <= end_datetime:
                    row_in_csv.append(current_filter_criteria)
                else:
                    matched = False
                    break
            else:
                matched = False
                logging.debug(
                    "Filtration failed for accreditation with id=%s.",
                    accreditation_ids_list[accr_index])
                break

        if matched:
            logging.debug(
                "Accreditation with id=%s fits the filtration!",
                accreditation_ids_list[accr_index])
            matched_accreditation_count += 1
            build_csv([row_in_csv])

    return matched_accreditation_count, len(accreditation_ids_list)


command_descriptions = AppInterfaceConstants.COMMAND_DESCRIPTIONS
app_interface = AppInterface()


def main():
    """Main function with logic of filtration and console interface for user."""
    LoggingConfigurator()

    logging.info(command_descriptions[AppInterfaceConstants.WELCOME_COMMANDS])
    logging.info(command_descriptions[AppInterfaceConstants.HELP_COMMANDS])

    while True:
        user_command = input()

        if user_command in AppInterfaceConstants.FILTER_COMMANDS:
            app_interface.handle_command(user_command)
            delete_old_csv()

            input_criteria_list = get_input_values_for_filtration()
            prepare_csv_table(input_criteria_list)
            criteria_list = map_filter_criteria(input_criteria_list)

            start = time.time()
            matched_accr_count, all_accr_count = filter_accreditation(criteria_list)

            # Time the current filtration
            end = time.time()
            time_result = end - start
            logging.debug("Filtration time: %.4f", time_result)

            logging.info("Усього акредитаційних справ було знайдено: %s", all_accr_count)
            logging.info("Знайдено акредитаційних справ щодо фільтрації: %s", matched_accr_count)
            logging.info("Файл %s було сформовано.", ProjectSettingsManager.CSV_FILE_NAME)

            logging.info(command_descriptions[AppInterfaceConstants.HELP_COMMANDS])
        elif user_command in AppInterfaceConstants.HELP_COMMANDS:
            app_interface.handle_command(user_command)
        elif user_command in AppInterfaceConstants.EXIT_COMMANDS:
            app_interface.handle_command(user_command)
        else:
            app_interface.handle_command("no_such_command")


if __name__ == '__main__':
    main()
