import csv
import os

CSV_FILE_NAME = 'naqa_system_test.csv'


def delete_old_csv():
    """Delete old csv file is exist."""
    if f"{CSV_FILE_NAME}" in os.listdir():
        os.remove(f"{CSV_FILE_NAME}")


def build_csv(row_list):
    """Building csv file that will contain filtered accreditation cases"""
    with open(f"{CSV_FILE_NAME}", 'a', encoding="utf8", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
        writer.writerows(row_list)
