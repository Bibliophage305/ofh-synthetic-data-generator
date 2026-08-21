from dataclasses import dataclass

from dataclass_type_validator import dataclass_validate
from faker import Faker

from .helpers import generate_code, generate_id

HAS_LSOA_AT_REG_PERCENTAGE = 50


@dataclass_validate
@dataclass
class LSOA:
    PID: str
    ID: str
    LSOA_AT_REG: str | None


class LSOAFactory:
    def __init__(self, fake: Faker):
        self.fake = fake

    def generate(self, PID):
        # TODO: what do these ids look like?
        ID = generate_id(self.fake)

        # TODO: are these codes always present? Currently nullable, should it be?
        if self.fake.pybool(truth_probability=HAS_LSOA_AT_REG_PERCENTAGE):
            LSOA_AT_REG = generate_code(self.fake, "LSOA_AT_REG")
        else:
            LSOA_AT_REG = None

        return LSOA(PID=PID, ID=ID, LSOA_AT_REG=LSOA_AT_REG)
