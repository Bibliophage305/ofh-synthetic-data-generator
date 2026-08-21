from dataclasses import dataclass
from datetime import datetime

from dataclass_type_validator import dataclass_validate
from faker import Faker

from ofh_synthetic_data_generator.constants import (
    MAX_HEIGHT_CM,
    MAX_WEIGHT_KG,
    MIN_HEIGHT_CM,
    MIN_WEIGHT_KG,
    STUDY_END_DATE,
)

from .helpers import generate_code, generate_id

# TODO: what are these versions? Should they affect the fields that are present?
APPOINTMENT_VERSIONS = ["v1", "v2", "v3"]

# TODO: what are sensible min/max values for waist?
MIN_WAIST_CM = 50
MAX_WAIST_CM = 150

# TODO: what are sensible min/max values for heart rate and blood pressure?
MIN_HEART_RATE = 50
MAX_HEART_RATE = 100
MIN_BP_SYSTOLIC = 90
MAX_BP_SYSTOLIC = 140
MIN_BP_DIASTOLIC = 60
MAX_BP_DIASTOLIC = 90


@dataclass_validate
@dataclass
class ClinicMeasurements:
    ID: str
    PID: str
    APPOINTMENT_VERSION: str
    APPOINTMENT_DATETIME: datetime
    HEIGHT: int | None
    WEIGHT: float | None
    WAIST: int | None
    HEART_FIRST_RATE: int | None
    HEART_FIRST_BP_SYSTOLIC: int | None
    HEART_FIRST_BP_DIASTOLIC: int | None
    HEART_SECOND_RATE: int | None
    HEART_SECOND_BP_SYSTOLIC: int | None
    HEART_SECOND_BP_DIASTOLIC: int | None
    HEART_THIRD_RATE: int | None
    HEART_THIRD_BP_SYSTOLIC: int | None
    HEART_THIRD_BP_DIASTOLIC: int | None
    HEIGHT_SKIPPED: int
    WEIGHT_SKIPPED: int
    WAIST_SKIPPED: int
    HEART_FIRST_SKIPPED: int
    HEART_SECOND_SKIPPED: int
    HEART_THIRD_SKIPPED: int
    HEIGHT_SKIPPED_REASON: int | None
    WEIGHT_SKIPPED_REASON: int | None
    WAIST_SKIPPED_REASON: int | None
    HEART_FIRST_RHYTHM: int | None
    HEART_SECOND_RHYTHM: int | None
    HEART_THIRD_RHYTHM: int | None
    HEART_FIRST_SKIPPED_REASON: int | None
    HEART_SECOND_SKIPPED_REASON: int | None
    HEART_THIRD_SKIPPED_REASON: int | None
    CLINIC_SITE_REF: str
    CLINIC_PROVIDER: str
    IS_MOBILE_CLINIC: int


