def get_id_program(response):
    """ID освітньої програми"""
    return response["formSEId"]


def get_request_number(response):
    """Номер акредитаційної справи"""
    return response["requestNumber"]


def get_id_from_edebo(response):
    """ID ОП в ЄДЕБО"""
    return response["accreditationRequest"]["programEdboId"]


def get_higher_education_name(response):
    """Назва закладу вищої освіти (наукової установи), що реалізує ОП"""
    return response["accreditationRequest"]["universityName"]


def get_higher_education_level_from_all(response, index):
    """Рівень вищої освіти"""
    # Из запроса на все аккредитации
    return response["items"][index]["programCycleName"]


def get_knowledge_area_from_all(response, index):
    """Галузь знань"""
    # Из запроса на все аккредитации
    return response["items"][index]["area"]


def get_speciality_from_all(response, index):
    """Спеціальність"""
    # Из запроса на все аккредитации
    return response["items"][index]["specialityName"]


def get_op(response):
    """Назва ОП"""
    return response["accreditationRequest"]["programName"]


def get_results_of_consideration_of_the_eg(response):
    """За результатами розгляду акредитаційної справи ЕГ"""
    pass


def get_results_of_consideration_of_the_ger(response):
    """За результатами розгляду акредитаційної справи ГЕР"""
    pass


def get_results_of_consideration_of_the_na(response):
    """За результатами розгляду акредитаційної справи НА"""
    pass


def get_date_of_na_adoption_on_op_accreditation(response):
    """Дата прийняття НА рішення щодо акредитації ОП"""
    pass


def get_date_of_na_order_on_appointment_of_expert_group(response):
    """Дата наказу НА про призначення експертної групи"""
    return response["accreditationOrders"][0]["orderDate"]


def get_number_of_na_order_on_appointment_of_expert_group(response):
    """Номер наказу НА про призначення експертної групи"""
    return response["accreditationOrders"][0]["orderNumber"]


def get_departure_start_date(response):
    """Дата початку виїзду"""
    return response["accreditationOrders"][0]["dateStart"]


def get_last_name_of_expert_leader(response):
    """Прізвище лідера експертної групи"""
    # ФИО лидера
    return response["accreditationOrders"][0]["leaderExpertGroup"]["name"]


def get_last_name_of_expert(response):
    """Прізвище експерта"""
    # Список ФИО экспертов. Нужно придумать как обходить всех експертов
    return response["accreditationOrders"][0]["experts"]


def get_surname_of_ger_speaker(response):
    """Прізвище доповідача ГЕР"""
    # ФИО спикера
    return response["branchSpeaker"]["speaker"]["name"]


def get_op_compliance_level_criterion_1_according_to_expert_group(response):
    """Рівень відповідності ОП Критерію 1 акредитації, згідно з висновком експертної групи"""
    return response["esAnalysis"]["lvl1"]


def get_op_compliance_level_criterion_2_according_to_expert_group(response):
    """Рівень відповідності ОП Критерію 2 акредитації, згідно з висновком експертної групи"""
    return response["esAnalysis"]["lvl2"]


def get_op_compliance_level_criterion_3_according_to_expert_group(response):
    """Рівень відповідності ОП Критерію 3 акредитації, згідно з висновком експертної групи"""
    return response["esAnalysis"]["lvl3"]


def get_op_compliance_level_criterion_4_according_to_expert_group(response):
    """Рівень відповідності ОП Критерію 4 акредитації, згідно з висновком експертної групи"""
    return response["esAnalysis"]["lvl4"]


def get_op_compliance_level_criterion_5_according_to_expert_group(response):
    """Рівень відповідності ОП Критерію 5 акредитації, згідно з висновком експертної групи"""
    return response["esAnalysis"]["lvl5"]


def get_op_compliance_level_criterion_6_according_to_expert_group(response):
    """Рівень відповідності ОП Критерію 6 акредитації, згідно з висновком експертної групи"""
    return response["esAnalysis"]["lvl6"]


def get_op_compliance_level_criterion_7_according_to_expert_group(response):
    """Рівень відповідності ОП Критерію 7 акредитації, згідно з висновком експертної групи"""
    return response["esAnalysis"]["lvl7"]


def get_op_compliance_level_criterion_8_according_to_expert_group(response):
    """Рівень відповідності ОП Критерію 8 акредитації, згідно з висновком експертної групи"""
    return response["esAnalysis"]["lvl8"]


def get_op_compliance_level_criterion_9_according_to_expert_group(response):
    """Рівень відповідності ОП Критерію 9 акредитації, згідно з висновком експертної групи"""
    return response["esAnalysis"]["lvl9"]


def get_op_compliance_level_criterion_10_according_to_expert_group(response):
    """Рівень відповідності ОП Критерію 10 акредитації, згідно з висновком експертної групи"""
    return response["esAnalysis"]["lvl10"]


def get_op_compliance_level_criterion_1_according_to_ger(response):
    """Рівень відповідності ОП Критерію 1 акредитації, згідно з висновком ГЕР"""
    return response["besResultEvaluation"]["besLvl1"]


def get_op_compliance_level_criterion_2_according_to_ger(response):
    """Рівень відповідності ОП Критерію 2 акредитації, згідно з висновком ГЕР"""
    return response["besResultEvaluation"]["besLvl2"]


def get_op_compliance_level_criterion_3_according_to_ger(response):
    """Рівень відповідності ОП Критерію 3 акредитації, згідно з висновком ГЕР"""
    return response["besResultEvaluation"]["besLvl3"]


def get_op_compliance_level_criterion_4_according_to_ger(response):
    """Рівень відповідності ОП Критерію 4 акредитації, згідно з висновком ГЕР"""
    return response["besResultEvaluation"]["besLvl4"]


def get_op_compliance_level_criterion_5_according_to_ger(response):
    """Рівень відповідності ОП Критерію 5 акредитації, згідно з висновком ГЕР"""
    return response["besResultEvaluation"]["besLvl5"]


def get_op_compliance_level_criterion_6_according_to_ger(response):
    """Рівень відповідності ОП Критерію 6 акредитації, згідно з висновком ГЕР"""
    return response["besResultEvaluation"]["besLvl6"]


def get_op_compliance_level_criterion_7_according_to_ger(response):
    """Рівень відповідності ОП Критерію 7 акредитації, згідно з висновком ГЕР"""
    return response["besResultEvaluation"]["besLvl7"]


def get_op_compliance_level_criterion_8_according_to_ger(response):
    """Рівень відповідності ОП Критерію 8 акредитації, згідно з висновком ГЕР"""
    return response["besResultEvaluation"]["besLvl8"]


def get_op_compliance_level_criterion_9_according_to_ger(response):
    """Рівень відповідності ОП Критерію 9 акредитації, згідно з висновком ГЕР"""
    return response["besResultEvaluation"]["besLvl9"]


def get_op_compliance_level_criterion_10_according_to_ger(response):
    """Рівень відповідності ОП Критерію 10 акредитації, згідно з висновком ГЕР"""
    return response["besResultEvaluation"]["besLvl10"]


def get_time_na_meeting(response):
    """
    Дата засідання НА.
    Часові межі
    """
    # TODO: Add logic to track the boarders for meeting: from-to.
    return response["naqaAppointmentMeeting"]["meetingDate"]
