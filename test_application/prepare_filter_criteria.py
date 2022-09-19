import logging
from manipulate_csv import build_csv
from constants import \
    ID_PROGRAM, \
    AC_NUMBER, \
    ID_EDEBO, \
    HIGHER_EDUCATION_NAME, \
    HIGHER_EDUCATION_LEVEL, \
    KNOWLEDGE_AREA, \
    SPECIALITY, \
    OP_NAME, \
    RESULTS_OD_CONSIDERATION_OF_THE_EG, \
    RESULTS_OD_CONSIDERATION_OF_THE_GER, \
    RESULTS_OD_CONSIDERATION_OF_THE_NA, \
    DATE_OF_NA_ORDER_ON_APPOINTMENT_OF_EG, \
    NUMBER_OF_NA_ORDER_ON_APPOINTMENT_OF_EG, \
    DEPARTURE_START_DATE, \
    LAST_NAME_OF_EXPERT_LEADER, \
    LAST_NAME_OF_EXPERT, \
    SURNAME_OF_GER_SPEAKER, \
    OP_COMPL_LVL_CRITERION_1_ACC_TO_EG, \
    OP_COMPL_LVL_CRITERION_2_ACC_TO_EG, \
    OP_COMPL_LVL_CRITERION_3_ACC_TO_EG, \
    OP_COMPL_LVL_CRITERION_4_ACC_TO_EG, \
    OP_COMPL_LVL_CRITERION_5_ACC_TO_EG, \
    OP_COMPL_LVL_CRITERION_6_ACC_TO_EG, \
    OP_COMPL_LVL_CRITERION_7_ACC_TO_EG, \
    OP_COMPL_LVL_CRITERION_8_ACC_TO_EG, \
    OP_COMPL_LVL_CRITERION_9_ACC_TO_EG, \
    OP_COMPL_LVL_CRITERION_10_ACC_TO_EG, \
    OP_COMPL_LEVEL_CRITERION_1_ACC_TO_GER, \
    OP_COMPL_LEVEL_CRITERION_2_ACC_TO_GER, \
    OP_COMPL_LEVEL_CRITERION_3_ACC_TO_GER, \
    OP_COMPL_LEVEL_CRITERION_4_ACC_TO_GER, \
    OP_COMPL_LEVEL_CRITERION_5_ACC_TO_GER, \
    OP_COMPL_LEVEL_CRITERION_6_ACC_TO_GER, \
    OP_COMPL_LEVEL_CRITERION_7_ACC_TO_GER, \
    OP_COMPL_LEVEL_CRITERION_8_ACC_TO_GER, \
    OP_COMPL_LEVEL_CRITERION_9_ACC_TO_GER, \
    OP_COMPL_LEVEL_CRITERION_10_ACC_TO_GER, \
    DEFAULT_CSV_TABLE_HEADERS, \
    DEFAULT_FILTRATION_CRITERIA, \
    INPUT_CRITERIA_FUNCTION_LIST, \
    CSV_COLUMN_NAME_LIST

# Set logging level
# TODO: Configure this information with help of Poetry(in .toml file)
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


def update_csv_headers(header):
    """
    Update scv table headers. Set up default headers if no headers
     is passed to function or update scv table with passed headers
     """
    default_headers = DEFAULT_CSV_TABLE_HEADERS
    if header not in default_headers:
        DEFAULT_CSV_TABLE_HEADERS.append(header)

    return DEFAULT_CSV_TABLE_HEADERS


