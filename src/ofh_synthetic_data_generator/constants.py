import os
from datetime import date
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

HEALTH_DATA_DICTIONARY_PATH = (
    Path(__file__).parent / "resources" / "health_data_dictionary"
)
HEALTH_CODINGS_DB_PATH = Path(__file__).parent / "resources" / "health_codings.db"

SEED = int(os.getenv("SEED", "0"))

STUDY_START_DATE = date(2015, 1, 1)
STUDY_END_DATE = date(2025, 12, 31)

MINIMUM_AGE_YEARS = 18

MIN_HEIGHT_CM = 90
MAX_HEIGHT_CM = 299

MIN_WEIGHT_KG = 20
MAX_WEIGHT_KG = 400
