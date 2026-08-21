from dataclasses import dataclass
from datetime import date

from dataclass_type_validator import dataclass_validate
from faker import Faker

from ofh_synthetic_data_generator.constants import STUDY_END_DATE

from .helpers import generate_code, generate_id


@dataclass_validate
@dataclass
class NHSEEngCanRegPatTumour:
    BEHAVIOUR_CODED: str
    BEHAVIOUR_CODED_DESC: str
    BEHAVIOUR_ICD10_O2: str
    BIGTUMOURCOUNT: int
    CODING_SYSTEM: str
    CODING_SYSTEM_DESC: str
    DIAGNOSISDATE1: date
    DIAGNOSISDATE2: date
    DIAGNOSISDATEBEST: date
    DUKES: str
    ER_SCORE: str
    ER_STATUS: str
    FIGO: str
    GLEASON_COMBINED: int
    GLEASON_PRIMARY: int
    GLEASON_SECONDARY: int
    GLEASON_TERTIARY: int
    GRADE: str
    HER2_STATUS: str
    HISTOLOGY_CODED: str
    HISTOLOGY_CODED_DESC: str
    IMD_QUINTILE: str
    LATERALITY: str
    MORPH_CODED: str
    MORPH_ICD10_O2: str
    M_BEST: str
    NODESEXCISED: int
    NODESINVOLVED: int
    NPI: float
    N_BEST: str
    PID: str
    PR_SCORE: str
    PR_STATUS: str
    PSEUDONYMISED_TUMOURID: str
    ROW_ID: str
    SCREENDETECTED: str
    SCREENINGSTATUSCOSD_CODE: str
    SCREENINGSTATUSCOSD_NAME: str
    SCREENINGSTATUSFULL_CODE: str
    SCREENINGSTATUSFULL_NAME: str
    SITE_CODED: str
    SITE_CODED_3CHAR: str
    SITE_CODED_DESC: str
    SITE_ICD10_O2: str
    STAGE_BEST: str
    STAGE_BEST_SYSTEM: str
    TUMOURCOUNT: int
    TUMOURSIZE: float
    T_BEST: str


