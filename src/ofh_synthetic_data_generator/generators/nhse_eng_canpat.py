from dataclasses import dataclass
from datetime import date

from dataclass_type_validator import dataclass_validate
from faker import Faker

from ofh_synthetic_data_generator.constants import STUDY_END_DATE

from .helpers import generate_code, generate_id

NEXT_EVENT_PROPERTY_EMPTY_PERCENTAGE = 40


@dataclass_validate
@dataclass
class NHSEENGCanPat:
    EVENT_DATE: date
    EVENT_END: date
    EVENT_PROPERTY_1: str
    EVENT_PROPERTY_2: str | None
    EVENT_PROPERTY_3: str | None
    EVENT_TYPE: int
    PID: str
    PSEUDONYMISED_AVPID: str
    PSEUDONYMISED_TUMOURID: str
    ROW_ID: str
    SOURCE_ID: str
    SOURCE_TABLE: str


class NHSEENGCanPatFactory:
    def __init__(self, fake: Faker):
        self.fake = fake

    def generate(self, PID, birth_date, previous_row_count):
        # TODO: is this an accurate representation of the event date and end date? Should either be nullable?
        EVENT_DATE = self.fake.date_between(
            start_date=birth_date, end_date=STUDY_END_DATE
        )
        EVENT_END = self.fake.date_between(
            start_date=EVENT_DATE, end_date=STUDY_END_DATE
        )

        # TODO: what do these properties look like?
        EVENT_PROPERTY_1 = self.fake.sentence(nb_words=10)

        if self.fake.pybool(
            truth_probability=100 - NEXT_EVENT_PROPERTY_EMPTY_PERCENTAGE
        ):
            EVENT_PROPERTY_2 = self.fake.sentence(nb_words=10)
        else:
            EVENT_PROPERTY_2 = None

        if self.fake.pybool(
            truth_probability=100 - NEXT_EVENT_PROPERTY_EMPTY_PERCENTAGE
        ):
            EVENT_PROPERTY_3 = self.fake.sentence(nb_words=10)
        else:
            EVENT_PROPERTY_3 = None

        EVENT_TYPE = generate_code(
            self.fake, "EVENT_TYPE_pathway_coding", enforce_numeric_codes=True
        )

        # TODO: what do these ids look like?
        PSEUDONYMISED_AVPID = generate_id(self.fake)
        PSEUDONYMISED_TUMOURID = generate_id(self.fake)
        ROW_ID = str(previous_row_count)
        SOURCE_ID = generate_id(self.fake)

        # TODO: this is definitely wrong, what should the source table be?
        SOURCE_TABLE = generate_id(self.fake)

        return NHSEENGCanPat(
            EVENT_DATE=EVENT_DATE,
            EVENT_END=EVENT_END,
            EVENT_PROPERTY_1=EVENT_PROPERTY_1,
            EVENT_PROPERTY_2=EVENT_PROPERTY_2,
            EVENT_PROPERTY_3=EVENT_PROPERTY_3,
            EVENT_TYPE=EVENT_TYPE,
            PID=PID,
            PSEUDONYMISED_AVPID=PSEUDONYMISED_AVPID,
            PSEUDONYMISED_TUMOURID=PSEUDONYMISED_TUMOURID,
            ROW_ID=ROW_ID,
            SOURCE_ID=SOURCE_ID,
            SOURCE_TABLE=SOURCE_TABLE,
        )
