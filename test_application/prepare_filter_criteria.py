import logging
from filter_params import *
from manipulate_csv import build_csv

# Set logging level
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

# Filtration criteria constants. Columns in csv file
ID_PROGRAM = "ID"
AC_NUMBER = "Номер AC"
ID_EDEBO = "ID програми в ЄДЕБО"
HIGHER_EDUCATION_NAME = "Назва університету"
HIGHER_EDUCATION_LEVEL = "Рівень вищої освіти"
KNOWLEDGE_AREA = "Галузь знань"
SPECIALITY = "Спеціальність"
OP_NAME = "Назва ОП"
RESULTS_OD_CONSIDERATION_OF_THE_EG = "За результатами розгляду акредитаційної справи ЕГ"
RESULTS_OD_CONSIDERATION_OF_THE_GER = "За результатами розгляду акредитаційної справи ГЕР"
RESULTS_OD_CONSIDERATION_OF_THE_NA = "За результатами розгляду акредитаційної справи НА"
DATE_OF_NA_ORDER_ON_APPOINTMENT_OF_EG = "Дата наказу НА про призначення експертної групи"
NUMBER_OF_NA_ORDER_ON_APPOINTMENT_OF_EG = "Номер наказу НА про призначення експертної групи"
DEPARTURE_START_DATE = "Дата початку виїзду"
LAST_NAME_OF_EXPERT_LEADER = "Прізвище лідера експертної групи"
LAST_NAME_OF_EXPERT = "Прізвище експерта"
SURNAME_OF_GER_SPEAKER = "Прізвище доповідача ГЕР"

# Compliance level criterion constants for EG
OP_COMPLIANCE_LVL_CRITERION_1_ACCORDING_TO_EG = "Рівень відповідності ОП Критерію 1 акредитації, згідно з висновком " \
                                                "експертної групи "
OP_COMPLIANCE_LVL_CRITERION_2_ACCORDING_TO_EG = "Рівень відповідності ОП Критерію 2 акредитації, згідно з висновком " \
                                                "експертної групи "
OP_COMPLIANCE_LVL_CRITERION_3_ACCORDING_TO_EG = "Рівень відповідності ОП Критерію 3 акредитації, згідно з висновком " \
                                                "експертної групи "
OP_COMPLIANCE_LVL_CRITERION_4_ACCORDING_TO_EG = "Рівень відповідності ОП Критерію 4 акредитації, згідно з висновком " \
                                                "експертної групи "
OP_COMPLIANCE_LVL_CRITERION_5_ACCORDING_TO_EG = "Рівень відповідності ОП Критерію 5 акредитації, згідно з висновком " \
                                                "експертної групи "
OP_COMPLIANCE_LVL_CRITERION_6_ACCORDING_TO_EG = "Рівень відповідності ОП Критерію 6 акредитації, згідно з висновком " \
                                                "експертної групи "
OP_COMPLIANCE_LVL_CRITERION_7_ACCORDING_TO_EG = "Рівень відповідності ОП Критерію 7 акредитації, згідно з висновком " \
                                                "експертної групи "
OP_COMPLIANCE_LVL_CRITERION_8_ACCORDING_TO_EG = "Рівень відповідності ОП Критерію 8 акредитації, згідно з висновком " \
                                                "експертної групи "
OP_COMPLIANCE_LVL_CRITERION_9_ACCORDING_TO_EG = "Рівень відповідності ОП Критерію 9 акредитації, згідно з висновком " \
                                                "експертної групи "
OP_COMPLIANCE_LVL_CRITERION_10_ACCORDING_TO_EG = "Рівень відповідності ОП Критерію 10 акредитації, згідно з висновком " \
                                                 "експертної групи "

# Compliance level criterion constants for GER
OP_COMPLIANCE_LEVEL_CRITERION_1_ACCORDING_TO_GER = "Рівень відповідності ОП Критерію 1 акредитації, згідно з " \
                                                   "висновком ГЕР "
OP_COMPLIANCE_LEVEL_CRITERION_2_ACCORDING_TO_GER = "Рівень відповідності ОП Критерію 2 акредитації, згідно з " \
                                                   "висновком ГЕР "
OP_COMPLIANCE_LEVEL_CRITERION_3_ACCORDING_TO_GER = "Рівень відповідності ОП Критерію 3 акредитації, згідно з " \
                                                   "висновком ГЕР "
