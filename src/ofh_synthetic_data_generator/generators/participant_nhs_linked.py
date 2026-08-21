from dataclasses import dataclass

from dataclass_type_validator import dataclass_validate
from faker import Faker

from .helpers import generate_id


@dataclass_validate
@dataclass
class ParticipantNHSLinked:
    PID: str
    ROW_ID: str


class ParticipantNHSLinkedFactory:
    def __init__(self, fake: Faker):
        self.fake = fake

    def generate(self, PID):
        # TODO: what do these ids look like?
        ROW_ID = generate_id(self.fake)

        return ParticipantNHSLinked(
            PID=PID,
            ROW_ID=ROW_ID,
        )
