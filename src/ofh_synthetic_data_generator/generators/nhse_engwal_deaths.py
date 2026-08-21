from dataclasses import dataclass
from datetime import date

from dataclass_type_validator import dataclass_validate
from faker import Faker

from ofh_synthetic_data_generator.constants import (
    STUDY_END_DATE,
    STUDY_START_DATE,
)

from .helpers import generate_code

NEXT_S_COD_CODE_EMPTY_PERCENTAGE = 20


@dataclass_validate
@dataclass
class NHSEEngWalDeaths:
    PID: str
    REG_DATE: date
    REG_DATE_OF_DEATH: date
    ROW_ID: str
    S_COD_CODE_1: str
    S_COD_CODE_2: str | None
    S_COD_CODE_3: str | None
    S_COD_CODE_4: str | None
    S_COD_CODE_5: str | None
    S_COD_CODE_6: str | None
    S_COD_CODE_7: str | None
    S_COD_CODE_8: str | None
    S_COD_CODE_9: str | None
    S_COD_CODE_10: str | None
    S_COD_CODE_11: str | None
    S_COD_CODE_12: str | None
    S_COD_CODE_13: str | None
    S_COD_CODE_14: str | None
    S_COD_CODE_15: str | None
    S_UNDERLYING_COD_ICD10: str


class NHSEEngWalDeathsFactory:
    def __init__(self, fake: Faker):
        self.fake = fake

    def generate(self, PID, previous_row_count):
        REG_DATE = self.fake.date_between(
            start_date=STUDY_START_DATE,
            end_date=STUDY_END_DATE,
        )
        REG_DATE_OF_DEATH = self.fake.date_between(
            start_date=REG_DATE,
            end_date=STUDY_END_DATE,
        )

        ROW_ID = str(previous_row_count)

        s_cod_codes = []
        for code_number in range(1, 16):
            if code_number == 1:
                s_cod_codes.append(generate_code(self.fake, "ICD10_coding"))
            elif s_cod_codes[code_number - 2] is None:
                s_cod_codes.append(None)
            elif self.fake.pybool(
                truth_probability=100 - NEXT_S_COD_CODE_EMPTY_PERCENTAGE
            ):
                s_cod_codes.append(generate_code(self.fake, "ICD10_coding"))
            else:
                s_cod_codes.append(None)

        S_UNDERLYING_COD_ICD10 = generate_code(self.fake, "ICD10_coding")

        return NHSEEngWalDeaths(
            PID=PID,
            REG_DATE=REG_DATE,
            REG_DATE_OF_DEATH=REG_DATE_OF_DEATH,
            ROW_ID=ROW_ID,
            S_COD_CODE_1=s_cod_codes[0],
            S_COD_CODE_2=s_cod_codes[1],
            S_COD_CODE_3=s_cod_codes[2],
            S_COD_CODE_4=s_cod_codes[3],
            S_COD_CODE_5=s_cod_codes[4],
            S_COD_CODE_6=s_cod_codes[5],
            S_COD_CODE_7=s_cod_codes[6],
            S_COD_CODE_8=s_cod_codes[7],
            S_COD_CODE_9=s_cod_codes[8],
            S_COD_CODE_10=s_cod_codes[9],
            S_COD_CODE_11=s_cod_codes[10],
            S_COD_CODE_12=s_cod_codes[11],
            S_COD_CODE_13=s_cod_codes[12],
            S_COD_CODE_14=s_cod_codes[13],
            S_COD_CODE_15=s_cod_codes[14],
            S_UNDERLYING_COD_ICD10=S_UNDERLYING_COD_ICD10,
        )
