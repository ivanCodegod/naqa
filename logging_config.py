import os
import logging
from datetime import datetime


def configure_logging():
    # Specify the log directory
    log_directory = "logs"

    # Create the log directory if it doesn't exist
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Specify the log file path within the log directory
    log_file_path = os.path.join(log_directory, f'log_{timestamp}.log')

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler(log_file_path),  # Create a new log file
            logging.StreamHandler()
        ]
    )
    logging.debug(f"Logging file {log_file_path} was initialized")
