from filter_params import \
    get_id_program, \
    get_request_number, \
    get_id_from_edebo, \
    get_higher_education_name, \
    get_higher_education_level_from_all, \
    get_knowledge_area_from_all, \
    get_speciality_from_all, \
    get_op, \
    get_results_of_consideration_of_the_eg, \
    get_results_of_consideration_of_the_ger, \
    get_results_of_consideration_of_the_na, \
    get_date_of_na_adoption_on_op_accreditation, \
    get_date_of_na_order_on_appointment_of_expert_group, \
    get_number_of_na_order_on_appointment_of_expert_group, \
    get_departure_start_date, \
    get_last_name_of_expert_leader, \
    get_last_name_of_expert, \
    get_surname_of_ger_speaker, \
    get_op_compliance_level_criterion_1_according_to_expert_group, \
    get_op_compliance_level_criterion_2_according_to_expert_group, \
    get_op_compliance_level_criterion_3_according_to_expert_group, \
    get_op_compliance_level_criterion_4_according_to_expert_group, \
    get_op_compliance_level_criterion_5_according_to_expert_group, \
    get_op_compliance_level_criterion_6_according_to_expert_group, \
    get_op_compliance_level_criterion_7_according_to_expert_group, \
    get_op_compliance_level_criterion_8_according_to_expert_group, \
    get_op_compliance_level_criterion_9_according_to_expert_group, \
    get_op_compliance_level_criterion_10_according_to_expert_group, \
    get_op_compliance_level_criterion_1_according_to_ger, \
    get_op_compliance_level_criterion_2_according_to_ger, \
    get_op_compliance_level_criterion_3_according_to_ger, \
    get_op_compliance_level_criterion_4_according_to_ger, \
    get_op_compliance_level_criterion_5_according_to_ger, \
    get_op_compliance_level_criterion_6_according_to_ger, \
    get_op_compliance_level_criterion_7_according_to_ger, \
    get_op_compliance_level_criterion_8_according_to_ger, \
    get_op_compliance_level_criterion_9_according_to_ger, \
    get_op_compliance_level_criterion_10_according_to_ger, \
    get_time_na_meeting

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
DATE_OF_NA_ADOPTION_ON_OP_ACCREDITATION = "Дата прийняття НА рішення щодо акредитації ОП"
DATE_OF_NA_ORDER_ON_APPOINTMENT_OF_EG = "Дата наказу НА про призначення експертної групи"
NUMBER_OF_NA_ORDER_ON_APPOINTMENT_OF_EG = "Номер наказу НА про призначення експертної групи"
DEPARTURE_START_DATE = "Дата початку виїзду"
LAST_NAME_OF_EXPERT_LEADER = "Прізвище лідера експертної групи"
LAST_NAME_OF_EXPERT = "Прізвище експерта"
SURNAME_OF_GER_SPEAKER = "Прізвище доповідача ГЕР"

# Compliance level criterion constants for EG
OP_COMPL_LVL_CRITERION_1_ACC_TO_EG = \
    "Рівень відповідності ОП Критерію 1 акредитації, згідно з висновком експертної групи"
OP_COMPL_LVL_CRITERION_2_ACC_TO_EG = \
    "Рівень відповідності ОП Критерію 2 акредитації, згідно з висновком експертної групи"
OP_COMPL_LVL_CRITERION_3_ACC_TO_EG = \
    "Рівень відповідності ОП Критерію 3 акредитації, згідно з висновком експертної групи"
OP_COMPL_LVL_CRITERION_4_ACC_TO_EG = \
    "Рівень відповідності ОП Критерію 4 акредитації, згідно з висновком експертної групи"
OP_COMPL_LVL_CRITERION_5_ACC_TO_EG = \
    "Рівень відповідності ОП Критерію 5 акредитації, згідно з висновком експертної групи"
OP_COMPL_LVL_CRITERION_6_ACC_TO_EG = \
    "Рівень відповідності ОП Критерію 6 акредитації, згідно з висновком експертної групи"
