import logging
from filter_params import *
from manipulate_csv import build_csv

# Set logging level
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


def prepare_filter_criteria():
    """
    Prepare input criteria for filtration of accreditation cases.
    You could specify the value for criteria to be filtered or pass an empty value to skip filtration for current
    criteria

    :return: List of criteria
    """

    # Collect all filtration criteria from user
    logging.info("Input for test: 5329 2248/АС-21 50265 Київська православна богословська академія Доктор філософії\n")
    exp_id_program = input("Enter expected ID освітньої програми: ")
    exp_request_number = input("Enter expected Номер акредитаційної справи: ")
    exp_id_edebo = input("Enter expected ID ОП в ЄДЕБО: ")
    exp_higher_education_name = input("Enter expected Назва закладу вищої освіти: ")
    exp_higher_education_level = input("Enter expected Рівень вищої освіти: ")
    exp_knowledge_area = input("Enter expected Галузь знань: ")
    exp_speciality = input("Enter expected Спеціальність: ")
    exp_op = input("Enter expected Назва ОП: ")

    # в формате год-месяц-день
    exp_date_of_na_order_on_appointment_of_expert_group = input(
        "Enter expected Дата наказу НА про призначення експертної групи: ")

    exp_number_of_na_order_on_appointment_of_expert_group = input(
        "Enter expected Номер наказу НА про призначення експертної групи: ")
    exp_departure_start_date = input("Enter expected Дата початку виїзду: ")
    exp_last_name_of_expert_leader = input("Enter expected Прізвище лідера експертної групи: ")
    # TODO: Add get_last_name_of_expert criteria
    exp_surname_of_ger_speaker = input("Enter expected Прізвище доповідача ГЕР: ")

    #EG
    exp_op_compliance_level_criterion_1_according_to_expert_group = input(
        "Enter expected Рівень відповідності ОП Критерію 1 акредитації, згідно з висновком експертної групи: ")
    exp_op_compliance_level_criterion_2_according_to_expert_group = input(
        "Enter expected Рівень відповідності ОП Критерію 2 акредитації, згідно з висновком експертної групи: ")
    exp_op_compliance_level_criterion_3_according_to_expert_group = input(
        "Enter expected Рівень відповідності ОП Критерію 3 акредитації, згідно з висновком експертної групи: ")
    exp_op_compliance_level_criterion_4_according_to_expert_group = input(
        "Enter expected Рівень відповідності ОП Критерію 4 акредитації, згідно з висновком експертної групи: ")
    exp_op_compliance_level_criterion_5_according_to_expert_group = input(
        "Enter expected Рівень відповідності ОП Критерію 5 акредитації, згідно з висновком експертної групи: ")
    exp_op_compliance_level_criterion_6_according_to_expert_group = input(
        "Enter expected Рівень відповідності ОП Критерію 6 акредитації, згідно з висновком експертної групи: ")
    exp_op_compliance_level_criterion_7_according_to_expert_group = input(
        "Enter expected Рівень відповідності ОП Критерію 7 акредитації, згідно з висновком експертної групи: ")
    exp_op_compliance_level_criterion_8_according_to_expert_group = input(
        "Enter expected Рівень відповідності ОП Критерію 8 акредитації, згідно з висновком експертної групи: ")
    exp_op_compliance_level_criterion_9_according_to_expert_group = input(
        "Enter expected Рівень відповідності ОП Критерію 9 акредитації, згідно з висновком експертної групи: ")
    exp_op_compliance_level_criterion_10_according_to_expert_group = input(
        "Enter expected Рівень відповідності ОП Критерію 10 акредитації, згідно з висновком експертної групи: ")

    #GER
    exp_op_compliance_level_criterion_1_according_to_ger = input(
        "Enter expected Рівень відповідності ОП Критерію 1 акредитації, згідно з висновком ГЕР: ")
    exp_op_compliance_level_criterion_2_according_to_ger = input(
        "Enter expected Рівень відповідності ОП Критерію 2 акредитації, згідно з висновком ГЕР: ")
    exp_op_compliance_level_criterion_3_according_to_ger = input(
        "Enter expected Рівень відповідності ОП Критерію 3 акредитації, згідно з висновком ГЕР: ")
    exp_op_compliance_level_criterion_4_according_to_ger = input(
        "Enter expected Рівень відповідності ОП Критерію 4 акредитації, згідно з висновком ГЕР: ")
    exp_op_compliance_level_criterion_5_according_to_ger = input(
        "Enter expected Рівень відповідності ОП Критерію 5 акредитації, згідно з висновком ГЕР: ")
    exp_op_compliance_level_criterion_6_according_to_ger = input(
        "Enter expected Рівень відповідності ОП Критерію 6 акредитації, згідно з висновком ГЕР: ")
    exp_op_compliance_level_criterion_7_according_to_ger = input(
        "Enter expected Рівень відповідності ОП Критерію 7 акредитації, згідно з висновком ГЕР: ")
    exp_op_compliance_level_criterion_8_according_to_ger = input(
        "Enter expected Рівень відповідності ОП Критерію 8 акредитації, згідно з висновком ГЕР: ")
    exp_op_compliance_level_criterion_9_according_to_ger = input(
        "Enter expected Рівень відповідності ОП Критерію 9 акредитації, згідно з висновком ГЕР: ")
    exp_op_compliance_level_criterion_10_according_to_ger = input(
        "Enter expected Рівень відповідності ОП Критерію 10 акредитації, згідно з висновком ГЕР: ")
    # TODO: Add Часові межі criteria
    # Construct table headers for csv file
    csv_table_headers = []
    criteria = []

    # Check if user specified criteria for filtration
    if exp_id_program:
        criteria.append([get_id_program, exp_id_program])
        csv_table_headers.append("ID")
    if exp_request_number:
        criteria.append([get_request_number, exp_request_number])
        csv_table_headers.append("Номер AC")
    if exp_id_edebo:
        criteria.append([get_id_from_edebo, exp_id_edebo])
        csv_table_headers.append("ID програми в ЄДЕБО")
    if exp_higher_education_name:
        criteria.append([get_higher_education_name, exp_higher_education_name])
        csv_table_headers.append("Назва університету")
    if exp_higher_education_level:
        criteria.append([get_higher_education_level_from_all, exp_higher_education_level])
        csv_table_headers.append("Рівень вищої освіти")
    if exp_knowledge_area:
        criteria.append([get_knowledge_area_from_all, exp_knowledge_area])
        csv_table_headers.append("Галузь знань")
    if exp_speciality:
        criteria.append([get_speciality_from_all, exp_speciality])
        csv_table_headers.append("Спеціальність")
    if exp_op:
        criteria.append([get_op, exp_op])
        csv_table_headers.append("Назва ОП")
    # TODO: Add get_results_of_consideration_of_the_{eg, ger, na}, get_date_of_na_adoption_on_op_accreditation
    if exp_date_of_na_order_on_appointment_of_expert_group:
        exp_date_of_na_order_on_appointment_of_expert_group += "T00:00:00"
        criteria.append([get_date_of_na_order_on_appointment_of_expert_group,
                         exp_date_of_na_order_on_appointment_of_expert_group])
        csv_table_headers.append("Дата наказу НА про призначення експертної групи")
    if exp_number_of_na_order_on_appointment_of_expert_group:
        criteria.append([get_number_of_na_order_on_appointment_of_expert_group,
                         exp_number_of_na_order_on_appointment_of_expert_group])
        csv_table_headers.append("Номер наказу НА про призначення експертної групи")
    if exp_departure_start_date:
        exp_departure_start_date += "T00:00:00"
        criteria.append([get_departure_start_date, exp_departure_start_date])
        csv_table_headers.append("Дата початку виїзду")
    if exp_last_name_of_expert_leader:
        criteria.append([get_last_name_of_expert_leader, exp_last_name_of_expert_leader])
        csv_table_headers.append("Прізвище лідера експертної групи")
    # TODO: Add get_last_name_of_expert criteria
    if exp_surname_of_ger_speaker:
        criteria.append([get_surname_of_ger_speaker, exp_surname_of_ger_speaker])
        csv_table_headers.append("Прізвище доповідача ГЕР")

    # EG
    if exp_op_compliance_level_criterion_1_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_1_according_to_expert_group,
                         exp_op_compliance_level_criterion_1_according_to_expert_group])
        csv_table_headers.append("Рівень відповідності ОП Критерію 1 акредитації, згідно з висновком експертної групи")

    if exp_op_compliance_level_criterion_2_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_2_according_to_expert_group,
                         exp_op_compliance_level_criterion_2_according_to_expert_group])
        csv_table_headers.append("Рівень відповідності ОП Критерію 2 акредитації, згідно з висновком експертної групи")
    if exp_op_compliance_level_criterion_3_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_3_according_to_expert_group,
                         exp_op_compliance_level_criterion_3_according_to_expert_group])
        csv_table_headers.append("Рівень відповідності ОП Критерію 3 акредитації, згідно з висновком експертної групи")
    if exp_op_compliance_level_criterion_4_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_4_according_to_expert_group,
                         exp_op_compliance_level_criterion_4_according_to_expert_group])
        csv_table_headers.append("Рівень відповідності ОП Критерію 4 акредитації, згідно з висновком експертної групи")
    if exp_op_compliance_level_criterion_5_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_5_according_to_expert_group,
                         exp_op_compliance_level_criterion_5_according_to_expert_group])
        csv_table_headers.append("Рівень відповідності ОП Критерію 5 акредитації, згідно з висновком експертної групи")
    if exp_op_compliance_level_criterion_6_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_6_according_to_expert_group,
                         exp_op_compliance_level_criterion_6_according_to_expert_group])
        csv_table_headers.append("Рівень відповідності ОП Критерію 6 акредитації, згідно з висновком експертної групи")
    if exp_op_compliance_level_criterion_7_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_7_according_to_expert_group,
                         exp_op_compliance_level_criterion_7_according_to_expert_group])
        csv_table_headers.append("Рівень відповідності ОП Критерію 7 акредитації, згідно з висновком експертної групи")
    if exp_op_compliance_level_criterion_8_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_8_according_to_expert_group,
                         exp_op_compliance_level_criterion_8_according_to_expert_group])
        csv_table_headers.append("Рівень відповідності ОП Критерію 8 акредитації, згідно з висновком експертної групи")
    if exp_op_compliance_level_criterion_9_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_9_according_to_expert_group,
                         exp_op_compliance_level_criterion_9_according_to_expert_group])
        csv_table_headers.append("Рівень відповідності ОП Критерію 9 акредитації, згідно з висновком експертної групи")
    if exp_op_compliance_level_criterion_10_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_10_according_to_expert_group,
                         exp_op_compliance_level_criterion_10_according_to_expert_group])
        csv_table_headers.append("Рівень відповідності ОП Критерію 10 акредитації, згідно з висновком експертної групи")

    #GER
    if exp_op_compliance_level_criterion_1_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_1_according_to_ger,
                         exp_op_compliance_level_criterion_1_according_to_ger])
        csv_table_headers.append("Рівень відповідності ОП Критерію 1 акредитації, згідно з висновком ГЕР")
    if exp_op_compliance_level_criterion_2_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_2_according_to_ger,
                         exp_op_compliance_level_criterion_2_according_to_ger])
        csv_table_headers.append("Рівень відповідності ОП Критерію 2 акредитації, згідно з висновком ГЕР")
    if exp_op_compliance_level_criterion_3_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_3_according_to_ger,
                         exp_op_compliance_level_criterion_3_according_to_ger])
        csv_table_headers.append("Рівень відповідності ОП Критерію 3 акредитації, згідно з висновком ГЕР")
    if exp_op_compliance_level_criterion_4_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_4_according_to_ger,
                         exp_op_compliance_level_criterion_4_according_to_ger])
        csv_table_headers.append("Рівень відповідності ОП Критерію 4 акредитації, згідно з висновком ГЕР")
    if exp_op_compliance_level_criterion_5_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_5_according_to_ger,
                         exp_op_compliance_level_criterion_5_according_to_ger])
        csv_table_headers.append("Рівень відповідності ОП Критерію 5 акредитації, згідно з висновком ГЕР")
    if exp_op_compliance_level_criterion_6_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_6_according_to_ger,
                         exp_op_compliance_level_criterion_6_according_to_ger])
        csv_table_headers.append("Рівень відповідності ОП Критерію 6 акредитації, згідно з висновком ГЕР")
    if exp_op_compliance_level_criterion_7_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_7_according_to_ger,
                         exp_op_compliance_level_criterion_7_according_to_ger])
        csv_table_headers.append("Рівень відповідності ОП Критерію 7 акредитації, згідно з висновком ГЕР")
    if exp_op_compliance_level_criterion_8_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_8_according_to_ger,
                         exp_op_compliance_level_criterion_8_according_to_ger])
        csv_table_headers.append("Рівень відповідності ОП Критерію 8 акредитації, згідно з висновком ГЕР")
    if exp_op_compliance_level_criterion_9_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_9_according_to_ger,
                         exp_op_compliance_level_criterion_9_according_to_ger])
        csv_table_headers.append("Рівень відповідності ОП Критерію 9 акредитації, згідно з висновком ГЕР")
    if exp_op_compliance_level_criterion_10_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_10_according_to_ger,
                         exp_op_compliance_level_criterion_10_according_to_ger])
        csv_table_headers.append("Рівень відповідності ОП Критерію 10 акредитації, згідно з висновком ГЕР")


    logging.info("Criteria list: %s", criteria)
    logging.info("Scv table headers: %s", csv_table_headers)

    build_csv([csv_table_headers])
    return criteria
