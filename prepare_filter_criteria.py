import os
import logging
from manipulate_csv import build_csv, update_csv_headers
from accreditation_filter_constants import \
    DEFAULT_FILTRATION_FUNCTIONS, \
    FILTRATION_FUNCTIONS, \
    CSV_TABLE_HEADERS, \
    AccreditationFilterConstants, \
    FilterFormatConstants
from project_settings import ProjectSettingsManager


def input_filtration_criteria(criteria: str, additional_comment: str = "") -> str:
    """Decorate text connected with filter parameter."""
    text = f"Введіть очікуваний '{criteria}' параметр для фільтрації"
    return text + ": " if not additional_comment else text + "." + f" {additional_comment}: "


def get_input_values_for_filtration() -> list:
    """
    Prompt the user to input values for filtration.

    :return: A list containing the input values provided by the user for filtration.
    """
    exp_id_program = input(input_filtration_criteria(AccreditationFilterConstants.ID_PROGRAM))
    exp_request_number = input(input_filtration_criteria(AccreditationFilterConstants.AC_NUMBER))
    exp_id_edebo = input(input_filtration_criteria(AccreditationFilterConstants.ID_EDEBO))
    exp_higher_education_name = input(input_filtration_criteria(AccreditationFilterConstants.HIGHER_EDUCATION_NAME))
    exp_higher_education_level = input(input_filtration_criteria(AccreditationFilterConstants.HIGHER_EDUCATION_LEVEL))

    exp_knowledge_area = input(input_filtration_criteria(AccreditationFilterConstants.KNOWLEDGE_AREA))
    # Set knowledge area as env variable
    if exp_knowledge_area:
        os.environ['KNOWLEDGE_AREA'] = exp_knowledge_area.split()[0]
    else:
        os.environ['KNOWLEDGE_AREA'] = ProjectSettingsManager.DEFAULT_KNOWLEDGE_AREA

    exp_speciality = input(input_filtration_criteria(AccreditationFilterConstants.SPECIALITY))
    exp_op_name = input(input_filtration_criteria(AccreditationFilterConstants.OP_NAME))
    exp_results_of_consideration_of_the_eg = input(
        input_filtration_criteria(AccreditationFilterConstants.RESULTS_OD_CONSIDERATION_OF_THE_EG,
                                  FilterFormatConstants.POSSIBLE_VARIANTS_FOR_EG_AND_GER)
    )
    exp_results_of_consideration_of_the_ger = input(
        input_filtration_criteria(AccreditationFilterConstants.RESULTS_OD_CONSIDERATION_OF_THE_GER,
                                  FilterFormatConstants.POSSIBLE_VARIANTS_FOR_EG_AND_GER)
    )
    exp_results_of_consideration_of_the_na = input(
        input_filtration_criteria(AccreditationFilterConstants.RESULTS_OD_CONSIDERATION_OF_THE_NA,
                                  FilterFormatConstants.POSSIBLE_VARIANTS_OF_CONSIDERATION_NA)
    )
    exp_date_of_na_adoption_on_op_accreditation = input(
        input_filtration_criteria(AccreditationFilterConstants.DATE_OF_NA_ADOPTION_ON_OP_ACCREDITATION,
                                  FilterFormatConstants.IN_FORMAT_YEAR_MONTH_DAY_T)
    )
    exp_date_of_na_order_on_appointment_of_expert_group = input(
        input_filtration_criteria(AccreditationFilterConstants.DATE_OF_NA_ORDER_ON_APPOINTMENT_OF_EG,
                                  FilterFormatConstants.IN_FORMAT_YEAR_MONTH_DAY)
    )
    if exp_date_of_na_order_on_appointment_of_expert_group:
        exp_date_of_na_order_on_appointment_of_expert_group += "T00:00:00"

    exp_number_of_na_order_on_appointment_of_expert_group = input(
        input_filtration_criteria(AccreditationFilterConstants.NUMBER_OF_NA_ORDER_ON_APPOINTMENT_OF_EG)
    )
    exp_departure_start_date = input(
        input_filtration_criteria(AccreditationFilterConstants.DEPARTURE_START_DATE,
                                  FilterFormatConstants.IN_FORMAT_YEAR_MONTH_DAY)
    )
    if exp_departure_start_date:
        exp_departure_start_date += "T00:00:00"
    exp_last_name_of_expert_leader = input(
        input_filtration_criteria(AccreditationFilterConstants.LAST_NAME_OF_EXPERT_LEADER,
                                  FilterFormatConstants.IN_FORMAT_FULL_NAME)
    )
    exp_get_last_name_of_expert = input(
        input_filtration_criteria(AccreditationFilterConstants.LAST_NAME_OF_EXPERT,
                                  FilterFormatConstants.IN_FORMAT_FULL_NAME)
    )
    exp_surname_of_ger_speaker = input(
        input_filtration_criteria(AccreditationFilterConstants.SURNAME_OF_GER_SPEAKER,
                                  FilterFormatConstants.IN_FORMAT_FULL_NAME)
    )

    # EG
    exp_op_compliance_level_criterion_1_according_to_expert_group = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LVL_CRITERION_1_ACC_TO_EG,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_2_according_to_expert_group = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LVL_CRITERION_2_ACC_TO_EG,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_3_according_to_expert_group = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LVL_CRITERION_3_ACC_TO_EG,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_4_according_to_expert_group = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LVL_CRITERION_4_ACC_TO_EG,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_5_according_to_expert_group = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LVL_CRITERION_5_ACC_TO_EG,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_6_according_to_expert_group = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LVL_CRITERION_6_ACC_TO_EG,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_7_according_to_expert_group = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LVL_CRITERION_7_ACC_TO_EG,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_8_according_to_expert_group = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LVL_CRITERION_8_ACC_TO_EG,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_9_according_to_expert_group = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LVL_CRITERION_9_ACC_TO_EG,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )
    exp_op_compliance_level_criterion_10_according_to_expert_group = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LVL_CRITERION_10_ACC_TO_EG,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_EG
        )
    )

    # Compliance level criterion constants for GER
    exp_op_compliance_level_criterion_1_according_to_ger = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LEVEL_CRITERION_1_ACC_TO_GER,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_2_according_to_ger = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LEVEL_CRITERION_2_ACC_TO_GER,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_3_according_to_ger = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LEVEL_CRITERION_3_ACC_TO_GER,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_4_according_to_ger = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LEVEL_CRITERION_4_ACC_TO_GER,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_5_according_to_ger = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LEVEL_CRITERION_5_ACC_TO_GER,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_6_according_to_ger = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LEVEL_CRITERION_6_ACC_TO_GER,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_7_according_to_ger = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LEVEL_CRITERION_7_ACC_TO_GER,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_8_according_to_ger = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LEVEL_CRITERION_8_ACC_TO_GER,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_9_according_to_ger = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LEVEL_CRITERION_9_ACC_TO_GER,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_op_compliance_level_criterion_10_according_to_ger = input(
        input_filtration_criteria(
            AccreditationFilterConstants.OP_COMPL_LEVEL_CRITERION_10_ACC_TO_GER,
            FilterFormatConstants.POSSIBLE_VARIANTS_FOR_COMPLIANCE_LEVEL_CRITERION_BY_GER
        )
    )
    exp_time_na_meeting = input(
        input_filtration_criteria(
            AccreditationFilterConstants.TIME_NA_MEETING,
            FilterFormatConstants.IN_FORMAT_TIME_NA_MEETING
        )
    )
    if exp_time_na_meeting:
        exp_time_na_meeting = exp_time_na_meeting.split()

    input_filtration_values_list = [
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
    return input_filtration_values_list


def map_filter_criteria(input_filtration_values_list: list) -> list[list]:
    """
    Map the accreditation case filter criteria to categories based on input values.

    This function takes a list of input values for filtration functions, and for each function, it maps the
    criteria to one of two categories:
    - 'default_criteria' if the input value is empty (indicating the use of a default criterion).
    - The actual input value if a specific criterion value is provided.

    :return: List of criteria in format [[function, 'default_criteria/current_filtration_value']] like:
    [[<function ResponseParser.get_id_program at 0x1046d1ee0>, 'default_criteria'], ...]
    """
    criteria = []

    # Construct criteria list and headers for csv file
    for i in zip(FILTRATION_FUNCTIONS, input_filtration_values_list, CSV_TABLE_HEADERS):
        current_filtration_function, current_filtration_value, _ = i[0], i[1], i[2]

        if current_filtration_function in DEFAULT_FILTRATION_FUNCTIONS and not current_filtration_value:
            criteria.append([current_filtration_function, "default_criteria"])
        elif current_filtration_value != '':
            criteria.append([current_filtration_function, current_filtration_value])

    logging.debug("Criteria list: %s", criteria)
    return criteria


def prepare_csv_table(input_filtration_values_list: list):
    """
    Prepare and write the CSV table headers for the filtered accreditation cases.

    :param input_filtration_values_list: List of input filtration values
    """
    csv_table_headers = []
    for i in zip(FILTRATION_FUNCTIONS, input_filtration_values_list, CSV_TABLE_HEADERS):
        _, current_filtration_value, current_csv_column_name = i[0], i[1], i[2]

        if current_filtration_value:
            csv_table_headers = update_csv_headers(current_csv_column_name)

    logging.debug("Csv table headers: %s", csv_table_headers)
    build_csv([csv_table_headers])
