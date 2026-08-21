import calendar
from dataclasses import dataclass
from datetime import date

from dataclass_type_validator import dataclass_validate
from faker import Faker

from ofh_synthetic_data_generator.constants import (
    MINIMUM_AGE_YEARS,
    STUDY_END_DATE,
    STUDY_START_DATE,
)

from .clinic_measurements import ClinicMeasurements, ClinicMeasurementsFactory
from .country_region import CountryRegion, CountryRegionFactory
from .helpers import generate_code, generate_id
from .intermediate_zones import IntermediateZones, IntermediateZonesFactory
from .lsoa import LSOA, LSOAFactory
from .msoa import MSOA, MSOAFactory
from .nhse_eng_canpat import NHSEENGCanPat, NHSEENGCanPatFactory
from .nhse_eng_canreg_pattumour import (
    NHSEEngCanRegPatTumour,
    NHSEEngCanRegPatTumourFactory,
)
from .nhse_engwal_deaths import NHSEEngWalDeaths, NHSEEngWalDeathsFactory
from .participant_nhs_linked import (
    ParticipantNHSLinked,
    ParticipantNHSLinkedFactory,
)
from .questionnaire import Questionnaire, QuestionnaireFactory

BIRTH_DATE_SUPPRESSION_PERCENTAGE = 5
EARLIEST_BIRTH_DATE = date(1910, 1, 1)

# TODO: what are the consent versions? Are they always present? Should this field be nullable?
CONSENT_VERSIONS = ["v1", "v2", "v3"]

PARTICIPANT_NHSE_ENGWAL_DEATHS_PERCENTAGE = 5
PARTICIPANT_NHS_LINKED_PERCENTAGE = 95

PARTICIPANT_NHSE_ENG_CANPAT_RECORD_PERCENTAGE = 20


@dataclass_validate
@dataclass
class Participant:
    PID: str
    REGISTRATION_YEAR: int
    REGISTRATION_MONTH: int
    CONSENT_VERSION: str
    CONSENT_YEAR: int
    CONSENT_MONTH: int
    BIRTH_YEAR: int
    BIRTH_MONTH: int
    BLOOD_SAMPLE: int
    DEMOG_ETHNICITY_1_1: int
    DEMOG_GENDER_1_1: int
    DEMOG_GENDER_2_1: int
    DEMOG_SEX_1_1: int
    DEMOG_SEX_2_1: int
    clinic_measurements: list[ClinicMeasurements]
    country_region: list[CountryRegion]
    intermediate_zones: list[IntermediateZones]
    lsoa: list[LSOA]
    msoa: list[MSOA]
    nhse_eng_canpat: list[NHSEENGCanPat]
    nhse_eng_canreg_pattumour: list[NHSEEngCanRegPatTumour]
    nhse_engwal_deaths: list[NHSEEngWalDeaths]
    participant_nhs_linked: list[ParticipantNHSLinked]
    questionnaire: list[Questionnaire]


