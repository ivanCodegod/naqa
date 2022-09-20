import sys
import time
import logging

from request_formation import collect_accreditation_id, parse_all_accreditation_by_area, \
    get_accreditation_response_list, get_response_json
from manipulate_csv import delete_old_csv, build_csv
from prepare_filter_criteria import prepare_filter_criteria, get_input_criteria

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
                    logging.info("There no such info/path in json body.")
                    break
            else:
                logging.debug("'NOT from all' option. id=%s", accreditation_ids_list[accr_index])
                logging.debug("function name=%s", str(filter_criteria).split()[1])
                try:
                    current_filter_criteria = str(filter_criteria(get_response_json(accreditation)))
                except (TypeError, AttributeError, IndexError):
                    logging.info("There no such info/path in json body.")
                    matched = False
                    break
            if current_filter_value == 'default_criteria':
                matched = True
                row_in_csv.append(current_filter_criteria)
            elif current_filter_criteria == current_filter_value:
                matched = True
                row_in_csv.append(current_filter_value)
            elif "get_last_name_of_expert" in str(filter_criteria):
                # not standard filtration. Need to filtrate specifically.
                if current_filter_value in current_filter_criteria:
                    matched = True
                    row_in_csv.append(current_filter_value)
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


def help_list(command):
    """Function that makes logging depends on user input command."""
    avaliable_commands = \
        'Список доступних команд:\n- "filter" або "f": Почати фільтрацію\n- "help" ' \
        'або "h": Отримати список усіх доступних команд\n- "exit" або "e": Завершити фільтрацію' \
        '\n\nНапишіть команду для виконання. Наприклад "filter"'
    if command in ("welcome", "w"):
        logging.info("Ласкаво просимо до системи фільтрації акредитаційних справ NAQA!")
        logging.info(avaliable_commands)
    elif command in ("filter", "f"):
        logging.info("Початок фільтрації!")
        logging.info(
            'Визначте наступні критерії фільтрації. Щоб пропустити фільтрацію'
            ' за параметром необхідно натиснути кнопку "Enter":')
    elif command in ("help", "h"):
        logging.info(avaliable_commands)
    elif command in ("exit", "e"):
        logging.info("exit")
        sys.exit("Exiting program")
    elif command in ("all_commands",):
        logging.info("\n%s", avaliable_commands)
    elif command in ("no_such_command",):
        logging.info("Такої команди немає")
        logging.info(avaliable_commands)


def main():
    """Main function with logic of filtration and console interface for user."""
    help_list("welcome")
    while True:
        user_command = input()

        if user_command in ("filter", "f"):
            help_list("filter")
            delete_old_csv()

            input_criteria_list = get_input_criteria()
            criteria_list = prepare_filter_criteria(input_criteria_list)

            start = time.time()
            matched_accr_count, all_accr_count = filter_accreditation(criteria_list)

            # TODO: Создать декоратор который будет считать время выполнения фильтрации
            end = time.time()
            time_result = end - start
            logging.debug("Program execution time: %.4f", time_result)

            logging.info("Знайдено акредитаційних справ щодо фільтрації: %s", matched_accr_count)
            logging.info("Усього акредитаційних справ було знайдено: %s", all_accr_count)

            help_list("all_commands")
        elif user_command in ("help", "h"):
            help_list("help")
        elif user_command in ("exit", "e"):
            help_list("exit")
        else:
            help_list("no_such_command")


if __name__ == '__main__':
    main()
