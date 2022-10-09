import logging
import sys

AVAILABLE_COMMANDS_INFO = \
    'Список доступних команд:\n' \
    '- "filter" або "f": Почати фільтрацію\n' \
    '- "help" або "h": Отримати список усіх доступних команд\n' \
    '- "exit" або "e": Завершити фільтрацію\n\n' \
    'Напишіть команду для виконання. Наприклад "filter"'

AVAILABLE_COMMANDS = [
    ("welcome", "w"),
    ("filter", "f"),
    ("help", "h"),
    ("exit", "e"),
    ("no_such_command",),
]


def valid_command(command):
    """
    Function to check if the user command in valid.
    The command in considered as valid when command exist in available commands.
    """
    return any(
        [command in AVAILABLE_COMMANDS[ind] for ind, current_command in enumerate(AVAILABLE_COMMANDS)]
    ) or False


def user_interface(command):
    """
    Function that represent the interface.
    Makes logging depends on user input command.
    """

    if valid_command(command):
        if command in ("welcome", "w"):
            logging.info("Ласкаво просимо до системи фільтрації акредитаційних справ NAQA!")
            logging.info(AVAILABLE_COMMANDS_INFO)
        elif command in ("filter", "f"):
            logging.info("Початок фільтрації!")
            logging.info(
                'Визначте наступні критерії фільтрації.'
                'Щоб пропустити фільтрацію за параметром необхідно натиснути кнопку "Enter":')
        elif command in ("help", "h"):
            logging.info(AVAILABLE_COMMANDS_INFO)
        elif command in ("exit", "e"):
            sys.exit("Exiting program!")
    else:
        logging.info("Такої команди немає!")
        logging.info(AVAILABLE_COMMANDS_INFO)