def prepare_filter_criteria():
    """
    Prepare input criteria for filtration of accreditation cases.
    You could specify the value for criteria to be filtered or pass
    an empty value to skip filtration for current criteria.

    :return: List of criteria
    """

    # Collect all filtration criteria from user to make a filtration of accreditation cases.
    logging.info("Specify filtration criteria.\n")
    logging.info("'ID': '6246'")
    logging.info("'Номер AC': '0793/АС-22'")
    logging.info("'ID програми в ЄДЕБО': 43443")
    logging.info(
        'Назва університету: Комунальний заклад "Уманський гуманітарно-педагогічний'
        ' фаховий коледж ім. Т.Г. Шевченка Черкаської обласної ради"')
    logging.info("'Рівень вищої освіти': Бакалавр")
    logging.info("'Галузь знань': 01 Освіта/Педагогіка")
    logging.info("'Спеціальність': 014 Середня освіта")
    logging.info("'Назва ОП': Середня освіта (Музичне мистецтво)."
                 " Музичне мистецтво в закладі дошкільної освіти")

    # Input filtration values
    exp_id_program = input(f"Enter expected '{ID_PROGRAM}': ")
    exp_request_number = input(f"Enter expected '{AC_NUMBER}': ")
    exp_id_edebo = input(f"Enter expected '{ID_EDEBO}': ")
    exp_higher_education_name = input(f"Enter expected '{HIGHER_EDUCATION_NAME}': ")
    exp_higher_education_level = input(f"Enter expected '{HIGHER_EDUCATION_LEVEL}': ")
    exp_knowledge_area = input(f"Enter expected '{KNOWLEDGE_AREA}': ")
    exp_speciality = input(f"Enter expected '{SPECIALITY}': ")
    exp_op_name = input(f"Enter expected '{OP_NAME}': ")

    exp_results_of_consideration_of_the_eg = input(
        f"Enter expected '{RESULTS_OD_CONSIDERATION_OF_THE_EG}': "
    )
    exp_results_of_consideration_of_the_ger = input(
        f"Enter expected '{RESULTS_OD_CONSIDERATION_OF_THE_GER}': "
    )
    exp_results_of_consideration_of_the_na = input(
        f"Enter expected '{RESULTS_OD_CONSIDERATION_OF_THE_NA}': "
    )
    # TODO: Add exp get_date_of_na_adoption_on_op_accreditation criteria

    # В формате год-месяц-день
    exp_date_of_na_order_on_appointment_of_expert_group = input(
        f"Enter expected '{DATE_OF_NA_ORDER_ON_APPOINTMENT_OF_EG}': "
    )
    exp_number_of_na_order_on_appointment_of_expert_group = input(
        f"Enter expected '{NUMBER_OF_NA_ORDER_ON_APPOINTMENT_OF_EG}': "
    )
    exp_departure_start_date = input(f"Enter expected '{DEPARTURE_START_DATE}': ")
    # TODO: Update last_name_of_expert_leader to find only by last name.
    #  For now we need specify Full name
    exp_last_name_of_expert_leader = input(
        f"Enter expected '{LAST_NAME_OF_EXPERT_LEADER}': "
    )
    # TODO: get_last_name_of_expert
    exp_get_last_name_of_expert = input(
        f"Enter expected '{LAST_NAME_OF_EXPERT}': "
    )
    exp_surname_of_ger_speaker = input(f"Enter expected '{SURNAME_OF_GER_SPEAKER}': ")

    # EG
    exp_op_compliance_level_criterion_1_according_to_expert_group = input(
        f"Enter expected '{OP_COMPL_LVL_CRITERION_1_ACC_TO_EG}': ")
    exp_op_compliance_level_criterion_2_according_to_expert_group = input(
        f"Enter expected '{OP_COMPL_LVL_CRITERION_2_ACC_TO_EG}': ")
    exp_op_compliance_level_criterion_3_according_to_expert_group = input(
        f"Enter expected '{OP_COMPL_LVL_CRITERION_3_ACC_TO_EG}': ")
    exp_op_compliance_level_criterion_4_according_to_expert_group = input(
        f"Enter expected '{OP_COMPL_LVL_CRITERION_4_ACC_TO_EG}': ")
    exp_op_compliance_level_criterion_5_according_to_expert_group = input(
        f"Enter expected '{OP_COMPL_LVL_CRITERION_5_ACC_TO_EG}': ")
    exp_op_compliance_level_criterion_6_according_to_expert_group = input(
        f"Enter expected '{OP_COMPL_LVL_CRITERION_6_ACC_TO_EG}': ")
    exp_op_compliance_level_criterion_7_according_to_expert_group = input(
        f"Enter expected '{OP_COMPL_LVL_CRITERION_7_ACC_TO_EG}': ")
    exp_op_compliance_level_criterion_8_according_to_expert_group = input(
        f"Enter expected '{OP_COMPL_LVL_CRITERION_8_ACC_TO_EG}': ")
    exp_op_compliance_level_criterion_9_according_to_expert_group = input(
        f"Enter expected '{OP_COMPL_LVL_CRITERION_9_ACC_TO_EG}': ")
    exp_op_compliance_level_criterion_10_according_to_expert_group = input(
        f"Enter expected '{OP_COMPL_LVL_CRITERION_10_ACC_TO_EG}': ")

    # Compliance level criterion constants for GER
    exp_op_compliance_level_criterion_1_according_to_ger = input(
        f"Enter expected '{OP_COMPL_LEVEL_CRITERION_1_ACC_TO_GER}': ")
    exp_op_compliance_level_criterion_2_according_to_ger = input(
        f"Enter expected '{OP_COMPL_LEVEL_CRITERION_2_ACC_TO_GER}': ")
    exp_op_compliance_level_criterion_3_according_to_ger = input(
        f"Enter expected '{OP_COMPL_LEVEL_CRITERION_3_ACC_TO_GER}': ")
    exp_op_compliance_level_criterion_4_according_to_ger = input(
        f"Enter expected '{OP_COMPL_LEVEL_CRITERION_4_ACC_TO_GER}': ")
    exp_op_compliance_level_criterion_5_according_to_ger = input(
        f"Enter expected '{OP_COMPL_LEVEL_CRITERION_5_ACC_TO_GER}': ")
    exp_op_compliance_level_criterion_6_according_to_ger = input(
        f"Enter expected '{OP_COMPL_LEVEL_CRITERION_6_ACC_TO_GER}': ")
    exp_op_compliance_level_criterion_7_according_to_ger = input(
        f"Enter expected '{OP_COMPL_LEVEL_CRITERION_7_ACC_TO_GER}': ")
    exp_op_compliance_level_criterion_8_according_to_ger = input(
        f"Enter expected '{OP_COMPL_LEVEL_CRITERION_8_ACC_TO_GER}': ")
    exp_op_compliance_level_criterion_9_according_to_ger = input(
        f"Enter expected '{OP_COMPL_LEVEL_CRITERION_9_ACC_TO_GER}': ")
    exp_op_compliance_level_criterion_10_according_to_ger = input(
        f"Enter expected '{OP_COMPL_LEVEL_CRITERION_10_ACC_TO_GER}': ")
    # TODO: Add Часові межі criteria

    input_criteria_value_list = [
        exp_id_program,
        exp_request_number,
        exp_id_edebo,
        exp_higher_education_name,
        exp_higher_education_level,
        exp_knowledge_area,
        exp_speciality,
        exp_op_name,
        exp_results_of_consideration_of_the_eg,
        exp_results_of_consideration_of_the_ger,
        exp_results_of_consideration_of_the_na,
        exp_date_of_na_order_on_appointment_of_expert_group,
        exp_number_of_na_order_on_appointment_of_expert_group,
        exp_departure_start_date,
        exp_last_name_of_expert_leader,
        exp_get_last_name_of_expert,
        exp_surname_of_ger_speaker,
        exp_op_compliance_level_criterion_1_according_to_expert_group,
        exp_op_compliance_level_criterion_2_according_to_expert_group,
        exp_op_compliance_level_criterion_3_according_to_expert_group,
        exp_op_compliance_level_criterion_4_according_to_expert_group,
        exp_op_compliance_level_criterion_5_according_to_expert_group,
        exp_op_compliance_level_criterion_6_according_to_expert_group,
        exp_op_compliance_level_criterion_7_according_to_expert_group,
        exp_op_compliance_level_criterion_8_according_to_expert_group,
        exp_op_compliance_level_criterion_9_according_to_expert_group,
        exp_op_compliance_level_criterion_10_according_to_expert_group,
        exp_op_compliance_level_criterion_1_according_to_ger,
        exp_op_compliance_level_criterion_2_according_to_ger,
        exp_op_compliance_level_criterion_3_according_to_ger,
        exp_op_compliance_level_criterion_4_according_to_ger,
        exp_op_compliance_level_criterion_5_according_to_ger,
        exp_op_compliance_level_criterion_6_according_to_ger,
        exp_op_compliance_level_criterion_7_according_to_ger,
        exp_op_compliance_level_criterion_8_according_to_ger,
        exp_op_compliance_level_criterion_9_according_to_ger,
        exp_op_compliance_level_criterion_10_according_to_ger
    ]

    # Construct table headers for csv file
    csv_table_headers = []
    criteria = []

    # Construct criteria list and headers for csv file
    for i in zip(INPUT_CRITERIA_FUNCTION_LIST, input_criteria_value_list, CSV_COLUMN_NAME_LIST):
        current_criteria_value = i[1]
        current_criteria_function = i[0]
        current_column_name = i[2]

        if current_criteria_value:
            csv_table_headers = update_csv_headers(current_column_name)

        if current_criteria_function in DEFAULT_FILTRATION_CRITERIA and not current_criteria_value:
            criteria.append([current_criteria_function, "default_criteria"])
        elif current_criteria_value != '':
            criteria.append([current_criteria_function, current_criteria_value])

    # TODO: Add get_date_of_na_adoption_on_op_accreditation criteria
    # TODO: Add get_time_na_meeting criteria

    logging.info("Criteria list: %s", criteria)
    logging.info("Csv table headers: %s", csv_table_headers)

    build_csv([csv_table_headers])
    return criteria