OP_COMPLIANCE_LEVEL_CRITERION_4_ACCORDING_TO_GER = "Рівень відповідності ОП Критерію 4 акредитації, згідно з " \
                                                   "висновком ГЕР "
OP_COMPLIANCE_LEVEL_CRITERION_5_ACCORDING_TO_GER = "Рівень відповідності ОП Критерію 5 акредитації, згідно з " \
                                                   "висновком ГЕР "
OP_COMPLIANCE_LEVEL_CRITERION_6_ACCORDING_TO_GER = "Рівень відповідності ОП Критерію 6 акредитації, згідно з " \
                                                   "висновком ГЕР "
OP_COMPLIANCE_LEVEL_CRITERION_7_ACCORDING_TO_GER = "Рівень відповідності ОП Критерію 7 акредитації, згідно з " \
                                                   "висновком ГЕР "
OP_COMPLIANCE_LEVEL_CRITERION_8_ACCORDING_TO_GER = "Рівень відповідності ОП Критерію 8 акредитації, згідно з " \
                                                   "висновком ГЕР "
OP_COMPLIANCE_LEVEL_CRITERION_9_ACCORDING_TO_GER = "Рівень відповідності ОП Критерію 9 акредитації, згідно з " \
                                                   "висновком ГЕР "
OP_COMPLIANCE_LEVEL_CRITERION_10_ACCORDING_TO_GER = "Рівень відповідності ОП Критерію 10 акредитації, згідно з " \
                                                    "висновком ГЕР "