class NHSEEngCanRegPatTumourFactory:
    def __init__(self, fake: Faker):
        self.fake = fake

    def generate(self, PID, birth_date, previous_row_count):
        BEHAVIOUR_CODED = generate_code(self.fake, "BEHAVIOUR_CODED_pattumour_coding")
        BEHAVIOUR_CODED_DESC = self.fake.sentence(nb_words=10)
        BEHAVIOUR_ICD10_O2 = generate_code(
            self.fake, "BEHAVIOUR_ICD10_O2_pattumour_coding"
        )

        # TODO: are these sensible bounds for tumour count?
        BIGTUMOURCOUNT = self.fake.random_int(min=1, max=10)

        CODING_SYSTEM = generate_code(self.fake, "CODING_SYSTEM_pattumour_coding")
        CODING_SYSTEM_DESC = self.fake.sentence(nb_words=10)

        # TODO: how do these dates interact, if at all?
        DIAGNOSISDATE1 = self.fake.date_between(
            start_date=birth_date, end_date=STUDY_END_DATE
        )
        DIAGNOSISDATE2 = self.fake.date_between(
            start_date=birth_date, end_date=STUDY_END_DATE
        )
        DIAGNOSISDATEBEST = self.fake.date_between(
            start_date=birth_date, end_date=STUDY_END_DATE
        )

        DUKES = generate_code(self.fake, "DUKES_pattumour_coding")

        # TODO: what are the possible values for ER_SCORE?
        ER_SCORE = self.fake.sentence(nb_words=10)

        ER_STATUS = generate_code(self.fake, "ER_STATUS_pattumour_coding")

        # TODO: what are the possible values for FIGO?
        FIGO = self.fake.sentence(nb_words=10)

        # TODO: does this depend on the other Gleason values, or is it independent? What are the possible values?
        GLEASON_COMBINED = self.fake.random_int(min=1, max=10)

        # TODO: are these all always present?
        GLEASON_PRIMARY = generate_code(
            self.fake, "GLEASON_PRIMARY_pattumour_coding", enforce_numeric_codes=True
        )
        GLEASON_SECONDARY = generate_code(
            self.fake, "GLEASON_SECONDARY_pattumour_coding", enforce_numeric_codes=True
        )
        GLEASON_TERTIARY = generate_code(
            self.fake, "GLEASON_TERTIARY_pattumour_coding", enforce_numeric_codes=True
        )

        GRADE = generate_code(self.fake, "GRADE_pattumour_coding")
        HER2_STATUS = generate_code(self.fake, "HER2_STATUS_pattumour_coding")
        HISTOLOGY_CODED = generate_code(self.fake, "MORPH_coding")
        HISTOLOGY_CODED_DESC = self.fake.sentence(nb_words=10)

        # TODO: this is definitely wrong, what values can IMD_QUINTILE take?
        IMD_QUINTILE = self.fake.sentence(nb_words=10)

        LATERALITY = generate_code(self.fake, "LATERALITY_pattumour_coding")

        # TODO: these are definitely wrong, what values can MORPH_CODED and MORPH_ICD10_O2 take?
        MORPH_CODED = self.fake.sentence(nb_words=10)
        MORPH_ICD10_O2 = self.fake.sentence(nb_words=10)

        M_BEST = generate_code(self.fake, "UICC_M_coding")

        # TODO: what are the possible values for these? Do they interact?
        NODESEXCISED = self.fake.random_int(min=0, max=20)
        NODESINVOLVED = self.fake.random_int(min=0, max=20)

        # TODO: what are the possible values for NPI?
        NPI = self.fake.pyfloat(min_value=0, max_value=10, right_digits=2)

        N_BEST = generate_code(self.fake, "UICC_N_coding")

        # TODO: what are the possible values for PR_SCORE?
        PR_SCORE = self.fake.sentence(nb_words=10)

        PR_STATUS = generate_code(self.fake, "PR_STATUS_pattumour_coding")

        # TODO: what do these look like?
        PSEUDONYMISED_TUMOURID = generate_id(self.fake)

        # TODO: are row ids calculated this way as stringified sequential ints?
        ROW_ID = str(previous_row_count)

        SCREENDETECTED = generate_code(self.fake, "SCREENDETECTED_pattumour_coding")
        SCREENINGSTATUSCOSD_CODE = generate_code(
            self.fake, "SCREENINGSTATUSCOSD_CODE_pattumour_coding"
        )

        # TODO: what do these look like?
        SCREENINGSTATUSCOSD_NAME = self.fake.sentence(nb_words=10)
        SCREENINGSTATUSFULL_CODE = self.fake.sentence(nb_words=10)
        SCREENINGSTATUSFULL_NAME = self.fake.sentence(nb_words=10)

        SITE_CODED = self.fake.sentence(nb_words=10)
        SITE_CODED_3CHAR = self.fake.sentence(nb_words=10)
        SITE_CODED_DESC = self.fake.sentence(nb_words=10)

        SITE_ICD10_O2 = generate_code(self.fake, "ICD10_coding")
        STAGE_BEST = generate_code(self.fake, "STAGE_BEST_pattumour_coding")

        # TODO: what are the possible values for STAGE_BEST_SYSTEM?
        STAGE_BEST_SYSTEM = self.fake.sentence(nb_words=10)

        # TODO: what are the possible values for TUMOURSIZE? Are there any bounds on this? Does it interact with BIGTUMOURCOUNT?
        TUMOURCOUNT = self.fake.random_int(min=1, max=10)

        # TODO: what are the possible values for TUMOURSIZE?
        TUMOURSIZE = self.fake.pyfloat(min_value=0, max_value=100, right_digits=2)

        T_BEST = generate_code(self.fake, "UICC_T_coding")

        return NHSEEngCanRegPatTumour(
            BEHAVIOUR_CODED=BEHAVIOUR_CODED,
            BEHAVIOUR_CODED_DESC=BEHAVIOUR_CODED_DESC,
            BEHAVIOUR_ICD10_O2=BEHAVIOUR_ICD10_O2,
            BIGTUMOURCOUNT=BIGTUMOURCOUNT,
            CODING_SYSTEM=CODING_SYSTEM,
            CODING_SYSTEM_DESC=CODING_SYSTEM_DESC,
            DIAGNOSISDATE1=DIAGNOSISDATE1,
            DIAGNOSISDATE2=DIAGNOSISDATE2,
            DIAGNOSISDATEBEST=DIAGNOSISDATEBEST,
            DUKES=DUKES,
            ER_SCORE=ER_SCORE,
            ER_STATUS=ER_STATUS,
            FIGO=FIGO,
            GLEASON_COMBINED=GLEASON_COMBINED,
            GLEASON_PRIMARY=GLEASON_PRIMARY,
            GLEASON_SECONDARY=GLEASON_SECONDARY,
            GLEASON_TERTIARY=GLEASON_TERTIARY,
            GRADE=GRADE,
            HER2_STATUS=HER2_STATUS,
            HISTOLOGY_CODED=HISTOLOGY_CODED,
            HISTOLOGY_CODED_DESC=HISTOLOGY_CODED_DESC,
            IMD_QUINTILE=IMD_QUINTILE,
            LATERALITY=LATERALITY,
            MORPH_CODED=MORPH_CODED,
            MORPH_ICD10_O2=MORPH_ICD10_O2,
            M_BEST=M_BEST,
            NODESEXCISED=NODESEXCISED,
            NODESINVOLVED=NODESINVOLVED,
            NPI=NPI,
            N_BEST=N_BEST,
            PID=PID,
            PR_SCORE=PR_SCORE,
            PR_STATUS=PR_STATUS,
            PSEUDONYMISED_TUMOURID=PSEUDONYMISED_TUMOURID,
            ROW_ID=ROW_ID,
            SCREENDETECTED=SCREENDETECTED,
            SCREENINGSTATUSCOSD_CODE=SCREENINGSTATUSCOSD_CODE,
            SCREENINGSTATUSCOSD_NAME=SCREENINGSTATUSCOSD_NAME,
            SCREENINGSTATUSFULL_CODE=SCREENINGSTATUSFULL_CODE,
            SCREENINGSTATUSFULL_NAME=SCREENINGSTATUSFULL_NAME,
            SITE_CODED=SITE_CODED,
            SITE_CODED_3CHAR=SITE_CODED_3CHAR,
            SITE_CODED_DESC=SITE_CODED_DESC,
            SITE_ICD10_O2=SITE_ICD10_O2,
            STAGE_BEST=STAGE_BEST,
            STAGE_BEST_SYSTEM=STAGE_BEST_SYSTEM,
            TUMOURCOUNT=TUMOURCOUNT,
            TUMOURSIZE=TUMOURSIZE,
            T_BEST=T_BEST,
        )