OP_COMPL_LVL_CRITERION_7_ACC_TO_EG = \
    "Рівень відповідності ОП Критерію 7 акредитації, згідно з висновком експертної групи"
OP_COMPL_LVL_CRITERION_8_ACC_TO_EG = \
    "Рівень відповідності ОП Критерію 8 акредитації, згідно з висновком експертної групи"
OP_COMPL_LVL_CRITERION_9_ACC_TO_EG = \
    "Рівень відповідності ОП Критерію 9 акредитації, згідно з висновком експертної групи"
OP_COMPL_LVL_CRITERION_10_ACC_TO_EG = \
    "Рівень відповідності ОП Критерію 10 акредитації, згідно з висновком експертної групи"

# COMPL level criterion constants for GER
OP_COMPL_LEVEL_CRITERION_1_ACC_TO_GER = \
    "Рівень відповідності ОП Критерію 1 акредитації, згідно з висновком ГЕР"
OP_COMPL_LEVEL_CRITERION_2_ACC_TO_GER = \
    "Рівень відповідності ОП Критерію 2 акредитації, згідно з висновком ГЕР"
OP_COMPL_LEVEL_CRITERION_3_ACC_TO_GER = \
    "Рівень відповідності ОП Критерію 3 акредитації, згідно з висновком ГЕР"
OP_COMPL_LEVEL_CRITERION_4_ACC_TO_GER = \
    "Рівень відповідності ОП Критерію 4 акредитації, згідно з висновком ГЕР"
OP_COMPL_LEVEL_CRITERION_5_ACC_TO_GER = \
    "Рівень відповідності ОП Критерію 5 акредитації, згідно з висновком ГЕР"
OP_COMPL_LEVEL_CRITERION_6_ACC_TO_GER = \
    "Рівень відповідності ОП Критерію 6 акредитації, згідно з висновком ГЕР"
OP_COMPL_LEVEL_CRITERION_7_ACC_TO_GER = \
    "Рівень відповідності ОП Критерію 7 акредитації, згідно з висновком ГЕР"
OP_COMPL_LEVEL_CRITERION_8_ACC_TO_GER = \
    "Рівень відповідності ОП Критерію 8 акредитації, згідно з висновком ГЕР"
OP_COMPL_LEVEL_CRITERION_9_ACC_TO_GER = \
    "Рівень відповідності ОП Критерію 9 акредитації, згідно з висновком ГЕР"
OP_COMPL_LEVEL_CRITERION_10_ACC_TO_GER = \
    "Рівень відповідності ОП Критерію 10 акредитації, згідно з висновком ГЕР"

DEFAULT_CSV_TABLE_HEADERS = [
    ID_PROGRAM,
    AC_NUMBER,
    ID_EDEBO,
    HIGHER_EDUCATION_NAME,
    HIGHER_EDUCATION_LEVEL,
    KNOWLEDGE_AREA,
    SPECIALITY,
    OP_NAME
]

DEFAULT_FILTRATION_CRITERIA = [
    get_id_program,
    get_request_number,
    get_id_from_edebo,
    get_higher_education_name,
    get_higher_education_level_from_all,
    get_knowledge_area_from_all,
    get_speciality_from_all,
    get_op
]

