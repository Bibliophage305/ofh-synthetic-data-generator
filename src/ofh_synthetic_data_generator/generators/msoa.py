from dataclasses import dataclass

from dataclass_type_validator import dataclass_validate
from faker import Faker

from .helpers import generate_code, generate_id

HAS_MSOA_AT_REG_PERCENTAGE = 50


@dataclass_validate
@dataclass
class MSOA:
    PID: str
    ID: str
    MSOA_AT_REG: str | None


class MSOAFactory:
    def __init__(self, fake: Faker):
        self.fake = fake

    def generate(self, PID):
        # TODO: what do these ids look like?
        ID = generate_id(self.fake)

        # TODO: are these codes always present? Currently nullable, should it be?
        if self.fake.pybool(truth_probability=HAS_MSOA_AT_REG_PERCENTAGE):
            MSOA_AT_REG = generate_code(self.fake, "MSOA_AT_REG")
        else:
            MSOA_AT_REG = None

        return MSOA(PID=PID, ID=ID, MSOA_AT_REG=MSOA_AT_REG)
