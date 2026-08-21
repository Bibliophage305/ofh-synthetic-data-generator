# ofh-synthetic-data-generator

Generates synthetic data that mimics the structure of the datasets held and
curated by [Our Future Health](https://ourfuturehealth.org.uk/) in their
Trusted Research Environment (TRE).

It's intended for people who want to write and test code against
OFH-shaped data - pipelines, queries, dashboards, ETL - without needing
access to the real TRE.

**This data is realistic, not representative.** Individual values (birth
dates, heights, code lookups, etc.) are generated to look plausible, but
there is no attempt to reproduce real-world distributions, correlations, or
prevalence rates. Do not use this data to draw any conclusions about the
real Our Future Health cohort - it's only meant for schema-valid pipeline
and integration testing.

## Quickstart

The only requirement is [uv](https://docs.astral.sh/uv/).

```bash
uv run ofh-synthetic-data-generator
```

Optionally, set a SEED environment variable.

You'll be asked how many synthetic participants to generate. Every other
table is generated to be consistent with those participants (linked via
`PID`).

## Output

Each run creates a new timestamped-ish folder under `outputs/` (named with a
short random ID), containing one CSV per table plus a `metadata.json` with
the run's creation time and the list of tables generated. Nothing is
overwritten between runs.

```
outputs/
└── a1b2c3d4/
    ├── participant.csv
    ├── questionnaire.csv
    ├── lsoa.csv
    ├── ...
    └── metadata.json
```

## How it works

Each table has:

- A **data dictionary** CSV in `src/ofh_synthetic_data_generator/resources/health_data_dictionary/`,
  describing that table's fields (name, type, whether it's coded, whether
  it's multi-select, etc.). These are the same data dictionaries OFH
  publishes for the TRE itself. These data dictionaries are provided here
  for reference only, the data requirements are hard-coded.
- A **generator** in `src/ofh_synthetic_data_generator/generators/`, with a
  dataclass matching the table's fields and a `*Factory` class with a
  `generate(...)` method that produces one row.
- A shared **coding lookup** (`resources/health_codings.db`, a SQLite
  database) that `generate_code`/`generate_codes` (in `generators/helpers.py`)
  draw from for any field backed by a coding table.

`main.py` generates participants one at a time, and each `Participant`
carries its related rows (questionnaire, linked NHS records, etc.) as nested
fields; `main.py` walks that structure and writes each nested model out to
its own table/CSV.

If you're not familiar with OFH's data dictionary / coding table format,
the source data is published here:

- Data dictionary and codings: https://research.ourfuturehealth.org.uk/data-and-cohort/
- Questionnaire logic: https://ourfuturehealth.gitbook.io/our-future-health/data-types/questionnaire-data

## Tables currently implemented

- `participant`
- `questionnaire`
- `lsoa` / `msoa` / `intermediate_zones`
- `country_region`
- `clinic_measurements`
- `participant_nhs_linked`
- `nhse_engwal_deaths`
- `nhse_eng_canpat`
- `nhse_eng_canreg_pattumour`

## Known limitations

- **The OFH data dictionaries describe field names, types, and coding
  tables, but not much about what realistic values should look like** -
  no valid ranges, no field interactions, no units in some cases. Where
  I've had to guess, that's flagged inline with a `# TODO:` comment, e.g.:

  ```python
  # TODO: are these sensible bounds for tumour count?
  BIGTUMOURCOUNT = self.fake.random_int(min=1, max=10)

  # TODO: how do these dates interact, if at all?
  DIAGNOSISDATE1 = self.fake.date_between(start_date=birth_date, end_date=STUDY_END_DATE)
  ```

  If you spot a `# TODO:` you can answer with domain knowledge, or a
  generator that's making an assumption you know to be wrong, contributions
  correcting these are very welcome.
- **There's also a good chance of unknown unknowns** - some fields may be
  wrong in ways I haven't thought to question, because I'm not a domain
  expert in any of these datasets (cancer registry staging, primary care
  coding, etc.). Treat every generator as a best-effort guess unless you
  know otherwise.
- The `questionnaire` generator hardcodes the show/hide logic from OFH's
  published questionnaire logic rather than interpreting it at runtime;
  it also has its own `# NOTE:`-flagged corrections where the source logic
  had typos or looked inconsistent - worth a skim if questionnaire branching
  matters for what you're testing.
