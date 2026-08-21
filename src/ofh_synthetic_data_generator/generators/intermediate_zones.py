from dataclasses import dataclass

from dataclass_type_validator import dataclass_validate
from faker import Faker

from .helpers import generate_code, generate_id


@dataclass_validate
@dataclass
class IntermediateZones:
    PID: str
    ID: str
    IZ_AT_REG: str | None


class IntermediateZonesFactory:
    def __init__(self, fake: Faker):
        self.fake = fake

    def generate(self, PID):
        # TODO: what do these ids look like?
        ID = generate_id(self.fake)

        # TODO: are these codes always present? Should this field be nullable?
        IZ_AT_REG = generate_code(self.fake, "IZ_AT_REG")

        return IntermediateZones(PID=PID, ID=ID, IZ_AT_REG=IZ_AT_REG)
