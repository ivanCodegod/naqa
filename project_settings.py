class ProjectSettingsManager:
    # Accreditation related settings
    DEFAULT_KNOWLEDGE_AREA = "04"

    # CSV settings
    CSV_FILE_NAME = 'filtered_accreditation_cases.csv'

    # Requests settings
    RETRY_COUNT = 5
    POOL_MAX_SIZE = 300
    TIMEOUT_COUNT = 15
    BACKOFF_FACTOR = 0.2
