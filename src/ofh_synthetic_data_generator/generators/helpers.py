import math

from faker import Faker

from ofh_synthetic_data_generator.db import get_codes


class ExclusiveCodes:
    def __init__(
        self,
        exclusive_percentage: int,
        negatives_are_exclusive: bool = True,
        special_exclusive_codes: list | None = None,
        special_non_exclusive_codes: list | None = None,
    ):
        self.exclusive_percentage = exclusive_percentage
        self.negatives_are_exclusive = negatives_are_exclusive
        self.special_exclusive_codes = special_exclusive_codes or []
        self.special_non_exclusive_codes = special_non_exclusive_codes or []

        if set(self.special_exclusive_codes) & set(self.special_non_exclusive_codes):
            raise ValueError("A code cannot be both exclusive and non-exclusive.")

    def _is_exclusive(self, code: int):
        if code in self.special_exclusive_codes:
            return True
        if code in self.special_non_exclusive_codes:
            return False
        return self.negatives_are_exclusive and type(code) is int and code < 0

    def get_exclusive_codes(self, codes: list[int]):
        return [code for code in codes if self._is_exclusive(code)]

    def get_non_exclusive_codes(self, codes: list[int]):
        return [code for code in codes if not self._is_exclusive(code)]


def generate_codes(
    fake: Faker,
    code_name: str,
    min_count: int = 1,
    max_count: int = math.inf,
    exclusive_codes: ExclusiveCodes | None = None,
    enforce_numeric_codes: bool = False,
):
    if exclusive_codes is None:
        exclusive_codes = ExclusiveCodes(
            exclusive_percentage=0, negatives_are_exclusive=False
        )

    codes = [
        int(code[1]) if enforce_numeric_codes else code[1]
        for code in get_codes(code_name)
    ]

    if fake.pybool(truth_probability=exclusive_codes.exclusive_percentage):
        exclusive_codes_list = exclusive_codes.get_exclusive_codes(codes)
        return [fake.random_element(elements=exclusive_codes_list)]

    non_exclusive_codes = exclusive_codes.get_non_exclusive_codes(codes)
    count = fake.random_int(
        min=min(min_count, len(non_exclusive_codes)),
        max=min(max_count, len(non_exclusive_codes)),
    )

    return sorted(
        fake.random_elements(elements=non_exclusive_codes, length=count, unique=True)
    )


def generate_code(fake: Faker, code_name: str, enforce_numeric_codes: bool = False):
    return generate_codes(
        fake,
        code_name,
        min_count=1,
        max_count=1,
        enforce_numeric_codes=enforce_numeric_codes,
    )[0]


def generate_id(fake: Faker):
    return str(fake.uuid4())
