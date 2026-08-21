import json
import uuid
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path

import pandas as pd
import questionary
import tqdm
from faker import Faker
from questionary import ValidationError, Validator

from ofh_synthetic_data_generator.constants import (
    HEALTH_DATA_DICTIONARY_PATH,
    SEED,
)
from ofh_synthetic_data_generator.generators.participant import (
    ParticipantFactory,
)


class RowCountValidator(Validator):
    def validate(self, document):
        if len(document.text) == 0:
            raise ValidationError(
                message="Please enter a value",
                cursor_position=len(document.text),
            )
        if not document.text.isdigit():
            raise ValidationError(
                message="Please enter a valid integer",
                cursor_position=len(document.text),
            )
        if int(document.text) <= 0:
            raise ValidationError(
                message="Please enter a positive integer",
                cursor_position=len(document.text),
            )
        if int(document.text) > 1000000:
            raise ValidationError(
                message="Please enter a value less than 1,000,000",
                cursor_position=len(document.text),
            )


def read_health_data_dictionary(health_data_dictionary_path):
    health_data_dictionary = {}

    for path in health_data_dictionary_path.glob("*.csv"):
        entity = path.stem
        health_data_dictionary[entity] = pd.read_csv(path)

    return health_data_dictionary


health_data_dictionaries = read_health_data_dictionary(HEALTH_DATA_DICTIONARY_PATH)


def unwrap_nested_model(model_name, model):
    field_names = set(health_data_dictionaries[model_name]["name"])
    ret = defaultdict(list)
    ret[model_name].append(
        {col: value for col, value in asdict(model).items() if col in field_names}
    )
    for col in asdict(model):
        if col not in field_names:
            if col not in health_data_dictionaries:
                raise ValueError(f"Column '{col}' not found in health data dictionary")
            value = getattr(model, col)
            if isinstance(value, list):
                for item in value:
                    ret.update(unwrap_nested_model(col, item))
            else:
                ret.update(unwrap_nested_model(col, value))
    return ret


def main():
    participants_to_generate = int(
        questionary.text(
            "How many synthetic participants do you want to generate?",
            default="100",
            validate=RowCountValidator,
        ).ask()
    )

    fake = Faker()
    Faker.seed(SEED)

    participant_factory = ParticipantFactory(fake)
    datasets = defaultdict(list)
    datasets_lengths = defaultdict(int)
    for _ in tqdm.trange(participants_to_generate):
        participant = participant_factory.generate(datasets_lengths)
        for k, v in unwrap_nested_model("participant", participant).items():
            datasets[k].extend(v)
        for k, v in datasets.items():
            datasets_lengths[k] = len(v)

    output_path = Path(__file__).parent / "outputs" / str(uuid.uuid4())[:8]
    output_path.mkdir(parents=True, exist_ok=True)

    for dataset, records in datasets.items():
        df = pd.DataFrame(records)
        df.to_csv(output_path / f"{dataset}.csv", index=False)

    metadata = {
        "created_at": pd.Timestamp.now().isoformat(),
        "datasets": list(datasets.keys()),
    }

    with open(output_path / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)


if __name__ == "__main__":
    main()
