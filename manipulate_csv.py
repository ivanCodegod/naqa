import csv
import os

from accreditation_filter_constants import DEFAULT_CSV_TABLE_HEADERS

from project_settings import ProjectSettingsManager


def delete_old_csv():
    """Delete old csv file is exist."""
    if f"{ProjectSettingsManager.CSV_FILE_NAME}" in os.listdir():
        os.remove(f"{ProjectSettingsManager.CSV_FILE_NAME}")


def build_csv(row_list: list):
    """Building csv file that will contain filtered accreditation cases"""
    with open(f"{ProjectSettingsManager.CSV_FILE_NAME}", 'a', encoding="utf8", newline='') as file:
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
