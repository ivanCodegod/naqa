import os
import logging
from datetime import datetime


class LoggingConfigurator:
    LOG_DIRECTORY = "logs"

    def __init__(self, log_directory=LOG_DIRECTORY):
        self.log_directory = log_directory
        self._configure_logging()

    def _configure_logging(self):
        # Create the log directory if it doesn't exist
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Specify the log file path within the log directory
        log_file_path = os.path.join(self.log_directory, f'log_{timestamp}.log')

        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s [%(levelname)s] %(message)s',
            handlers=[
                logging.FileHandler(log_file_path),  # Create a new log file
                logging.StreamHandler()
            ]
        )
        logging.debug(f"Logging file {log_file_path} was initialized")