class ClinicMeasurementsFactory:
    def __init__(self, fake: Faker):
        self.fake = fake

    def generate(self, PID, registration_date):
        ID = generate_id(self.fake)
        APPOINTMENT_VERSION = self.fake.random_element(APPOINTMENT_VERSIONS)
        APPOINTMENT_DATETIME = datetime.fromordinal(
            self.fake.date_between(
                start_date=registration_date, end_date=STUDY_END_DATE
            ).toordinal()
        )

        HEIGHT_SKIPPED = generate_code(
            self.fake, "HEIGHT_SKIPPED", enforce_numeric_codes=True
        )

        # TODO: how are skipped measurements represented? Are they null, or are they 0, or something else?
        HEIGHT = None
        # TODO: how is this represented if the measurement is not skipped? Is it null, or 0, or something else?
        HEIGHT_SKIPPED_REASON = None
        if HEIGHT_SKIPPED == 0:
            HEIGHT = self.fake.random_int(MIN_HEIGHT_CM, MAX_HEIGHT_CM)
        elif HEIGHT_SKIPPED == 1:
            HEIGHT_SKIPPED_REASON = generate_code(
                self.fake, "HEIGHT_SKIPPED_REASON", enforce_numeric_codes=True
            )

        WEIGHT_SKIPPED = generate_code(
            self.fake, "WEIGHT_SKIPPED", enforce_numeric_codes=True
        )

        WEIGHT = None
        WEIGHT_SKIPPED_REASON = None
        if WEIGHT_SKIPPED == 0:
            WEIGHT = self.fake.pyfloat(
                min_value=MIN_WEIGHT_KG, max_value=MAX_WEIGHT_KG, right_digits=1
            )
        elif WEIGHT_SKIPPED == 1:
            WEIGHT_SKIPPED_REASON = generate_code(
                self.fake, "WEIGHT_SKIPPED_REASON", enforce_numeric_codes=True
            )

        WAIST_SKIPPED = generate_code(
            self.fake, "WAIST_SKIPPED", enforce_numeric_codes=True
        )

        WAIST = None
        WAIST_SKIPPED_REASON = None
        if WAIST_SKIPPED == 0:
            WAIST = self.fake.random_int(MIN_WAIST_CM, MAX_WAIST_CM)
        elif WAIST_SKIPPED == 1:
            WAIST_SKIPPED_REASON = generate_code(
                self.fake, "WAIST_SKIPPED_REASON", enforce_numeric_codes=True
            )

        HEART_FIRST_SKIPPED = generate_code(
            self.fake, "HEART_FIRST_SKIPPED", enforce_numeric_codes=True
        )

        HEART_FIRST_RATE = None
        HEART_FIRST_BP_SYSTOLIC = None
        HEART_FIRST_BP_DIASTOLIC = None
        HEART_FIRST_RHYTHM = None
        HEART_FIRST_SKIPPED_REASON = None
        if HEART_FIRST_SKIPPED == 0:
            # TODO: what are sensible min/max values for heart rate and blood pressure?
            HEART_FIRST_RATE = self.fake.random_int(MIN_HEART_RATE, MAX_HEART_RATE)
            HEART_FIRST_BP_SYSTOLIC = self.fake.random_int(
                MIN_BP_SYSTOLIC, MAX_BP_SYSTOLIC
            )
            HEART_FIRST_BP_DIASTOLIC = self.fake.random_int(
                MIN_BP_DIASTOLIC, MAX_BP_DIASTOLIC
            )
            HEART_FIRST_RHYTHM = generate_code(
                self.fake, "HEART_FIRST_RHYTHM", enforce_numeric_codes=True
            )
        elif HEART_FIRST_SKIPPED == 1:
            HEART_FIRST_SKIPPED_REASON = generate_code(
                self.fake, "HEART_FIRST_SKIPPED_REASON", enforce_numeric_codes=True
            )

        # TODO: is it possible for the first heart measurement to be skipped but the second to be present?
        HEART_SECOND_SKIPPED = generate_code(
            self.fake, "HEART_SECOND_SKIPPED", enforce_numeric_codes=True
        )

        HEART_SECOND_RATE = None
        HEART_SECOND_BP_SYSTOLIC = None
        HEART_SECOND_BP_DIASTOLIC = None
        HEART_SECOND_RHYTHM = None
        HEART_SECOND_SKIPPED_REASON = None
        if HEART_SECOND_SKIPPED == 0:
            HEART_SECOND_RATE = self.fake.random_int(MIN_HEART_RATE, MAX_HEART_RATE)
            HEART_SECOND_BP_SYSTOLIC = self.fake.random_int(
                MIN_BP_SYSTOLIC, MAX_BP_SYSTOLIC
            )
            HEART_SECOND_BP_DIASTOLIC = self.fake.random_int(
                MIN_BP_DIASTOLIC, MAX_BP_DIASTOLIC
            )
            HEART_SECOND_RHYTHM = generate_code(
                self.fake, "HEART_SECOND_RHYTHM", enforce_numeric_codes=True
            )
        elif HEART_SECOND_SKIPPED == 1:
            HEART_SECOND_SKIPPED_REASON = generate_code(
                self.fake, "HEART_SECOND_SKIPPED_REASON", enforce_numeric_codes=True
            )

        HEART_THIRD_SKIPPED = generate_code(
            self.fake, "HEART_THIRD_SKIPPED", enforce_numeric_codes=True
        )

        HEART_THIRD_RATE = None
        HEART_THIRD_BP_SYSTOLIC = None
        HEART_THIRD_BP_DIASTOLIC = None
        HEART_THIRD_RHYTHM = None
        HEART_THIRD_SKIPPED_REASON = None
        if HEART_THIRD_SKIPPED == 0:
            HEART_THIRD_RATE = self.fake.random_int(MIN_HEART_RATE, MAX_HEART_RATE)
            HEART_THIRD_BP_SYSTOLIC = self.fake.random_int(
                MIN_BP_SYSTOLIC, MAX_BP_SYSTOLIC
            )
            HEART_THIRD_BP_DIASTOLIC = self.fake.random_int(
                MIN_BP_DIASTOLIC, MAX_BP_DIASTOLIC
            )
            HEART_THIRD_RHYTHM = generate_code(
                self.fake, "HEART_THIRD_RHYTHM", enforce_numeric_codes=True
            )
        elif HEART_THIRD_SKIPPED == 1:
            HEART_THIRD_SKIPPED_REASON = generate_code(
                self.fake, "HEART_THIRD_SKIPPED_REASON", enforce_numeric_codes=True
            )

        # TODO: what do these look like?
        CLINIC_SITE_REF = generate_id(self.fake)
        CLINIC_PROVIDER = generate_id(self.fake)

        IS_MOBILE_CLINIC = generate_code(
            self.fake, "IS_MOBILE_CLINIC", enforce_numeric_codes=True
        )

        return ClinicMeasurements(
            ID=ID,
            PID=PID,
            APPOINTMENT_VERSION=APPOINTMENT_VERSION,
            APPOINTMENT_DATETIME=APPOINTMENT_DATETIME,
            HEIGHT=HEIGHT,
            WEIGHT=WEIGHT,
            WAIST=WAIST,
            HEART_FIRST_RATE=HEART_FIRST_RATE,
            HEART_FIRST_BP_SYSTOLIC=HEART_FIRST_BP_SYSTOLIC,
            HEART_FIRST_BP_DIASTOLIC=HEART_FIRST_BP_DIASTOLIC,
            HEART_SECOND_RATE=HEART_SECOND_RATE,
            HEART_SECOND_BP_SYSTOLIC=HEART_SECOND_BP_SYSTOLIC,
            HEART_SECOND_BP_DIASTOLIC=HEART_SECOND_BP_DIASTOLIC,
            HEART_THIRD_RATE=HEART_THIRD_RATE,
            HEART_THIRD_BP_SYSTOLIC=HEART_THIRD_BP_SYSTOLIC,
            HEART_THIRD_BP_DIASTOLIC=HEART_THIRD_BP_DIASTOLIC,
            HEIGHT_SKIPPED=HEIGHT_SKIPPED,
            WEIGHT_SKIPPED=WEIGHT_SKIPPED,
            WAIST_SKIPPED=WAIST_SKIPPED,
            HEART_FIRST_SKIPPED=HEART_FIRST_SKIPPED,
            HEART_SECOND_SKIPPED=HEART_SECOND_SKIPPED,
            HEART_THIRD_SKIPPED=HEART_THIRD_SKIPPED,
            HEIGHT_SKIPPED_REASON=HEIGHT_SKIPPED_REASON,
            WEIGHT_SKIPPED_REASON=WEIGHT_SKIPPED_REASON,
            WAIST_SKIPPED_REASON=WAIST_SKIPPED_REASON,
            HEART_FIRST_RHYTHM=HEART_FIRST_RHYTHM,
            HEART_SECOND_RHYTHM=HEART_SECOND_RHYTHM,
            HEART_THIRD_RHYTHM=HEART_THIRD_RHYTHM,
            HEART_FIRST_SKIPPED_REASON=HEART_FIRST_SKIPPED_REASON,
            HEART_SECOND_SKIPPED_REASON=HEART_SECOND_SKIPPED_REASON,
            HEART_THIRD_SKIPPED_REASON=HEART_THIRD_SKIPPED_REASON,
            CLINIC_SITE_REF=CLINIC_SITE_REF,
            CLINIC_PROVIDER=CLINIC_PROVIDER,
            IS_MOBILE_CLINIC=IS_MOBILE_CLINIC,
        )