class ParticipantFactory:
    def __init__(self, fake: Faker):
        self.fake = fake

    def generate(self, datasets_lengths):
        # TODO: what do these ids look like?
        PID = generate_id(self.fake)

        latest_birth_date = date(
            STUDY_END_DATE.year - MINIMUM_AGE_YEARS,
            STUDY_END_DATE.month,
            STUDY_END_DATE.day,
        )
        birth_date = self.fake.date_between(
            start_date=EARLIEST_BIRTH_DATE,
            end_date=min(STUDY_END_DATE, latest_birth_date),
        )
        if self.fake.pybool(truth_probability=BIRTH_DATE_SUPPRESSION_PERCENTAGE):
            BIRTH_YEAR = generate_code(
                self.fake, "BIRTH_YEAR", enforce_numeric_codes=True
            )
            BIRTH_MONTH = generate_code(
                self.fake, "BIRTH_MONTH", enforce_numeric_codes=True
            )
        else:
            BIRTH_YEAR = birth_date.year
            BIRTH_MONTH = birth_date.month

        minimum_registration_date = date(
            birth_date.year + 18,
            birth_date.month,
            min(
                birth_date.day,
                calendar.monthrange(birth_date.year + 18, birth_date.month)[1],
            ),
        )

        registration_date = self.fake.date_between(
            start_date=max(minimum_registration_date, STUDY_START_DATE),
            end_date=STUDY_END_DATE,
        )
        REGISTRATION_YEAR = registration_date.year
        REGISTRATION_MONTH = registration_date.month

        CONSENT_VERSION = self.fake.random_element(elements=CONSENT_VERSIONS)

        consent_date = self.fake.date_between(
            start_date=registration_date, end_date=STUDY_END_DATE
        )
        CONSENT_YEAR = consent_date.year
        CONSENT_MONTH = consent_date.month

        BLOOD_SAMPLE = generate_code(
            self.fake, "BLOOD_SAMPLE", enforce_numeric_codes=True
        )

        # TODO: these share some similarities with the questionnaire fields, and therefore might
        # only be present if they took that version of the questionnaire. Is this correct?
        DEMOG_ETHNICITY_1_1 = generate_code(
            self.fake, "DEMOG_ETHNICITY_1_1", enforce_numeric_codes=True
        )
        DEMOG_GENDER_1_1 = generate_code(
            self.fake, "DEMOG_GENDER_1_1", enforce_numeric_codes=True
        )
        DEMOG_GENDER_2_1 = generate_code(
            self.fake, "DEMOG_GENDER_2_1", enforce_numeric_codes=True
        )
        DEMOG_SEX_1_1 = generate_code(
            self.fake, "DEMOG_SEX_1_1", enforce_numeric_codes=True
        )
        DEMOG_SEX_2_1 = generate_code(
            self.fake, "DEMOG_SEX_2_1", enforce_numeric_codes=True
        )

        # TODO: is this always present? Is there ever more than one of these?
        clinic_measurements_factory = ClinicMeasurementsFactory(self.fake)
        clinic_measurements = [
            clinic_measurements_factory.generate(PID, registration_date)
        ]

        # TODO: is this always present? Is there ever more than one of these?
        country_region_factory = CountryRegionFactory(self.fake)
        country_region = [country_region_factory.generate(PID)]

        # TODO: is this always present? Is there ever more than one of these?
        intermediate_zones_factory = IntermediateZonesFactory(self.fake)
        intermediate_zones = [intermediate_zones_factory.generate(PID)]

        # TODO: is this always present? Is there ever more than one of these?
        lsoa_factory = LSOAFactory(self.fake)
        lsoa = [lsoa_factory.generate(PID)]

        # TODO: is this always present? Is there ever more than one of these?
        msoa_factory = MSOAFactory(self.fake)
        msoa = [msoa_factory.generate(PID)]

        # TODO: I have assumed that if a patient has cancer, they will have a record in the nhse_eng_canreg_pattumour table. Is this correct?
        if self.fake.pybool(
            truth_probability=PARTICIPANT_NHSE_ENG_CANPAT_RECORD_PERCENTAGE
        ):
            nhse_eng_canpat_factory = NHSEENGCanPatFactory(self.fake)
            # TODO: how many of these records are there per participant? Is there a maximum number? Should this be a random number? Can the dates overlap? Should the dates be in order? Should the dates be within a certain range of each other?
            nhse_eng_canpat = [
                nhse_eng_canpat_factory.generate(
                    PID, birth_date, datasets_lengths["nhse_eng_canpat"]
                )
                for _ in range(self.fake.random_int(min=1, max=5))
            ]

            nhse_eng_canreg_pattumour_factory = NHSEEngCanRegPatTumourFactory(self.fake)
            # TODO: how many of these records are there per participant? Is there a maximum number? Should this be a random number?
            nhse_eng_canreg_pattumour = [
                nhse_eng_canreg_pattumour_factory.generate(
                    PID, birth_date, datasets_lengths["nhse_eng_canreg_pattumour"]
                )
                for _ in range(self.fake.random_int(min=1, max=5))
            ]
        else:
            nhse_eng_canpat = []
            nhse_eng_canreg_pattumour = []

        # TODO: is this always present? Is there ever more than one of these?
        questionnaire_factory = QuestionnaireFactory(self.fake)
        questionnaire = questionnaire_factory.generate(PID, birth_date, DEMOG_SEX_2_1)

        # TODO: is this always present? Is there ever more than one of these?
        participant_has_nhs_linked_record = self.fake.pybool(
            truth_probability=PARTICIPANT_NHS_LINKED_PERCENTAGE
        )
        if participant_has_nhs_linked_record:
            participant_nhs_linked_factory = ParticipantNHSLinkedFactory(self.fake)
            participant_nhs_linked = [participant_nhs_linked_factory.generate(PID)]
        else:
            participant_nhs_linked = []

        # TODO: is this always present? Is there ever more than one of these?
        if participant_has_nhs_linked_record and self.fake.pybool(
            truth_probability=PARTICIPANT_NHSE_ENGWAL_DEATHS_PERCENTAGE
        ):
            nhse_engwal_deaths_factory = NHSEEngWalDeathsFactory(self.fake)
            nhse_engwal_deaths = [
                nhse_engwal_deaths_factory.generate(
                    PID, datasets_lengths["nhse_engwal_deaths"]
                )
            ]
        else:
            nhse_engwal_deaths = []

        return Participant(
            PID=PID,
            REGISTRATION_YEAR=REGISTRATION_YEAR,
            REGISTRATION_MONTH=REGISTRATION_MONTH,
            CONSENT_VERSION=CONSENT_VERSION,
            CONSENT_YEAR=CONSENT_YEAR,
            CONSENT_MONTH=CONSENT_MONTH,
            BIRTH_YEAR=BIRTH_YEAR,
            BIRTH_MONTH=BIRTH_MONTH,
            BLOOD_SAMPLE=BLOOD_SAMPLE,
            DEMOG_ETHNICITY_1_1=DEMOG_ETHNICITY_1_1,
            DEMOG_GENDER_1_1=DEMOG_GENDER_1_1,
            DEMOG_GENDER_2_1=DEMOG_GENDER_2_1,
            DEMOG_SEX_1_1=DEMOG_SEX_1_1,
            DEMOG_SEX_2_1=DEMOG_SEX_2_1,
            clinic_measurements=clinic_measurements,
            country_region=country_region,
            intermediate_zones=intermediate_zones,
            lsoa=lsoa,
            msoa=msoa,
            nhse_eng_canreg_pattumour=nhse_eng_canreg_pattumour,
            nhse_eng_canpat=nhse_eng_canpat,
            nhse_engwal_deaths=nhse_engwal_deaths,
            participant_nhs_linked=participant_nhs_linked,
            questionnaire=questionnaire,
        )
