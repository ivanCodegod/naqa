import csv
import logging
import os

from accreditation_filter_constants import DEFAULT_CSV_TABLE_HEADERS

from project_settings import ProjectSettingsManager

OUTPUT_DIR = 'output_filtered_data'


def delete_old_csv():
    """Delete old csv file if it exists."""
    csv_file_path = os.path.join(OUTPUT_DIR, ProjectSettingsManager.CSV_FILE_NAME)

    # Check if the CSV file exists in the output directory
    if os.path.exists(csv_file_path):
        # Remove the old CSV file
        os.remove(csv_file_path)
        logging.debug(f"Old CSV file {ProjectSettingsManager.CSV_FILE_NAME} deleted.")
    else:
        logging.debug("Old CSV file not found, no need to delete.")


def build_csv(row_list: list):
    """Building csv file that will contain filtered accreditation cases"""
    with open(f"{OUTPUT_DIR}/{ProjectSettingsManager.CSV_FILE_NAME}", 'a', encoding="utf8",
              newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
        writer.writerows(row_list)


def update_csv_headers(header: str) -> list:
    """
    Update scv table headers. Set up default headers if no headers
     is passed to function or update scv table with passed headers
     """
    default_headers = DEFAULT_CSV_TABLE_HEADERS
    if header not in default_headers:
        DEFAULT_CSV_TABLE_HEADERS.append(header)

    return DEFAULT_CSV_TABLE_HEADERS
