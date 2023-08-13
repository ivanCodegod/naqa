class ResponseParser:
    """
    Class for parsing response JSON objects from accreditation requests.

    This class provides methods to extract specific information from the JSON response.
    """

    @staticmethod
    def get_id_program(response: dict):
        """ID освітньої програми"""
        return response["formSEId"]

    @staticmethod
    def get_request_number(response: dict):
        """Номер акредитаційної справи"""
        return response["requestNumber"]

    @staticmethod
    def get_id_from_edebo(response: dict):
        """ID ОП в ЄДЕБО"""
        return response["accreditationRequest"]["programEdboId"]

    @staticmethod
    def get_higher_education_name(response: dict):
        """Назва закладу вищої освіти (наукової установи), що реалізує ОП"""
        return response["accreditationRequest"]["universityName"]

    @staticmethod
    def get_higher_education_level_from_all(response: dict, index: int):
        """Рівень вищої освіти"""
        # Із запиту на всі акредитації
        return response["items"][index]["programCycleName"]

    @staticmethod
    def get_knowledge_area_from_all(response: dict, index: int):
        """Галузь знань"""
        # Із запиту на всі акредитації
        return response["items"][index]["area"]

    @staticmethod
    def get_speciality_from_all(response: dict, index: int):
        """Спеціальність"""
        # Із запиту на всі акредитації
        return response["items"][index]["specialityName"]

    @staticmethod
    def get_op(response: dict):
        """Назва ОП"""
        return response["accreditationRequest"]["programName"]

    @staticmethod
    def get_results_of_consideration_of_the_eg(response: dict):
        """За результатами розгляду акредитаційної справи ЕГ"""
        result = response["esResults"]["expertGroupDecision"]

        if result == 1:
            result = 'Акредитація з визначенням "зразкова"'
        elif result == 2:
            result = 'Умовна'
        elif result == 3:
            result = 'Відмова в акредитації'
        elif result == 4:
            result = 'Призначення повторної акредитаційної експертизи'
        elif result == 5:
            result = 'Акредитація'

        return result

    @staticmethod
    def get_results_of_consideration_of_the_ger(response: dict):
        """За результатами розгляду акредитаційної справи ГЕР"""
        result = response["besReport"]["accreditationDecision"]

        if result == 1:
            result = 'Акредитація з визначенням "зразкова"'
        elif result == 2:
            result = 'Умовна'
        elif result == 3:
            result = 'Відмова в акредитації'
        elif result == 4:
            result = 'Призначення повторної акредитаційної експертизи'
        elif result == 5:
            result = 'Акредитація'

        return result

    @staticmethod
    def get_results_of_consideration_of_the_na(response: dict):
        """За результатами розгляду акредитаційної справи НА"""
        result = response["naqaDecision"]["decision"]

        if result == 1:
            result = 'Акредитувати освітню програму з визначенням "зразкова"'
        elif result == 2:
            result = 'Акредитувати освітню програму умовно (відкладено)'
        elif result == 3:
            result = 'Відмовити в акредитації освітньої програми'
        elif result == 4:
            result = 'Акредитувати освітню програму'
        elif result == 6:
            result = "Відмовити в акредитації освітньої програми з підстав, не пов'язаних" \
                     " з відповідністю Критеріям оцінювання якості освітньої програми."
        elif result == 7:
            result = "Призначити повторну акредитаційну експертизу"
        elif result == 8:
            result = "Повернути справу до галузевої експертної ради для повторного розгляду"

        return result

    @staticmethod
    def get_date_of_na_adoption_on_op_accreditation(response: dict):
        """Дата прийняття НА рішення щодо акредитації ОП"""
        return response["naqaAppointmentMeeting"]["meetingDate"]

    @staticmethod
    def get_date_of_na_order_on_appointment_of_expert_group(response: dict):
        """Дата наказу НА про призначення експертної групи"""
        return response["accreditationOrders"][0]["orderDate"]

    @staticmethod
    def get_number_of_na_order_on_appointment_of_expert_group(response: dict):
        """Номер наказу НА про призначення експертної групи"""
        return response["accreditationOrders"][0]["orderNumber"]

    @staticmethod
    def get_departure_start_date(response: dict):
        """Дата початку виїзду"""
        return response["accreditationOrders"][0]["dateStart"]

    @staticmethod
    def get_last_name_of_expert_leader(response: dict):
        """Прізвище керівника експертної групи"""
        return response["accreditationOrders"][0]["leaderExpertGroup"]["name"]

    @staticmethod
    def get_last_name_of_expert(response: dict):
        """Прізвище експерта"""
        experts_list = []
        for expert in response["accreditationOrders"][0]["experts"]:
            experts_list.append(expert["name"])

        return experts_list

    @staticmethod
    def get_surname_of_ger_speaker(response: dict):
        """Прізвище доповідача ГЕР"""
        return response["branchSpeaker"]["speaker"]["name"]

    @staticmethod
    def get_op_compliance_level_criterion_1_according_to_expert_group(response: dict):
        """Рівень відповідності ОП Критерію 1 акредитації, згідно з висновком експертної групи"""
        return response["esAnalysis"]["lvl1"]

    @staticmethod
    def get_op_compliance_level_criterion_2_according_to_expert_group(response: dict):
        """Рівень відповідності ОП Критерію 2 акредитації, згідно з висновком експертної групи"""
        return response["esAnalysis"]["lvl2"]

    @staticmethod
    def get_op_compliance_level_criterion_3_according_to_expert_group(response: dict):
        """Рівень відповідності ОП Критерію 3 акредитації, згідно з висновком експертної групи"""
        return response["esAnalysis"]["lvl3"]

    @staticmethod
    def get_op_compliance_level_criterion_4_according_to_expert_group(response: dict):
        """Рівень відповідності ОП Критерію 4 акредитації, згідно з висновком експертної групи"""
        return response["esAnalysis"]["lvl4"]

    @staticmethod
    def get_op_compliance_level_criterion_5_according_to_expert_group(response: dict):
        """Рівень відповідності ОП Критерію 5 акредитації, згідно з висновком експертної групи"""
        return response["esAnalysis"]["lvl5"]

    @staticmethod
    def get_op_compliance_level_criterion_6_according_to_expert_group(response: dict):
        """Рівень відповідності ОП Критерію 6 акредитації, згідно з висновком експертної групи"""
        return response["esAnalysis"]["lvl6"]

    @staticmethod
    def get_op_compliance_level_criterion_7_according_to_expert_group(response: dict):
        """Рівень відповідності ОП Критерію 7 акредитації, згідно з висновком експертної групи"""
        return response["esAnalysis"]["lvl7"]

    @staticmethod
    def get_op_compliance_level_criterion_8_according_to_expert_group(response: dict):
        """Рівень відповідності ОП Критерію 8 акредитації, згідно з висновком експертної групи"""
        return response["esAnalysis"]["lvl8"]

    @staticmethod
    def get_op_compliance_level_criterion_9_according_to_expert_group(response: dict):
        """Рівень відповідності ОП Критерію 9 акредитації, згідно з висновком експертної групи"""
        return response["esAnalysis"]["lvl9"]

    @staticmethod
    def get_op_compliance_level_criterion_10_according_to_expert_group(response: dict):
        """Рівень відповідності ОП Критерію 10 акредитації, згідно з висновком експертної групи"""
        return response["esAnalysis"]["lvl10"]

    @staticmethod
    def get_op_compliance_level_criterion_1_according_to_ger(response: dict):
        """Рівень відповідності ОП Критерію 1 акредитації, згідно з висновком ГЕР"""
        return response["besResultEvaluation"]["besLvl1"]

    @staticmethod
    def get_op_compliance_level_criterion_2_according_to_ger(response: dict):
        """Рівень відповідності ОП Критерію 2 акредитації, згідно з висновком ГЕР"""
        return response["besResultEvaluation"]["besLvl2"]

    @staticmethod
    def get_op_compliance_level_criterion_3_according_to_ger(response: dict):
        """Рівень відповідності ОП Критерію 3 акредитації, згідно з висновком ГЕР"""
        return response["besResultEvaluation"]["besLvl3"]

    @staticmethod
    def get_op_compliance_level_criterion_4_according_to_ger(response: dict):
        """Рівень відповідності ОП Критерію 4 акредитації, згідно з висновком ГЕР"""
        return response["besResultEvaluation"]["besLvl4"]

    @staticmethod
    def get_op_compliance_level_criterion_5_according_to_ger(response: dict):
        """Рівень відповідності ОП Критерію 5 акредитації, згідно з висновком ГЕР"""
        return response["besResultEvaluation"]["besLvl5"]

    @staticmethod
    def get_op_compliance_level_criterion_6_according_to_ger(response: dict):
        """Рівень відповідності ОП Критерію 6 акредитації, згідно з висновком ГЕР"""
        return response["besResultEvaluation"]["besLvl6"]

    @staticmethod
    def get_op_compliance_level_criterion_7_according_to_ger(response: dict):
        """Рівень відповідності ОП Критерію 7 акредитації, згідно з висновком ГЕР"""
        return response["besResultEvaluation"]["besLvl7"]

    @staticmethod
    def get_op_compliance_level_criterion_8_according_to_ger(response: dict):
        """Рівень відповідності ОП Критерію 8 акредитації, згідно з висновком ГЕР"""
        return response["besResultEvaluation"]["besLvl8"]

    @staticmethod
    def get_op_compliance_level_criterion_9_according_to_ger(response: dict):
        """Рівень відповідності ОП Критерію 9 акредитації, згідно з висновком ГЕР"""
        return response["besResultEvaluation"]["besLvl9"]

    @staticmethod
    def get_op_compliance_level_criterion_10_according_to_ger(response: dict):
        """Рівень відповідності ОП Критерію 10 акредитації, згідно з висновком ГЕР"""
        return response["besResultEvaluation"]["besLvl10"]

    @staticmethod
    def get_time_na_meeting(response: dict):
        """
        Дата засідання НА.
        Часові межі
        """
        return response["naqaAppointmentMeeting"]["meetingDate"]