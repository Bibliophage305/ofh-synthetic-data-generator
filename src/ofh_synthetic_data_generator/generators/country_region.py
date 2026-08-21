from dataclasses import dataclass

from dataclass_type_validator import dataclass_validate
from faker import Faker

from .helpers import generate_code, generate_id


@dataclass_validate
@dataclass
class CountryRegion:
    PID: str
    ID: str
    COUNTRY_AT_REG: str
    REGION_AT_REG: str


class CountryRegionFactory:
    def __init__(self, fake: Faker):
        self.fake = fake

    def generate(self, PID):
        # TODO: what do these ids look like?
        ID = generate_id(self.fake)

        # TODO: are these codes always present? Should this field be nullable?
        COUNTRY_AT_REG = generate_code(self.fake, "COUNTRY_AT_REG")
        REGION_AT_REG = generate_code(self.fake, "REGION_AT_REG")

        return CountryRegion(
            PID=PID, ID=ID, COUNTRY_AT_REG=COUNTRY_AT_REG, REGION_AT_REG=REGION_AT_REG
        )