INPUT_CRITERIA_FUNCTION_LIST = [
    get_id_program,
    get_request_number,
    get_id_from_edebo,
    get_higher_education_name,
    get_higher_education_level_from_all,
    get_knowledge_area_from_all,
    get_speciality_from_all,
    get_op,
    get_results_of_consideration_of_the_eg,
    get_results_of_consideration_of_the_ger,
    get_results_of_consideration_of_the_na,
    get_date_of_na_adoption_on_op_accreditation,
    get_date_of_na_order_on_appointment_of_expert_group,
    get_number_of_na_order_on_appointment_of_expert_group,
    get_departure_start_date,
    get_last_name_of_expert_leader,
    get_last_name_of_expert,
    get_surname_of_ger_speaker,
    get_op_compliance_level_criterion_1_according_to_expert_group,
    get_op_compliance_level_criterion_2_according_to_expert_group,
    get_op_compliance_level_criterion_3_according_to_expert_group,
    get_op_compliance_level_criterion_4_according_to_expert_group,
    get_op_compliance_level_criterion_5_according_to_expert_group,
    get_op_compliance_level_criterion_6_according_to_expert_group,
    get_op_compliance_level_criterion_7_according_to_expert_group,
    get_op_compliance_level_criterion_8_according_to_expert_group,
    get_op_compliance_level_criterion_9_according_to_expert_group,
    get_op_compliance_level_criterion_10_according_to_expert_group,
    get_op_compliance_level_criterion_1_according_to_ger,
    get_op_compliance_level_criterion_2_according_to_ger,
    get_op_compliance_level_criterion_3_according_to_ger,
    get_op_compliance_level_criterion_4_according_to_ger,
    get_op_compliance_level_criterion_5_according_to_ger,
    get_op_compliance_level_criterion_6_according_to_ger,
    get_op_compliance_level_criterion_7_according_to_ger,
    get_op_compliance_level_criterion_8_according_to_ger,
    get_op_compliance_level_criterion_9_according_to_ger,
    get_op_compliance_level_criterion_10_according_to_ger
]

CSV_COLUMN_NAME_LIST = [
    ID_PROGRAM,
    AC_NUMBER,
    ID_EDEBO,
    HIGHER_EDUCATION_NAME,
    HIGHER_EDUCATION_LEVEL,
    KNOWLEDGE_AREA,
    SPECIALITY,
    OP_NAME,
    RESULTS_OD_CONSIDERATION_OF_THE_EG,
    RESULTS_OD_CONSIDERATION_OF_THE_GER,
    RESULTS_OD_CONSIDERATION_OF_THE_NA,
    DATE_OF_NA_ADOPTION_ON_OP_ACCREDITATION,
    DATE_OF_NA_ORDER_ON_APPOINTMENT_OF_EG,
    NUMBER_OF_NA_ORDER_ON_APPOINTMENT_OF_EG,
    DEPARTURE_START_DATE,
    LAST_NAME_OF_EXPERT_LEADER,
    LAST_NAME_OF_EXPERT,
    SURNAME_OF_GER_SPEAKER,
    OP_COMPL_LVL_CRITERION_1_ACC_TO_EG,
    OP_COMPL_LVL_CRITERION_2_ACC_TO_EG,
    OP_COMPL_LVL_CRITERION_3_ACC_TO_EG,
    OP_COMPL_LVL_CRITERION_4_ACC_TO_EG,
    OP_COMPL_LVL_CRITERION_5_ACC_TO_EG,
    OP_COMPL_LVL_CRITERION_6_ACC_TO_EG,
    OP_COMPL_LVL_CRITERION_7_ACC_TO_EG,
    OP_COMPL_LVL_CRITERION_8_ACC_TO_EG,
    OP_COMPL_LVL_CRITERION_9_ACC_TO_EG,
    OP_COMPL_LVL_CRITERION_10_ACC_TO_EG,
    OP_COMPL_LEVEL_CRITERION_1_ACC_TO_GER,
    OP_COMPL_LEVEL_CRITERION_2_ACC_TO_GER,
    OP_COMPL_LEVEL_CRITERION_3_ACC_TO_GER,
    OP_COMPL_LEVEL_CRITERION_4_ACC_TO_GER,
    OP_COMPL_LEVEL_CRITERION_5_ACC_TO_GER,
    OP_COMPL_LEVEL_CRITERION_6_ACC_TO_GER,
    OP_COMPL_LEVEL_CRITERION_7_ACC_TO_GER,
    OP_COMPL_LEVEL_CRITERION_8_ACC_TO_GER,
    OP_COMPL_LEVEL_CRITERION_9_ACC_TO_GER,
    OP_COMPL_LEVEL_CRITERION_10_ACC_TO_GER
]
