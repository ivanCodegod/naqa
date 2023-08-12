import logging
import sys


class AppInterfaceConstants:
    """
    Constants related to the application interface.

    This class defines command aliases and their associated descriptions, which are used in the application interface
    to provide user feedback and handle user commands.

    Attributes:
        WELCOME_COMMANDS (tuple): Command aliases for the welcome command.
        FILTER_COMMANDS (tuple): Command aliases for the filter command.
        HELP_COMMANDS (tuple): Command aliases for the help command.
        EXIT_COMMANDS (tuple): Command aliases for the exit command.
        COMMAND_DESCRIPTIONS (dict): A dictionary mapping command aliases to their corresponding descriptions.
    """
    # Command aliases
    WELCOME_COMMANDS = ("welcome", "w")
    FILTER_COMMANDS = ("filter", "f")
    HELP_COMMANDS = ("help", "h")
    EXIT_COMMANDS = ("exit", "e")

    # Command descriptions
    COMMAND_DESCRIPTIONS = {
        WELCOME_COMMANDS: "Ласкаво просимо до системи фільтрації акредитаційних справ NAQA!",
        FILTER_COMMANDS: "Початок фільтрації!\n"
                         "Визначте наступні критерії фільтрації. "
                         "Щоб пропустити фільтрацію за параметром необхідно натиснути кнопку \"Enter\":",
        HELP_COMMANDS: "Список доступних команд:\n"
                       '- "filter" (або "f"): Почати фільтрацію\n'
                       '- "help" (або "h)": Отримати список усіх доступних команд\n'
                       '- "exit" (або "e"): Завершити фільтрацію\n\n'
                       'Напишіть команду для виконання. Наприклад "filter"',
        EXIT_COMMANDS: "Exiting program!"
    }


class AppInterface:
    """
    Application interface for the filtering system.

    This class represents the user interface for the filtration system. It handles user input commands,
    displays appropriate messages, and logs user interactions.
    """
    def __init__(self):
        self.constants = AppInterfaceConstants()

    def valid_command(self, command: str):
        """
        Function to check if the user command is valid.
        The command is considered valid when it exists in available commands.

        :param command: The user input command, such as "welcome", "filter", "help", or "exit".
        """
        return any(command in cmd for cmd in self.constants.COMMAND_DESCRIPTIONS)

    def handle_command(self, command: str):
        """
        Represents the user interface for the filtering system.

        This method processes the user's input command and performs appropriate actions based on the command.
        It handles commands such as displaying a welcome message, starting the filtration process, providing help,
        and exiting the program. The method logs messages to provide user feedback.

        :param command: The user input command, such as "welcome", "filter", "help", or "exit".

        :return: None
        :raises SystemExit: If the user enters the "exit" command, the program exits with a message.
        """
        if self.valid_command(command):
            for cmd_aliases, cmd_description in self.constants.COMMAND_DESCRIPTIONS.items():
                if command in cmd_aliases:
                    logging.info(cmd_description)
                    if cmd_aliases == self.constants.EXIT_COMMANDS:
                        sys.exit(cmd_description)
                    break
            else:
                print("")
        else:
            logging.info("Такої команди немає!")
            logging.info(self.constants.COMMAND_DESCRIPTIONS[self.constants.HELP_COMMANDS])
