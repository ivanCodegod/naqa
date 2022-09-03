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


def get_higher_education_level(response):
    """Рівень вищої освіти"""
    # Из запроса на все аккредитации
    return response["programCycleName"]


def get_knowledge_area(response):
    """Галузь знань"""
    # Из запроса на все аккредитации
    return response["area"]


def get_speciality(response):
    """Спеціальність"""
    # Из запроса на все аккредитации
    return response["specialityName"]


def get_op(response):
    """Назва ОП"""
    # Из запроса на все аккредитации
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
    response["accreditationOrders"][0]["orderDate"]


def get_number_of_na_order_on_appointment_of_expert_group(response):
    """Номер наказу НА про призначення експертної групи"""
    response["accreditationOrders"][0]["orderNumber"]


def get_departure_start_date(response):
    """Дата початку виїзду"""
    response["accreditationOrders"][0]["dateStart"]


def get_last_name_of_expert_leader(response):
    """Прізвище лідера експертної групи"""
    # ФИО лидера
    return response["accreditationOrders"][0]["leaderExpertGroup"]["name"]


def get_last_name_of_expert(response):
    """Прізвище експерта"""
    # Список ФИО экспертов
    return response["accreditationOrders"][0]["experts"]


def get_surname_of_ger_speaker(response):
    """Прізвище доповідача ГЕР"""
    # Тут целое ФИО
    return response["branchSpeaker"]["speaker"]["name"]
