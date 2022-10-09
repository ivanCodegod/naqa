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
    DATE_OF_NA_ADOPTION_ON_OP_ACCREDITATION, \
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
    CSV_COLUMN_NAME_LIST, \
    IN_FORMAT_YEAR_MONTH_DAY, \
    IN_FORMAT_YEAR_MONTH_DAY_T, \
    IN_FORMAT_FULL_NAME, \
    POSSIBLE_VARIANTS_FOR_EG_AND_GER, \
    POSSIBLE_VARIANTS_OF_CONSIDERATION_NA, \
    POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG, \
    POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER, \
    TIME_NA_MEETING, \
    IN_FORMAT_TIME_NA_MEETING

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


def input_filtration_criteria(criteria, additional_comment=""):
    """Decorate text connected with filter parameter."""
    text = f"Введіть очікуваний '{criteria}' параметр для фільтрації"
    return text + ": " if not additional_comment else text + "." + f" {additional_comment}: "


def get_input_criteria():
    """
    Get input criteria for filtration.
    :return: list of input criteria
    """

    # Input filtration values
    exp_id_program = input(input_filtration_criteria(ID_PROGRAM))
    exp_request_number = input(input_filtration_criteria(AC_NUMBER))
    exp_id_edebo = input(input_filtration_criteria(ID_EDEBO))
    exp_higher_education_name = input(input_filtration_criteria(HIGHER_EDUCATION_NAME))
    exp_higher_education_level = input(input_filtration_criteria(HIGHER_EDUCATION_LEVEL))
    exp_knowledge_area = input(input_filtration_criteria(KNOWLEDGE_AREA))
    exp_speciality = input(input_filtration_criteria(SPECIALITY))
    exp_op_name = input(input_filtration_criteria(OP_NAME))
    exp_results_of_consideration_of_the_eg = input(
        input_filtration_criteria(RESULTS_OD_CONSIDERATION_OF_THE_EG,
                                  POSSIBLE_VARIANTS_FOR_EG_AND_GER)
    )
    exp_results_of_consideration_of_the_ger = input(
        input_filtration_criteria(RESULTS_OD_CONSIDERATION_OF_THE_GER,
                                  POSSIBLE_VARIANTS_FOR_EG_AND_GER)
    )
    exp_results_of_consideration_of_the_na = input(
        input_filtration_criteria(RESULTS_OD_CONSIDERATION_OF_THE_NA,
                                  POSSIBLE_VARIANTS_OF_CONSIDERATION_NA)
    )
    exp_date_of_na_adoption_on_op_accreditation = input(
        input_filtration_criteria(DATE_OF_NA_ADOPTION_ON_OP_ACCREDITATION,
                                  IN_FORMAT_YEAR_MONTH_DAY_T)
    )
    exp_date_of_na_order_on_appointment_of_expert_group = input(
        input_filtration_criteria(DATE_OF_NA_ORDER_ON_APPOINTMENT_OF_EG, IN_FORMAT_YEAR_MONTH_DAY)
    )
    if exp_date_of_na_order_on_appointment_of_expert_group:
        exp_date_of_na_order_on_appointment_of_expert_group += "T00:00:00"

    exp_number_of_na_order_on_appointment_of_expert_group = input(
        input_filtration_criteria(NUMBER_OF_NA_ORDER_ON_APPOINTMENT_OF_EG)
    )
    exp_departure_start_date = input(
        input_filtration_criteria(DEPARTURE_START_DATE, IN_FORMAT_YEAR_MONTH_DAY)
    )
    if exp_departure_start_date:
        exp_departure_start_date += "T00:00:00"
    exp_last_name_of_expert_leader = input(
        input_filtration_criteria(LAST_NAME_OF_EXPERT_LEADER, IN_FORMAT_FULL_NAME)
    )
    exp_get_last_name_of_expert = input(
        input_filtration_criteria(LAST_NAME_OF_EXPERT, IN_FORMAT_FULL_NAME)
    )
    exp_surname_of_ger_speaker = input(
        input_filtration_criteria(SURNAME_OF_GER_SPEAKER, IN_FORMAT_FULL_NAME)
    )

    # EG
    exp_op_compliance_level_criterion_1_according_to_expert_group = input(
        input_filtration_criteria(
            OP_COMPL_LVL_CRITERION_1_ACC_TO_EG,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_2_according_to_expert_group = input(
        input_filtration_criteria(
            OP_COMPL_LVL_CRITERION_2_ACC_TO_EG,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_3_according_to_expert_group = input(
        input_filtration_criteria(
            OP_COMPL_LVL_CRITERION_3_ACC_TO_EG,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_4_according_to_expert_group = input(
        input_filtration_criteria(
            OP_COMPL_LVL_CRITERION_4_ACC_TO_EG,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_5_according_to_expert_group = input(
        input_filtration_criteria(
            OP_COMPL_LVL_CRITERION_5_ACC_TO_EG,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_6_according_to_expert_group = input(
        input_filtration_criteria(
            OP_COMPL_LVL_CRITERION_6_ACC_TO_EG,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_7_according_to_expert_group = input(
        input_filtration_criteria(
            OP_COMPL_LVL_CRITERION_7_ACC_TO_EG,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_8_according_to_expert_group = input(
        input_filtration_criteria(
            OP_COMPL_LVL_CRITERION_8_ACC_TO_EG,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_9_according_to_expert_group = input(
        input_filtration_criteria(
            OP_COMPL_LVL_CRITERION_9_ACC_TO_EG,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_10_according_to_expert_group = input(
        input_filtration_criteria(
            OP_COMPL_LVL_CRITERION_10_ACC_TO_EG,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )

    # Compliance level criterion constants for GER
    exp_op_compliance_level_criterion_1_according_to_ger = input(
        input_filtration_criteria(
            OP_COMPL_LEVEL_CRITERION_1_ACC_TO_GER,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_2_according_to_ger = input(
        input_filtration_criteria(
            OP_COMPL_LEVEL_CRITERION_2_ACC_TO_GER,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_3_according_to_ger = input(
        input_filtration_criteria(
            OP_COMPL_LEVEL_CRITERION_3_ACC_TO_GER,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_4_according_to_ger = input(
        input_filtration_criteria(
            OP_COMPL_LEVEL_CRITERION_4_ACC_TO_GER,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_5_according_to_ger = input(
        input_filtration_criteria(
            OP_COMPL_LEVEL_CRITERION_5_ACC_TO_GER,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_6_according_to_ger = input(
        input_filtration_criteria(
            OP_COMPL_LEVEL_CRITERION_6_ACC_TO_GER,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_7_according_to_ger = input(
        input_filtration_criteria(
            OP_COMPL_LEVEL_CRITERION_7_ACC_TO_GER,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_8_according_to_ger = input(
        input_filtration_criteria(
            OP_COMPL_LEVEL_CRITERION_8_ACC_TO_GER,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_9_according_to_ger = input(
        input_filtration_criteria(
            OP_COMPL_LEVEL_CRITERION_9_ACC_TO_GER,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_10_according_to_ger = input(
        input_filtration_criteria(
            OP_COMPL_LEVEL_CRITERION_10_ACC_TO_GER,
            POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_time_na_meeting = input(
        input_filtration_criteria(
            TIME_NA_MEETING,
            IN_FORMAT_TIME_NA_MEETING
        )
    ).split()

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
        exp_date_of_na_adoption_on_op_accreditation,
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
        exp_op_compliance_level_criterion_10_according_to_ger,
        exp_time_na_meeting
    ]
    return input_criteria_value_list


def prepare_filter_criteria(input_criteria_value_list):
    """
    Prepare input criteria for filtration of accreditation cases.
    You could specify the value for criteria to be filtered or pass
    an empty value to skip filtration for current criteria.

    :return: List of criteria
    """

    # Construct table headers for csv file
    csv_table_headers = []
    criteria = []

    # Construct criteria list and headers for csv file
    for i in zip(INPUT_CRITERIA_FUNCTION_LIST, input_criteria_value_list, CSV_COLUMN_NAME_LIST):
        current_criteria_function, current_criteria_value, current_column_name = i[0], i[1], i[2]

        if current_criteria_value:
            csv_table_headers = update_csv_headers(current_column_name)
        if current_criteria_function in DEFAULT_FILTRATION_CRITERIA and not current_criteria_value:
            criteria.append([current_criteria_function, "default_criteria"])
        elif current_criteria_value != '':
            criteria.append([current_criteria_function, current_criteria_value])

    logging.debug("Criteria list: %s", criteria)
    logging.debug("Csv table headers: %s", csv_table_headers)

    build_csv([csv_table_headers])
    return criteria