def prepare_filter_criteria():
    """
    Prepare input criteria for filtration of accreditation cases.
    You could specify the value for criteria to be filtered or pass an empty value to skip filtration for current
    criteria

    :return: List of criteria
    """

    # Collect all filtration criteria from user to make a filtration of accreditation cases.
    logging.info("Specify filtration criteria.\n")
    logging.info(
        "Test Input Filtration: 5329 2248/АС-21 50265 Київська православна богословська академія Доктор філософії\n")
    exp_id_program = input(f"Enter expected '{ID_PROGRAM}': ")
    exp_request_number = input(f"Enter expected '{AC_NUMBER}': ")
    exp_id_edebo = input(f"Enter expected '{ID_EDEBO}': ")
    exp_higher_education_name = input(f"Enter expected '{HIGHER_EDUCATION_NAME}': ")
    exp_higher_education_level = input(f"Enter expected '{HIGHER_EDUCATION_LEVEL}': ")
    exp_knowledge_area = input(f"Enter expected '{KNOWLEDGE_AREA}': ")
    exp_speciality = input(f"Enter expected '{SPECIALITY}': ")
    exp_op_name = input(f"Enter expected '{OP_NAME}': ")

    exp_results_of_consideration_of_the_eg = input(f"Enter expected '{RESULTS_OD_CONSIDERATION_OF_THE_EG}': ")
    exp_results_of_consideration_of_the_ger = input(f"Enter expected '{RESULTS_OD_CONSIDERATION_OF_THE_GER}': ")
    exp_results_of_consideration_of_the_na = input(f"Enter expected '{RESULTS_OD_CONSIDERATION_OF_THE_NA}': ")
    # TODO: Add exp get_date_of_na_adoption_on_op_accreditation criteria

    # В формате год-месяц-день
    exp_date_of_na_order_on_appointment_of_expert_group = input(
        f"Enter expected '{DATE_OF_NA_ORDER_ON_APPOINTMENT_OF_EG}': ")
    exp_number_of_na_order_on_appointment_of_expert_group = input(
        f"Enter expected '{NUMBER_OF_NA_ORDER_ON_APPOINTMENT_OF_EG}': ")
    exp_departure_start_date = input(f"Enter expected '{DEPARTURE_START_DATE}': ")

    # TODO: Update last_name_of_expert_leader to find only by last name. For now we need specify Full name
    exp_last_name_of_expert_leader = input(f"Enter expected '{LAST_NAME_OF_EXPERT_LEADER}': ")
    # TODO: get_last_name_of_expert

    exp_surname_of_ger_speaker = input(f"Enter expected '{SURNAME_OF_GER_SPEAKER}': ")

    # EG
    exp_op_compliance_level_criterion_1_according_to_expert_group = input(
        f"Enter expected '{OP_COMPLIANCE_LVL_CRITERION_1_ACCORDING_TO_EG}': ")
    exp_op_compliance_level_criterion_2_according_to_expert_group = input(
        f"Enter expected '{OP_COMPLIANCE_LVL_CRITERION_2_ACCORDING_TO_EG}': ")
    exp_op_compliance_level_criterion_3_according_to_expert_group = input(
        f"Enter expected '{OP_COMPLIANCE_LVL_CRITERION_3_ACCORDING_TO_EG}': ")
    exp_op_compliance_level_criterion_4_according_to_expert_group = input(
        f"Enter expected '{OP_COMPLIANCE_LVL_CRITERION_4_ACCORDING_TO_EG}': ")
    exp_op_compliance_level_criterion_5_according_to_expert_group = input(
        f"Enter expected '{OP_COMPLIANCE_LVL_CRITERION_5_ACCORDING_TO_EG}': ")
    exp_op_compliance_level_criterion_6_according_to_expert_group = input(
        f"Enter expected '{OP_COMPLIANCE_LVL_CRITERION_6_ACCORDING_TO_EG}': ")
    exp_op_compliance_level_criterion_7_according_to_expert_group = input(
        f"Enter expected '{OP_COMPLIANCE_LVL_CRITERION_7_ACCORDING_TO_EG}': ")
    exp_op_compliance_level_criterion_8_according_to_expert_group = input(
        f"Enter expected '{OP_COMPLIANCE_LVL_CRITERION_8_ACCORDING_TO_EG}': ")
    exp_op_compliance_level_criterion_9_according_to_expert_group = input(
        f"Enter expected '{OP_COMPLIANCE_LVL_CRITERION_9_ACCORDING_TO_EG}': ")
    exp_op_compliance_level_criterion_10_according_to_expert_group = input(
        f"Enter expected '{OP_COMPLIANCE_LVL_CRITERION_10_ACCORDING_TO_EG}': ")

    # Compliance level criterion constants for GER
    exp_op_compliance_level_criterion_1_according_to_ger = input(
        f"Enter expected '{OP_COMPLIANCE_LEVEL_CRITERION_1_ACCORDING_TO_GER}': ")
    exp_op_compliance_level_criterion_2_according_to_ger = input(
        f"Enter expected '{OP_COMPLIANCE_LEVEL_CRITERION_2_ACCORDING_TO_GER}': ")
    exp_op_compliance_level_criterion_3_according_to_ger = input(
        f"Enter expected '{OP_COMPLIANCE_LEVEL_CRITERION_3_ACCORDING_TO_GER}': ")
    exp_op_compliance_level_criterion_4_according_to_ger = input(
        f"Enter expected '{OP_COMPLIANCE_LEVEL_CRITERION_4_ACCORDING_TO_GER}': ")
    exp_op_compliance_level_criterion_5_according_to_ger = input(
        f"Enter expected '{OP_COMPLIANCE_LEVEL_CRITERION_5_ACCORDING_TO_GER}': ")
    exp_op_compliance_level_criterion_6_according_to_ger = input(
        f"Enter expected '{OP_COMPLIANCE_LEVEL_CRITERION_6_ACCORDING_TO_GER}': ")
    exp_op_compliance_level_criterion_7_according_to_ger = input(
        f"Enter expected '{OP_COMPLIANCE_LEVEL_CRITERION_7_ACCORDING_TO_GER}': ")
    exp_op_compliance_level_criterion_8_according_to_ger = input(
        f"Enter expected '{OP_COMPLIANCE_LEVEL_CRITERION_8_ACCORDING_TO_GER}': ")
    exp_op_compliance_level_criterion_9_according_to_ger = input(
        f"Enter expected '{OP_COMPLIANCE_LEVEL_CRITERION_9_ACCORDING_TO_GER}': ")
    exp_op_compliance_level_criterion_10_according_to_ger = input(
        f"Enter expected '{OP_COMPLIANCE_LEVEL_CRITERION_10_ACCORDING_TO_GER}': ")
    # TODO: Add Часові межі criteria
    # Construct table headers for csv file
    csv_table_headers = []
    criteria = []

    # Check if user specified criteria for filtration
    if exp_id_program:
        criteria.append([get_id_program, exp_id_program])
        csv_table_headers.append(ID_PROGRAM)
    if exp_request_number:
        criteria.append([get_request_number, exp_request_number])
        csv_table_headers.append(AC_NUMBER)
    if exp_id_edebo:
        criteria.append([get_id_from_edebo, exp_id_edebo])
        csv_table_headers.append(ID_EDEBO)
    if exp_higher_education_name:
        criteria.append([get_higher_education_name, exp_higher_education_name])
        csv_table_headers.append(HIGHER_EDUCATION_NAME)
    if exp_higher_education_level:
        criteria.append([get_higher_education_level_from_all, exp_higher_education_level])
        csv_table_headers.append(HIGHER_EDUCATION_LEVEL)
    if exp_knowledge_area:
        criteria.append([get_knowledge_area_from_all, exp_knowledge_area])
        csv_table_headers.append(KNOWLEDGE_AREA)
    if exp_speciality:
        criteria.append([get_speciality_from_all, exp_speciality])
        csv_table_headers.append(SPECIALITY)
    if exp_op_name:
        criteria.append([get_op, exp_op_name])
        csv_table_headers.append(OP_NAME)
    if exp_results_of_consideration_of_the_eg:
        criteria.append([get_results_of_consideration_of_the_eg, exp_results_of_consideration_of_the_eg])
        csv_table_headers.append(RESULTS_OD_CONSIDERATION_OF_THE_EG)
    if exp_results_of_consideration_of_the_ger:
        criteria.append([get_results_of_consideration_of_the_ger, exp_results_of_consideration_of_the_ger])
        csv_table_headers.append(RESULTS_OD_CONSIDERATION_OF_THE_GER)
    if exp_results_of_consideration_of_the_na:
        criteria.append([get_results_of_consideration_of_the_na, exp_results_of_consideration_of_the_na])
        csv_table_headers.append(RESULTS_OD_CONSIDERATION_OF_THE_NA)
    # TODO: Add get_date_of_na_adoption_on_op_accreditation criteria
    if exp_date_of_na_order_on_appointment_of_expert_group:
        exp_date_of_na_order_on_appointment_of_expert_group += "T00:00:00"
        criteria.append([get_date_of_na_order_on_appointment_of_expert_group,
                         exp_date_of_na_order_on_appointment_of_expert_group])
        csv_table_headers.append(DATE_OF_NA_ORDER_ON_APPOINTMENT_OF_EG)
    if exp_number_of_na_order_on_appointment_of_expert_group:
        criteria.append([get_number_of_na_order_on_appointment_of_expert_group,
                         exp_number_of_na_order_on_appointment_of_expert_group])
        csv_table_headers.append(NUMBER_OF_NA_ORDER_ON_APPOINTMENT_OF_EG)
    if exp_departure_start_date:
        exp_departure_start_date += "T00:00:00"
        criteria.append([get_departure_start_date, exp_departure_start_date])
        csv_table_headers.append(DEPARTURE_START_DATE)
    if exp_last_name_of_expert_leader:
        criteria.append([get_last_name_of_expert_leader, exp_last_name_of_expert_leader])
        csv_table_headers.append(LAST_NAME_OF_EXPERT_LEADER)
    # TODO: Add get_last_name_of_expert criteria
    if exp_surname_of_ger_speaker:
        criteria.append([get_surname_of_ger_speaker, exp_surname_of_ger_speaker])
        csv_table_headers.append(SURNAME_OF_GER_SPEAKER)

    # compliance level criterion for EG
    if exp_op_compliance_level_criterion_1_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_1_according_to_expert_group,
                         exp_op_compliance_level_criterion_1_according_to_expert_group])
        csv_table_headers.append(OP_COMPLIANCE_LVL_CRITERION_1_ACCORDING_TO_EG)
    if exp_op_compliance_level_criterion_2_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_2_according_to_expert_group,
                         exp_op_compliance_level_criterion_2_according_to_expert_group])
        csv_table_headers.append(OP_COMPLIANCE_LVL_CRITERION_2_ACCORDING_TO_EG)
    if exp_op_compliance_level_criterion_3_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_3_according_to_expert_group,
                         exp_op_compliance_level_criterion_3_according_to_expert_group])
        csv_table_headers.append(OP_COMPLIANCE_LVL_CRITERION_3_ACCORDING_TO_EG)
    if exp_op_compliance_level_criterion_4_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_4_according_to_expert_group,
                         exp_op_compliance_level_criterion_4_according_to_expert_group])
        csv_table_headers.append(OP_COMPLIANCE_LVL_CRITERION_4_ACCORDING_TO_EG)
    if exp_op_compliance_level_criterion_5_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_5_according_to_expert_group,
                         exp_op_compliance_level_criterion_5_according_to_expert_group])
        csv_table_headers.append(OP_COMPLIANCE_LVL_CRITERION_5_ACCORDING_TO_EG)
    if exp_op_compliance_level_criterion_6_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_6_according_to_expert_group,
                         exp_op_compliance_level_criterion_6_according_to_expert_group])
        csv_table_headers.append(OP_COMPLIANCE_LVL_CRITERION_6_ACCORDING_TO_EG)
    if exp_op_compliance_level_criterion_7_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_7_according_to_expert_group,
                         exp_op_compliance_level_criterion_7_according_to_expert_group])
        csv_table_headers.append(OP_COMPLIANCE_LVL_CRITERION_7_ACCORDING_TO_EG)
    if exp_op_compliance_level_criterion_8_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_8_according_to_expert_group,
                         exp_op_compliance_level_criterion_8_according_to_expert_group])
        csv_table_headers.append(OP_COMPLIANCE_LVL_CRITERION_8_ACCORDING_TO_EG)
    if exp_op_compliance_level_criterion_9_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_9_according_to_expert_group,
                         exp_op_compliance_level_criterion_9_according_to_expert_group])
        csv_table_headers.append(OP_COMPLIANCE_LVL_CRITERION_9_ACCORDING_TO_EG)
    if exp_op_compliance_level_criterion_10_according_to_expert_group:
        criteria.append([get_op_compliance_level_criterion_10_according_to_expert_group,
                         exp_op_compliance_level_criterion_10_according_to_expert_group])
        csv_table_headers.append(OP_COMPLIANCE_LVL_CRITERION_10_ACCORDING_TO_EG)

    # compliance level criterion for GER
    if exp_op_compliance_level_criterion_1_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_1_according_to_ger,
                         exp_op_compliance_level_criterion_1_according_to_ger])
        csv_table_headers.append(OP_COMPLIANCE_LEVEL_CRITERION_1_ACCORDING_TO_GER)
    if exp_op_compliance_level_criterion_2_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_2_according_to_ger,
                         exp_op_compliance_level_criterion_2_according_to_ger])
        csv_table_headers.append(OP_COMPLIANCE_LEVEL_CRITERION_2_ACCORDING_TO_GER)
    if exp_op_compliance_level_criterion_3_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_3_according_to_ger,
                         exp_op_compliance_level_criterion_3_according_to_ger])
        csv_table_headers.append(OP_COMPLIANCE_LEVEL_CRITERION_3_ACCORDING_TO_GER)
    if exp_op_compliance_level_criterion_4_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_4_according_to_ger,
                         exp_op_compliance_level_criterion_4_according_to_ger])
        csv_table_headers.append(OP_COMPLIANCE_LEVEL_CRITERION_4_ACCORDING_TO_GER)
    if exp_op_compliance_level_criterion_5_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_5_according_to_ger,
                         exp_op_compliance_level_criterion_5_according_to_ger])
        csv_table_headers.append(OP_COMPLIANCE_LEVEL_CRITERION_5_ACCORDING_TO_GER)
    if exp_op_compliance_level_criterion_6_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_6_according_to_ger,
                         exp_op_compliance_level_criterion_6_according_to_ger])
        csv_table_headers.append(OP_COMPLIANCE_LEVEL_CRITERION_6_ACCORDING_TO_GER)
    if exp_op_compliance_level_criterion_7_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_7_according_to_ger,
                         exp_op_compliance_level_criterion_7_according_to_ger])
        csv_table_headers.append(OP_COMPLIANCE_LEVEL_CRITERION_7_ACCORDING_TO_GER)
    if exp_op_compliance_level_criterion_8_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_8_according_to_ger,
                         exp_op_compliance_level_criterion_8_according_to_ger])
        csv_table_headers.append(OP_COMPLIANCE_LEVEL_CRITERION_8_ACCORDING_TO_GER)
    if exp_op_compliance_level_criterion_9_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_9_according_to_ger,
                         exp_op_compliance_level_criterion_9_according_to_ger])
        csv_table_headers.append(OP_COMPLIANCE_LEVEL_CRITERION_9_ACCORDING_TO_GER)
    if exp_op_compliance_level_criterion_10_according_to_ger:
        criteria.append([get_op_compliance_level_criterion_10_according_to_ger,
                         exp_op_compliance_level_criterion_10_according_to_ger])
        csv_table_headers.append(OP_COMPLIANCE_LEVEL_CRITERION_10_ACCORDING_TO_GER)

    logging.info("Criteria list: %s", criteria)
    logging.info("Scv table headers: %s", csv_table_headers)

    build_csv([csv_table_headers])
    return criteria
