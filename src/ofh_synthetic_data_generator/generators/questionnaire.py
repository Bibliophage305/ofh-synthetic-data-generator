from dataclasses import dataclass
from datetime import date

from dataclass_type_validator import dataclass_validate
from faker import Faker

from ofh_synthetic_data_generator.constants import (
    MAX_HEIGHT_CM,
    MAX_WEIGHT_KG,
    MIN_HEIGHT_CM,
    MIN_WEIGHT_KG,
    STUDY_END_DATE,
)

from .helpers import ExclusiveCodes, generate_code, generate_codes, generate_id

QUESTIONNAIRE_VERSIONS = [
    {"version_number": "v1", "live_date": date(2021, 5, 1)},
    {"version_number": "v2", "live_date": date(2022, 11, 20)},
    {"version_number": "v2.1", "live_date": date(2023, 12, 21)},
    {"version_number": "v2.2", "live_date": date(2024, 7, 6)},
]

PREFER_NOT_TO_ANSWER_PERCENTAGE = 15


@dataclass_validate
@dataclass
class Questionnaire:
    # non-questionnaire fields
    ID: str
    PID: str
    QUESTIONNAIRE_VERSION: str
    SUBMISSION_DATE: date

    # questionnaire fields

    # 1. About you and your household
    DEMOG_TRANSGENDER_1_1: int
    DEMOG_SEXUAL_ORIENTATION_1_1: int
    DEMOG_HEIGHT_ENTER_UNIT_1_1: int
    DEMOG_HEIGHT_1_1: float
    DEMOG_WEIGHT_ENTER_UNIT_1_1: int
    DEMOG_WEIGHT_1_1: float
    DEMOG_LANGUAGE_1_1: int
    DEMOG_RELATSH_STATUS_2_1: int
    DEMOG_RELATSH_MARR_CURR_1_1: int | None
    DEMOG_RELATSH_CIVIL_CURR_1_1: int | None
    DEMOG_RELATSH_MARR_PREV_1_1: int | None
    DEMOG_RELATSH_CIVIL_PREV_1_1: int | None
    HOUSING_TYPE_1_1: int
    HOUSING_TENURE_1_1: int | None
    HOUSING_ENERGY_1_M: list[int]
    HOUSING_HEAT_1_M: list[int]
    HOUSING_CURR_ADD_YRS_1_1: int
    HOUSING_PEOPLE_1_1: int
    HOUSING_PEOPLE_RELATE_1_M: list[int] | None
    HOUSING_VEHICLES_1_1: int

    # 2. Your work and education
    WORK_STATUS_2_M: list[int]
    WORK_YRS_1_1: int | None
    WORK_WK_HRS_1_1: int | None
    WORK_WK_TRAVEL_1_1: int | None
    WORK_TRANSPORT_1_M: list[int] | None
    WORK_DISTANCE_1_1: int | None
    WORK_WALK_STAND_1_1: int | None
    WORK_MANUAL_LABOUR_1_1: int | None
    WORK_SHIFTS_1_1: int | None
    WORK_NIGHTS_1_1: int | None
    EDU_QUAL_1_M: list[int]
    EDU_COMP_AGE_2_1: int
    HOUSING_INCOME_1_1: int

    # 3. Your lifestyle
    ACTIVITY_WALK_DAYS_2_1: int
    ACTIVITY_WALK_MINS_2_1: int | None
    ACTIVITY_MOD_DAYS_2_1: int
    ACTIVITY_MOD_MINS_2_1: int
    ACTIVITY_VIG_DAYS_2_1: int
    ACTIVITY_VIG_MINS_2_1: int
    ACTIVITY_WALK_PACE_1_1: int | None
    ACTIVITY_STAIRS_1_1: int | None
    ACTIVITY_TRANSPORT_1_M: list[int]
    ACTIVITY_TYPE_1_M: list[int]
    ACTIVITY_TYPE_WALK_1_1: int | None
    ACTIVITY_TYPE_WALK_DUR_1_1: int | None
    ACTIVITY_TYPE_EXERCISE_1_1: int | None
    ACTIVITY_TYPE_EXERCISE_DUR_1_1: int | None
    ACTIVITY_TYPE_STREN_1_1: int | None
    ACTIVITY_TYPE_STREN_DUR_1_1: int | None
    ACTIVITY_TYPE_DIY_LIGHT_1_1: int | None
    ACTIVITY_TYPE_DIY_LIGHT_DUR_1_1: int | None
    ACTIVITY_TYPE_DIY_HEAVY_1_1: int | None
    ACTIVITY_TYPE_DIY_HEAVY_DUR_1_1: int | None
    LIFESTYLE_SOCIAL_VISITS_1_1: int
    LIFESTYLE_SOCIAL_REC_1_M: list[int]
    LIFESTYLE_OUTDOOR_SUM_HRS_1_1: int
    LIFESTYLE_OUTDOOR_WIN_HRS_1_1: int
    LIFESTYLE_SCREEN_TV_HRS_2_1: int
    LIFESTYLE_SCREEN_PC_HRS_2_1: int
    LIFESTYLE_DRIVE_HRS_1_1: int
    SLEEP_HRS_1_1: int
    SLEEP_WAKING_1_1: int
    SLEEP_CHRONOTYPE_1_1: int
    SLEEP_NAPPING_1_1: int
    SLEEP_DAYTIME_1_1: int
    SLEEP_TROUBLE_1_1: int
    SLEEP_SNORING_1_1: int
    SMOKE_TOBACCO_TYPE_1_M: list[int]
    SMOKE_TOBACCO_AGE_1_1: int | None
    SMOKE_100_TIMES_2_1: int | None
    SMOKE_VAPE_AGE_2_1: int | None
    SMOKE_VAPE_USE_2_1: int | None
    SMOKE_REG_1_M: list[int] | None
    SMOKE_REG_FIRST_AGE_2_1: int | None
    SMOKE_REG_TYPE_2_1: int | None
    SMOKE_STATUS_2_1: int | None
    SMOKE_PREV_REG_2_1: int | None
    SMOKE_FIRST_AGE_2_1: int | None
    SMOKE_PREV_AGE_2_1: int | None
    SMOKE_AVG_2_1: int | None
    SMOKE_PREV_REDUCE_REASON_2_M: list[int] | None
    SMOKE_REG_DAY_2_1: int | None
    SMOKE_CHG_2_1: int | None
    SMOKE_CHG_REDUCE_REASON_2_M: list[int] | None
    SMOKE_CHG_REDUCE_ABST_1_1: int | None
    SMOKE_CHG_REDUCE_ABST_REASON_1_M: list[int] | None
    SMOKE_CHG_ABST_2_1: int | None
    SMOKE_CHG_ABST_REASON_1_M: list[int] | None
    SMOKE_VAPE_AVG_2_1: int | None
    SMOKE_VAPE_TYPE_2_M: list[int] | None
    SMOKE_EXPOSURE_1_1: int
    SMOKE_EXPOSURE_HRS_1_1: int | None
    ALCOHOL_CURR_1_1: int
    ALCOHOL_PREV_1_1: int | None
    ALCOHOL_WINE_RED_MTH_2_1: int | None
    ALCOHOL_WINE_WHITE_MTH_2_1: int | None
    ALCOHOL_BEER_MTH_2_1: int | None
    ALCOHOL_SPIRITS_MTH_2_1: int | None
    ALCOHOL_WINE_FORT_MTH_2_1: int | None
    ALCOHOL_OTHER_MTH_2_1: int | None
    ALCOHOL_WINE_RED_WK_1_1: int | None
    ALCOHOL_WINE_WHITE_WK_1_1: int | None
    ALCOHOL_BEER_WK_1_1: int | None
    ALCOHOL_SPIRITS_WK_1_1: int | None
    ALCOHOL_WINE_FORT_WK_1_1: int | None
    ALCOHOL_OTHER_WK_1_1: int | None
    ALCOHOL_FOOD_1_1: int | None
    ALCOHOL_CHG_1_1: int | None
    ALCOHOL_CHG_REDUCE_REASON_2_M: list[int] | None
    ALCOHOL_CHG_ABST_REASON_2_M: list[int] | None

    # 4. Family health history
    BIRTH_PLACE_1_1: int
    IMMIGRATE_UK_YR_1_1: int | None
    ADOPTION_STATUS_1_1: int
    FATHER_ALIVE_1_1: int
    FATHER_AGE_1_1: int | None
    FATHER_AGE_DECEASED_1_1: int | None
    FATHER_DIAG_A_2_M: list[int]
    FATHER_DIAG_AUTO_1_M: list[int] | None
    FATHER_DIAG_ANAEMIA_1_M: list[int] | None
    FATHER_DIAG_CANCER_1_M: list[int] | None
    FATHER_DIAG_CANCER_SKIN_1_M: list[int] | None
    FATHER_DIAG_GASTRO_1_M: list[int] | None
    FATHER_DIAG_ENDOCR_1_M: list[int] | None
    FATHER_DIAG_OPTHAL_1_M: list[int] | None
    FATHER_DIAG_OSTEO_1_M: list[int] | None
    FATHER_DIAG_CVD_1_M: list[int] | None
    FATHER_DIAG_UROL_1_M: list[int] | None
    FATHER_DIAG_RESP_1_M: list[int] | None
    FATHER_DIAG_PSYCH_1_M: list[int] | None
    FATHER_DIAG_PSYCH_ANX_1_M: list[int] | None
    FATHER_DIAG_PSYCH_DEPR_1_M: list[int] | None
    FATHER_DIAG_PSYCH_EAT_1_M: list[int] | None
    FATHER_DIAG_NEURO_DEV_1_M: list[int] | None
    FATHER_DIAG_NEURO_1_M: list[int] | None
    FATHER_DIAG_REPRO_1_M: list[int] | None
    MOTHER_ALIVE_1_1: int
    MOTHER_AGE_1_1: int | None
    MOTHER_AGE_DECEASED_1_1: int | None
    MOTHER_DIAG_A_2_M: list[int]
    MOTHER_DIAG_AUTO_1_M: list[int] | None
    MOTHER_DIAG_ANAEMIA_1_M: list[int] | None
    MOTHER_DIAG_CANCER_1_M: list[int] | None
    MOTHER_DIAG_CANCER_SKIN_1_M: list[int] | None
    MOTHER_DIAG_GASTRO_1_M: list[int] | None
    MOTHER_DIAG_ENDOCR_1_M: list[int] | None
    MOTHER_DIAG_OPTHAL_1_M: list[int] | None
    MOTHER_DIAG_OSTEO_1_M: list[int] | None
    MOTHER_DIAG_CVD_1_M: list[int] | None
    MOTHER_DIAG_UROL_1_M: list[int] | None
    MOTHER_DIAG_RESP_1_M: list[int] | None
    MOTHER_DIAG_PSYCH_1_M: list[int] | None
    MOTHER_DIAG_PSYCH_ANX_1_M: list[int] | None
    MOTHER_DIAG_PSYCH_DEPR_1_M: list[int] | None
    MOTHER_DIAG_PSYCH_EAT_1_M: list[int] | None
    MOTHER_DIAG_NEURO_DEV_1_M: list[int] | None
    MOTHER_DIAG_NEURO_1_M: list[int] | None
    MOTHER_DIAG_REPRO_1_M: list[int] | None
    SIBLING_NUM_BROTHERS_1_1: int
    SIBLING_NUM_SISTERS_1_1: int
    SIBLING_DIAG_A_2_M: list[int] | None
    SIBLING_DIAG_AUTO_1_M: list[int] | None
    SIBLING_DIAG_ANAEMIA_1_M: list[int] | None
    SIBLING_DIAG_CANCER_1_M: list[int] | None
    SIBLING_DIAG_CANCER_SKIN_1_M: list[int] | None
    SIBLING_DIAG_GASTRO_1_M: list[int] | None
    SIBLING_DIAG_ENDOCR_1_M: list[int] | None
    SIBLING_DIAG_OPTHAL_1_M: list[int] | None
    SIBLING_DIAG_OSTEO_1_M: list[int] | None
    SIBLING_DIAG_CVD_1_M: list[int] | None
    SIBLING_DIAG_UROL_1_M: list[int] | None
    SIBLING_DIAG_RESP_1_M: list[int] | None
    SIBLING_DIAG_PSYCH_1_M: list[int] | None
    SIBLING_DIAG_PSYCH_ANX_1_M: list[int] | None
    SIBLING_DIAG_PSYCH_DEPR_1_M: list[int] | None
    SIBLING_DIAG_PSYCH_EAT_1_M: list[int] | None
    SIBLING_DIAG_NEURO_DEV_1_M: list[int] | None
    SIBLING_DIAG_NEURO_1_M: list[int] | None
    SIBLING_DIAG_REPRO_1_M: list[int] | None

    # 5. Your health history
    HEALTH_STATUS_CURR_1_1: int
    HEALTH_STATUS_CHRONIC_1_1: int
    HEALTH_STATUS_DISABILITY_SUPPORT_1_M: list[int] | None
    HEALTH_STATUS_PRIVATE_HEALTHCARE_1_1: int
    HEALTH_COVID_1_1: int
    HEALTH_SUN_PROTECT_1_1: int
    HEALTH_DENTAL_1_M: list[int]
    HEALTH_FALLS_1_1: int
    HEALTH_WEIGHT_CHG_1_1: int
    HEALTH_RESP_WHEEZE_1_1: int
    HEALTH_RESP_SHORT_1_1: int | None
    HEALTH_PAIN_LEG_1_1: int | None
    HEALTH_AMPUTATION_1_1: int
    HEALTH_PAIN_ACUTE_2_M: list[int]
    HEALTH_PAIN_CHRONIC_1_M: list[int]
    HEALTH_PAIN_CHEST_1_1: int
    HEALTH_PAIN_CHEST_WALK_1_1: int | None
    HEALTH_PAIN_CHEST_WALK_UPHILL_1_1: int | None
    HEALTH_PAIN_CHEST_SUBSIDE_1_1: int | None
    HEALTH_CHECK_COLORECTAL_1_1: int
    HEALTH_CHECK_COLORECTAL_YRS_1_1: int | None
    HEALTH_CHECK_PROSTATE_1_1: int | None
    HEALTH_CHECK_PROSTATE_YRS_1_1: int | None
    CHILDREN_BIO_NUM_2_1: int | None
    CHILDREN_BIO_FIRST_AGE_1_1: int | None
    CHILDREN_BIO_LAST_AGE_1_1: int | None
    HEALTH_CHECK_MAMMOGRAM_1_1: int | None
    HEALTH_CHECK_MAMMOGRAM_YRS_1_1: int | None
    HEALTH_CHECK_SMEAR_1_1: int | None
    HEALTH_CHECK_SMEAR_YRS_1_1: int | None
    GYN_MENSTR_AGE_1_1: int | None
    GYN_MENOPAUSE_2_1: int | None
    GYN_MENOPAUSE_LAST_PERIOD_AGE_2_1: int | None
    GYN_MENSTR_LAST_PERIOD_DAYS_2_1: int | None
    GYN_MENSTR_CYCLE_DAYS_2_1: int | None
    CHILDREN_BIRTHED_NUM_1_1: int | None
    CHILDREN_BIRTHED_FIRST_AGE_1_1: int | None
    CHILDREN_BIRTHED_LAST_AGE_1_1: int | None
    GYN_CONTRACEPT_IMPLANT_1_1: int | None
    GYN_CONTRACEPT_METHODS_1_M: list[int] | None
    GYN_CONTRACEPT_PILL_FIRST_AGE_1_1: int | None
    GYN_CONTRACEPT_PILL_LAST_AGE_1_1: int | None
    GYN_HRT_1_1: int | None
    GYN_HRT_FIRST_TRT_AGE_1_1: int | None
    GYN_HRT_LAST_TRT_AGE_1_1: int | None
    GYN_HYST_1_1: int | None
    GYN_HYST_AGE_1_1: int | None
    GYN_OOPH_1_1: int | None
    GYN_OOPH_AGE_1_1: int | None
    DIAG_2_M: list[int]
    DIAG_AUTO_1_M: list[int] | None
    DIAG_ANAEMIA_1_M: list[int] | None
    DIAG_CANCER_1_M: list[int] | None
    DIAG_CANCER_SKIN_1_M: list[int] | None
    DIAG_OB_1_M: list[int] | None
    DIAG_GASTRO_1_M: list[int] | None
    DIAG_ENDOCR_1_M: list[int] | None
    DIAG_OPTHAL_1_M: list[int] | None
    DIAG_OSTEO_1_M: list[int] | None
    DIAG_CVD_1_M: list[int] | None
    DIAG_UROL_1_M: list[int] | None
    DIAG_RESP_1_M: list[int] | None
    DIAG_PSYCH_1_M: list[int] | None
    DIAG_PSYCH_ANX_1_M: list[int] | None
    DIAG_PSYCH_DEPR_1_M: list[int] | None
    DIAG_PSYCH_EAT_1_M: list[int] | None
    DIAG_NEURO_DEV_1_M: list[int] | None
    DIAG_NEURO_1_M: list[int] | None
    DIAG_REPRO_1_M: list[int] | None
    MEDICAT_1_M: list[int]
    MEDICAT_AUTO_1_M: list[int] | None
    MEDICAT_OSTEO_1_M: list[int] | None
    MEDICAT_CANCER_1_M: list[int] | None
    MEDICAT_DIAB_1_M: list[int] | None
    MEDICAT_GASTRO_1_M: list[int] | None
    MEDICAT_ENDOCR_1_M: list[int] | None
    MEDICAT_CVD_1_M: list[int] | None
    MEDICAT_RESP_1_M: list[int] | None
    MEDICAT_PSYCH_1_M: list[int] | None
    MEDICAT_PSYCH_ANTIDEPR_1_M: list[int] | None
    MEDICAT_PSYCH_ANTIPSYCH_1_M: list[int] | None
    MEDICAT_NEURO_1_M: list[int] | None
    MEDICAT_PAIN_1_M: list[int] | None
    MEDICAT_REPRO_1_M: list[int] | None
    MEDICAT_REPRO_CONTRACEPT_1_M: list[int] | None
    MEDICAT_SUPPL_1_M: list[int] | None
    SKIP_PHQ9_GAD7_1_1: int
    PHQ9_ITEM1_INTEREST_1_1: int | None
    PHQ9_ITEM2_DOWN_1_1: int | None
    PHQ9_ITEM3_SLEEP_1_1: int | None
    PHQ9_ITEM4_ENERGY_1_1: int | None
    PHQ9_ITEM5_APPETITE_1_1: int | None
    PHQ9_ITEM6_BAD_1_1: int | None
    PHQ9_ITEM7_CONCENTR_1_1: int | None
    PHQ9_ITEM8_MOVEMENT_1_1: int | None
    PHQ9_ITEM9_HARM_1_1: int | None
    PHQ9_IMPAIR_1_1: int | None
    GAD7_ITEM1_ANX_1_1: int | None
    GAD7_ITEM2_WORRY_CONTROL_1_1: int | None
    GAD7_ITEM3_WORRY_AMOUNT_1_1: int | None
    GAD7_ITEM4_RELAX_1_1: int | None
    GAD7_ITEM5_RESTLESS_1_1: int | None
    GAD7_ITEM6_ANNOYED_1_1: int | None
    GAD7_ITEM7_AFRAID_1_1: int | None
    GAD7_IMPAIR_1_1: int | None

    # fields in the data dictionary but not in the questionnaire logic
    ACTIVITY_MOD_DAYS_1_1: int | None = None
    ACTIVITY_MOD_MINS_1_1: int | None = None
    ACTIVITY_VIG_DAYS_1_1: int | None = None
    ACTIVITY_VIG_MINS_1_1: int | None = None
    ACTIVITY_WALK_DAYS_1_1: int | None = None
    ACTIVITY_WALK_MINS_1_1: int | None = None
    ALCOHOL_BEER_MTH_1_1: int | None = None
    ALCOHOL_CHG_ABST_REASON_1_1: int | None = None
    ALCOHOL_CHG_REDUCE_REASON_1_1: int | None = None
    ALCOHOL_OTHER_MTH_1_1: int | None = None
    ALCOHOL_SPIRITS_MTH_1_1: int | None = None
    ALCOHOL_WINE_FORT_MTH_1_1: int | None = None
    ALCOHOL_WINE_RED_MTH_1_1: int | None = None
    ALCOHOL_WINE_WHITE_MTH_1_1: int | None = None
    CHILDREN_BIO_NUM_1_1: int | None = None
    DEMOG_RELATSH_STATUS_1_1: int | None = None
    DIAG_1_M: list[int] | None = None
    EDU_COMP_AGE_1_1: int | None = None
    FATHER_DIAG_A_1_M: list[int] | None = None
    FATHER_DIAG_B_1_M: list[int] | None = None
    GYN_CONTRACEPT_PILL_1_1: int | None = None
    GYN_MENOPAUSE_1_1: int | None = None
    GYN_MENOPAUSE_LAST_PERIOD_AGE_1_1: int | None = None
    GYN_MENSTR_CYCLE_DAYS_1_1: int | None = None
    GYN_MENSTR_LAST_PERIOD_DAYS_1_1: int | None = None
    HEALTH_PAIN_ACUTE_1_M: list[int] | None = None
    HEALTH_PAIN_CHRONIC_BACK_1_1: int | None = None
    HEALTH_PAIN_CHRONIC_BODY_1_1: int | None = None
    HEALTH_PAIN_CHRONIC_FACE_1_1: int | None = None
    HEALTH_PAIN_CHRONIC_HEADACHE_1_1: int | None = None
    HEALTH_PAIN_CHRONIC_HIP_1_1: int | None = None
    HEALTH_PAIN_CHRONIC_KNEE_1_1: int | None = None
    HEALTH_PAIN_CHRONIC_SHOULDER_1_1: int | None = None
    HEALTH_PAIN_CHRONIC_STOMACH_1_1: int | None = None
    HEALTH_STATUS_DISABILITY_1_1: int | None = None
    HEALTH_SUN_SOLARIUM_1_1: int | None = None
    LIFESTYLE_SCREEN_PC_HRS_1_1: int | None = None
    LIFESTYLE_SCREEN_TV_HRS_1_1: int | None = None
    MEDICAT_A_1_M: list[int] | None = None
    MEDICAT_B_1_M: list[int] | None = None
    MEDICAT_C_1_M: list[int] | None = None
    MEDICAT_D_1_M: list[int] | None = None
    MEDICAT_PRESCRIPT_1_M: list[int] | None = None
    MOTHER_DIAG_A_1_M: list[int] | None = None
    MOTHER_DIAG_B_1_M: list[int] | None = None
    SIBLING_DIAG_A_1_M: list[int] | None = None
    SIBLING_DIAG_B_1_M: list[int] | None = None
    SMOKE_100_TIMES_1_1: int | None = None
    SMOKE_AVG_1_1: int | None = None
    SMOKE_AVG_PREV_1_1: int | None = None
    SMOKE_CHG_1_1: int | None = None
    SMOKE_CHG_ABST_1_1: int | None = None
    SMOKE_CHG_REDUCE_REASON_1_M: list[int] | None = None
    SMOKE_EXPOSE_HOUSE_HRS_1_1: int | None = None
    SMOKE_EXPOSE_OUTSIDE_HRS_1_1: int | None = None
    SMOKE_FIRST_AGE_1_1: int | None = None
    SMOKE_HOUSE_1_1: int | None = None
    SMOKE_PREV_AGE_1_1: int | None = None
    SMOKE_PREV_REDUCE_REASON_1_M: list[int] | None = None
    SMOKE_PREV_REG_1_1: int | None = None
    SMOKE_PREV_TYPE_1_1: int | None = None
    SMOKE_REG_DAY_1_1: int | None = None
    SMOKE_REG_FIRST_AGE_1_1: int | None = None
    SMOKE_REG_TYPE_1_1: int | None = None
    SMOKE_STATUS_1_1: int | None = None
    SMOKE_TOBACCO_PREV_1_1: int | None = None
    SMOKE_VAPE_1_1: int | None = None
    SMOKE_VAPE_AGE_1_1: int | None = None
    SMOKE_VAPE_AVG_1_1: int | None = None
    SMOKE_VAPE_TYPE_1_M: list[int] | None = None
    SMOKE_VAPE_USE_1_1: int | None = None
    WORK_STATUS_1_M: list[int] | None = None

    # fields in the questionnaire logic but not in the data dictionary
    # DEMOG_SEX_2_1
    # DEMOG_GENDER_2_1
    # DEMOG_ETHNICITY_1_1


class QuestionnaireFactory:
    def __init__(self, fake: Faker):
        self.fake = fake

    def generate(self, PID, birth_date, DEMOG_SEX_2_1):
        ID = generate_id(self.fake)

        # Currently no access to previous questionnaire logic, so using the latest version for all generated questionnaires
        questionnaire_version_index = len(QUESTIONNAIRE_VERSIONS) - 1

        # When other questionnaire versions are available, use the following line to randomly select a version for each generated questionnaire
        # questionnaire_version_index = self.fake.random_element(elements=range(len(QUESTIONNAIRE_VERSIONS)))

        QUESTIONNAIRE_VERSION = QUESTIONNAIRE_VERSIONS[questionnaire_version_index][
            "version_number"
        ]
        SUBMISSION_DATE = self.fake.date_between(
            start_date=max(
                QUESTIONNAIRE_VERSIONS[questionnaire_version_index]["live_date"],
                birth_date,
            ),
            end_date=(
                QUESTIONNAIRE_VERSIONS[questionnaire_version_index + 1]["live_date"]
                if questionnaire_version_index + 1 < len(QUESTIONNAIRE_VERSIONS)
                else STUDY_END_DATE
            ),
        )

        # current age is submission date year minus birth date year, minus 1 if submission date month and day is before birth date month and day (birthday hasn't happened yet this year)
        current_age = (
            SUBMISSION_DATE.year
            - birth_date.year
            - (
                (SUBMISSION_DATE.month, SUBMISSION_DATE.day)
                < (birth_date.month, birth_date.day)
            )
        )

        # 1. About you and your household
        DEMOG_TRANSGENDER_1_1 = None
        DEMOG_SEXUAL_ORIENTATION_1_1 = None
        DEMOG_HEIGHT_ENTER_UNIT_1_1 = None
        DEMOG_HEIGHT_1_1 = None
        DEMOG_WEIGHT_ENTER_UNIT_1_1 = None
        DEMOG_WEIGHT_1_1 = None
        DEMOG_LANGUAGE_1_1 = None
        DEMOG_RELATSH_STATUS_2_1 = None
        DEMOG_RELATSH_MARR_CURR_1_1 = None
        DEMOG_RELATSH_CIVIL_CURR_1_1 = None
        DEMOG_RELATSH_MARR_PREV_1_1 = None
        DEMOG_RELATSH_CIVIL_PREV_1_1 = None
        HOUSING_TYPE_1_1 = None
        HOUSING_TENURE_1_1 = None
        HOUSING_ENERGY_1_M = None
        HOUSING_HEAT_1_M = None
        HOUSING_CURR_ADD_YRS_1_1 = None
        HOUSING_PEOPLE_1_1 = None
        HOUSING_PEOPLE_RELATE_1_M = None
        HOUSING_VEHICLES_1_1 = None

        DEMOG_TRANSGENDER_1_1 = generate_code(
            self.fake, "DEMOG_TRANSGENDER_1_1", enforce_numeric_codes=True
        )
        DEMOG_SEXUAL_ORIENTATION_1_1 = generate_code(
            self.fake, "DEMOG_SEXUAL_ORIENTATION_1_1", enforce_numeric_codes=True
        )
        DEMOG_HEIGHT_ENTER_UNIT_1_1 = generate_code(
            self.fake, "DEMOG_HEIGHT_ENTER_UNIT_1_1", enforce_numeric_codes=True
        )
        DEMOG_HEIGHT_1_1 = self.fake.pyfloat(
            min_value=MIN_HEIGHT_CM, max_value=MAX_HEIGHT_CM, right_digits=1
        )
        DEMOG_WEIGHT_ENTER_UNIT_1_1 = generate_code(
            self.fake, "DEMOG_WEIGHT_ENTER_UNIT_1_1", enforce_numeric_codes=True
        )
        DEMOG_WEIGHT_1_1 = self.fake.pyfloat(
            min_value=MIN_WEIGHT_KG, max_value=MAX_WEIGHT_KG, right_digits=1
        )
        DEMOG_LANGUAGE_1_1 = generate_code(
            self.fake, "DEMOG_LANGUAGE_1_1", enforce_numeric_codes=True
        )
        DEMOG_RELATSH_STATUS_2_1 = generate_code(
            self.fake, "DEMOG_RELATSH_STATUS_2_1", enforce_numeric_codes=True
        )

        if DEMOG_RELATSH_STATUS_2_1 in (2, 4):
            DEMOG_RELATSH_MARR_CURR_1_1 = generate_code(
                self.fake, "DEMOG_RELATSH_MARR_CURR_1_1", enforce_numeric_codes=True
            )
        elif DEMOG_RELATSH_STATUS_2_1 in (3, 5):
            DEMOG_RELATSH_CIVIL_CURR_1_1 = generate_code(
                self.fake, "DEMOG_RELATSH_CIVIL_CURR_1_1", enforce_numeric_codes=True
            )
        elif DEMOG_RELATSH_STATUS_2_1 in (6, 8):
            DEMOG_RELATSH_MARR_PREV_1_1 = generate_code(
                self.fake, "DEMOG_RELATSH_MARR_PREV_1_1", enforce_numeric_codes=True
            )
        elif DEMOG_RELATSH_STATUS_2_1 in (7, 9):
            DEMOG_RELATSH_CIVIL_PREV_1_1 = generate_code(
                self.fake, "DEMOG_RELATSH_CIVIL_PREV_1_1", enforce_numeric_codes=True
            )

        HOUSING_TYPE_1_1 = generate_code(
            self.fake, "HOUSING_TYPE_1_1", enforce_numeric_codes=True
        )

        if HOUSING_TYPE_1_1 in (1, 2, 3, -7, -3):
            HOUSING_TENURE_1_1 = generate_code(
                self.fake, "HOUSING_TENURE_1_1", enforce_numeric_codes=True
            )

        HOUSING_ENERGY_1_M = generate_codes(
            self.fake,
            "HOUSING_ENERGY_1_M",
            exclusive_codes=ExclusiveCodes(
                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
            ),
            enforce_numeric_codes=True,
        )

        # NOTE: Similar questions in the questionnaire logic make the negative codes exclusive, but this does not.
        # I have assumed this is a mistake and the user can't choose both valid options and something like "I don't know" or "Prefer not to answer" at the same time, so I have made the negative codes exclusive here as well.
        HOUSING_HEAT_1_M = generate_codes(
            self.fake,
            "HOUSING_HEAT_1_M",
            exclusive_codes=ExclusiveCodes(
                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
            ),
            enforce_numeric_codes=True,
        )

        if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
            HOUSING_CURR_ADD_YRS_1_1 = generate_code(
                self.fake, "HOUSING_CURR_ADD_YRS_1_1", enforce_numeric_codes=True
            )
        else:
            HOUSING_CURR_ADD_YRS_1_1 = self.fake.random_int(min=1, max=current_age)

        if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
            HOUSING_PEOPLE_1_1 = generate_code(
                self.fake, "HOUSING_PEOPLE_1_1", enforce_numeric_codes=True
            )
        else:
            HOUSING_PEOPLE_1_1 = self.fake.random_int(min=1, max=100)

        if HOUSING_PEOPLE_1_1 > 1 or HOUSING_PEOPLE_1_1 in (-1, -3):
            HOUSING_PEOPLE_RELATE_1_M = generate_codes(
                self.fake,
                "HOUSING_PEOPLE_RELATE_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        HOUSING_VEHICLES_1_1 = generate_code(
            self.fake, "HOUSING_VEHICLES_1_1", enforce_numeric_codes=True
        )

        # 2. Your work and education
        WORK_STATUS_2_M = None
        WORK_YRS_1_1 = None
        WORK_WK_HRS_1_1 = None
        WORK_WK_TRAVEL_1_1 = None
        WORK_TRANSPORT_1_M = None
        WORK_DISTANCE_1_1 = None
        WORK_WALK_STAND_1_1 = None
        WORK_MANUAL_LABOUR_1_1 = None
        WORK_SHIFTS_1_1 = None
        WORK_NIGHTS_1_1 = None
        EDU_QUAL_1_M = None
        EDU_COMP_AGE_2_1 = None
        HOUSING_INCOME_1_1 = None

        WORK_STATUS_2_M = generate_codes(
            self.fake,
            "WORK_STATUS_2_M",
            exclusive_codes=ExclusiveCodes(
                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
            ),
            enforce_numeric_codes=True,
        )

        if any(code in (1, 3, 6, 8, -3, -7) for code in WORK_STATUS_2_M):
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                WORK_YRS_1_1 = generate_code(
                    self.fake, "WORK_YRS_1_1", enforce_numeric_codes=True
                )
            else:
                WORK_YRS_1_1 = self.fake.random_int(min=1, max=current_age)

            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                WORK_WK_HRS_1_1 = generate_code(
                    self.fake, "WORK_WK_HRS_1_1", enforce_numeric_codes=True
                )
            else:
                WORK_WK_HRS_1_1 = self.fake.random_int(min=0, max=168)

            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                WORK_WK_TRAVEL_1_1 = generate_code(
                    self.fake, "WORK_WK_TRAVEL_1_1", enforce_numeric_codes=True
                )
            else:
                WORK_WK_TRAVEL_1_1 = self.fake.random_int(min=0, max=999)

            WORK_TRANSPORT_1_M = generate_codes(
                self.fake,
                "WORK_TRANSPORT_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                WORK_DISTANCE_1_1 = generate_code(
                    self.fake, "WORK_DISTANCE_1_1", enforce_numeric_codes=True
                )
            else:
                WORK_DISTANCE_1_1 = self.fake.random_int(min=0, max=999)

            WORK_WALK_STAND_1_1 = generate_code(
                self.fake, "WORK_WALK_STAND_1_1", enforce_numeric_codes=True
            )

            WORK_MANUAL_LABOUR_1_1 = generate_code(
                self.fake, "WORK_MANUAL_LABOUR_1_1", enforce_numeric_codes=True
            )

            WORK_SHIFTS_1_1 = generate_code(
                self.fake, "WORK_SHIFTS_1_1", enforce_numeric_codes=True
            )

            if WORK_SHIFTS_1_1 in (2, 3, 4, -1, -3):
                WORK_NIGHTS_1_1 = generate_code(
                    self.fake, "WORK_NIGHTS_1_1", enforce_numeric_codes=True
                )

        EDU_QUAL_1_M = generate_codes(
            self.fake,
            "EDU_QUAL_1_M",
            exclusive_codes=ExclusiveCodes(
                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
            ),
            enforce_numeric_codes=True,
        )

        if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
            EDU_COMP_AGE_2_1 = generate_code(
                self.fake, "EDU_COMP_AGE_2_1", enforce_numeric_codes=True
            )
        else:
            # Questionnaire says "Expect <= 40" but the actual enforced bound is current_age
            EDU_COMP_AGE_2_1 = self.fake.random_int(min=5, max=current_age)

        HOUSING_INCOME_1_1 = generate_code(
            self.fake, "HOUSING_INCOME_1_1", enforce_numeric_codes=True
        )

        # 3. Your lifestyle
        ACTIVITY_WALK_DAYS_2_1 = None
        ACTIVITY_WALK_MINS_2_1 = None
        ACTIVITY_MOD_DAYS_2_1 = None
        ACTIVITY_MOD_MINS_2_1 = None
        ACTIVITY_VIG_DAYS_2_1 = None
        ACTIVITY_VIG_MINS_2_1 = None
        ACTIVITY_WALK_PACE_1_1 = None
        ACTIVITY_STAIRS_1_1 = None
        ACTIVITY_TRANSPORT_1_M = None
        ACTIVITY_TYPE_1_M = None
        ACTIVITY_TYPE_WALK_1_1 = None
        ACTIVITY_TYPE_WALK_DUR_1_1 = None
        ACTIVITY_TYPE_EXERCISE_1_1 = None
        ACTIVITY_TYPE_EXERCISE_DUR_1_1 = None
        ACTIVITY_TYPE_STREN_1_1 = None
        ACTIVITY_TYPE_STREN_DUR_1_1 = None
        ACTIVITY_TYPE_DIY_LIGHT_1_1 = None
        ACTIVITY_TYPE_DIY_LIGHT_DUR_1_1 = None
        ACTIVITY_TYPE_DIY_HEAVY_1_1 = None
        ACTIVITY_TYPE_DIY_HEAVY_DUR_1_1 = None
        LIFESTYLE_SOCIAL_VISITS_1_1 = None
        LIFESTYLE_SOCIAL_REC_1_M = None
        LIFESTYLE_OUTDOOR_SUM_HRS_1_1 = None
        LIFESTYLE_OUTDOOR_WIN_HRS_1_1 = None
        LIFESTYLE_SCREEN_TV_HRS_2_1 = None
        LIFESTYLE_SCREEN_PC_HRS_2_1 = None
        LIFESTYLE_DRIVE_HRS_1_1 = None
        SLEEP_HRS_1_1 = None
        SLEEP_WAKING_1_1 = None
        SLEEP_CHRONOTYPE_1_1 = None
        SLEEP_NAPPING_1_1 = None
        SLEEP_DAYTIME_1_1 = None
        SLEEP_TROUBLE_1_1 = None
        SLEEP_SNORING_1_1 = None
        SMOKE_TOBACCO_TYPE_1_M = None
        SMOKE_TOBACCO_AGE_1_1 = None
        SMOKE_100_TIMES_2_1 = None
        SMOKE_VAPE_AGE_2_1 = None
        SMOKE_VAPE_USE_2_1 = None
        SMOKE_REG_1_M = None
        SMOKE_REG_FIRST_AGE_2_1 = None
        SMOKE_REG_TYPE_2_1 = None
        SMOKE_STATUS_2_1 = None
        SMOKE_PREV_REG_2_1 = None
        SMOKE_FIRST_AGE_2_1 = None
        SMOKE_PREV_AGE_2_1 = None
        SMOKE_AVG_2_1 = None
        SMOKE_PREV_REDUCE_REASON_2_M = None
        SMOKE_REG_DAY_2_1 = None
        SMOKE_CHG_2_1 = None
        SMOKE_CHG_REDUCE_REASON_2_M = None
        SMOKE_CHG_REDUCE_ABST_1_1 = None
        SMOKE_CHG_REDUCE_ABST_REASON_1_M = None
        SMOKE_CHG_ABST_2_1 = None
        SMOKE_CHG_ABST_REASON_1_M = None
        SMOKE_VAPE_AVG_2_1 = None
        SMOKE_VAPE_TYPE_2_M = None
        SMOKE_EXPOSURE_1_1 = None
        SMOKE_EXPOSURE_HRS_1_1 = None
        ALCOHOL_CURR_1_1 = None
        ALCOHOL_PREV_1_1 = None
        ALCOHOL_WINE_RED_MTH_2_1 = None
        ALCOHOL_WINE_WHITE_MTH_2_1 = None
        ALCOHOL_BEER_MTH_2_1 = None
        ALCOHOL_SPIRITS_MTH_2_1 = None
        ALCOHOL_WINE_FORT_MTH_2_1 = None
        ALCOHOL_OTHER_MTH_2_1 = None
        ALCOHOL_WINE_RED_WK_1_1 = None
        ALCOHOL_WINE_WHITE_WK_1_1 = None
        ALCOHOL_BEER_WK_1_1 = None
        ALCOHOL_SPIRITS_WK_1_1 = None
        ALCOHOL_WINE_FORT_WK_1_1 = None
        ALCOHOL_OTHER_WK_1_1 = None
        ALCOHOL_FOOD_1_1 = None
        ALCOHOL_CHG_1_1 = None
        ALCOHOL_CHG_REDUCE_REASON_2_M = None
        ALCOHOL_CHG_ABST_REASON_2_M = None

        if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
            ACTIVITY_WALK_DAYS_2_1 = generate_code(
                self.fake, "ACTIVITY_WALK_DAYS_2_1", enforce_numeric_codes=True
            )
        else:
            ACTIVITY_WALK_DAYS_2_1 = self.fake.random_int(min=0, max=7)

        if 0 <= ACTIVITY_WALK_DAYS_2_1 <= 7 or ACTIVITY_WALK_DAYS_2_1 in (-1, -3):
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                ACTIVITY_WALK_MINS_2_1 = generate_code(
                    self.fake, "ACTIVITY_WALK_MINS_2_1", enforce_numeric_codes=True
                )
            else:
                ACTIVITY_WALK_MINS_2_1 = self.fake.random_int(min=0, max=1440)

        if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
            ACTIVITY_MOD_DAYS_2_1 = generate_code(
                self.fake, "ACTIVITY_MOD_DAYS_2_1", enforce_numeric_codes=True
            )
        else:
            ACTIVITY_MOD_DAYS_2_1 = self.fake.random_int(min=0, max=7)

        if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
            ACTIVITY_MOD_MINS_2_1 = generate_code(
                self.fake, "ACTIVITY_MOD_MINS_2_1", enforce_numeric_codes=True
            )
        else:
            ACTIVITY_MOD_MINS_2_1 = self.fake.random_int(min=0, max=1440)

        if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
            ACTIVITY_VIG_DAYS_2_1 = generate_code(
                self.fake, "ACTIVITY_VIG_DAYS_2_1", enforce_numeric_codes=True
            )
        else:
            ACTIVITY_VIG_DAYS_2_1 = self.fake.random_int(min=0, max=7)

        if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
            ACTIVITY_VIG_MINS_2_1 = generate_code(
                self.fake, "ACTIVITY_VIG_MINS_2_1", enforce_numeric_codes=True
            )
        else:
            ACTIVITY_VIG_MINS_2_1 = self.fake.random_int(min=0, max=1440)

        if 0 <= ACTIVITY_WALK_DAYS_2_1 <= 7 or ACTIVITY_WALK_DAYS_2_1 in (-1, -3):
            ACTIVITY_WALK_PACE_1_1 = generate_code(
                self.fake, "ACTIVITY_WALK_PACE_1_1", enforce_numeric_codes=True
            )
            ACTIVITY_STAIRS_1_1 = generate_code(
                self.fake, "ACTIVITY_STAIRS_1_1", enforce_numeric_codes=True
            )

        ACTIVITY_TRANSPORT_1_M = generate_codes(
            self.fake,
            "ACTIVITY_TRANSPORT_1_M",
            exclusive_codes=ExclusiveCodes(
                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
            ),
            enforce_numeric_codes=True,
        )

        ACTIVITY_TYPE_1_M = generate_codes(
            self.fake,
            "ACTIVITY_TYPE_1_M",
            exclusive_codes=ExclusiveCodes(
                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
            ),
            enforce_numeric_codes=True,
        )

        if any(code == 1 for code in ACTIVITY_TYPE_1_M):
            ACTIVITY_TYPE_WALK_1_1 = generate_code(
                self.fake, "ACTIVITY_TYPE_WALK_1_1", enforce_numeric_codes=True
            )
            ACTIVITY_TYPE_WALK_DUR_1_1 = generate_code(
                self.fake, "ACTIVITY_TYPE_WALK_DUR_1_1", enforce_numeric_codes=True
            )

        if any(code == 2 for code in ACTIVITY_TYPE_1_M):
            ACTIVITY_TYPE_EXERCISE_1_1 = generate_code(
                self.fake, "ACTIVITY_TYPE_EXERCISE_1_1", enforce_numeric_codes=True
            )
            ACTIVITY_TYPE_EXERCISE_DUR_1_1 = generate_code(
                self.fake, "ACTIVITY_TYPE_EXERCISE_DUR_1_1", enforce_numeric_codes=True
            )

        if any(code == 3 for code in ACTIVITY_TYPE_1_M):
            ACTIVITY_TYPE_STREN_1_1 = generate_code(
                self.fake, "ACTIVITY_TYPE_STREN_1_1", enforce_numeric_codes=True
            )
            ACTIVITY_TYPE_STREN_DUR_1_1 = generate_code(
                self.fake, "ACTIVITY_TYPE_STREN_DUR_1_1", enforce_numeric_codes=True
            )

        if any(code == 4 for code in ACTIVITY_TYPE_1_M):
            ACTIVITY_TYPE_DIY_LIGHT_1_1 = generate_code(
                self.fake, "ACTIVITY_TYPE_DIY_LIGHT_1_1", enforce_numeric_codes=True
            )
            ACTIVITY_TYPE_DIY_LIGHT_DUR_1_1 = generate_code(
                self.fake, "ACTIVITY_TYPE_DIY_LIGHT_DUR_1_1", enforce_numeric_codes=True
            )

        if any(code == 5 for code in ACTIVITY_TYPE_1_M):
            ACTIVITY_TYPE_DIY_HEAVY_1_1 = generate_code(
                self.fake, "ACTIVITY_TYPE_DIY_HEAVY_1_1", enforce_numeric_codes=True
            )
            ACTIVITY_TYPE_DIY_HEAVY_DUR_1_1 = generate_code(
                self.fake, "ACTIVITY_TYPE_DIY_HEAVY_DUR_1_1", enforce_numeric_codes=True
            )

        LIFESTYLE_SOCIAL_VISITS_1_1 = generate_code(
            self.fake, "LIFESTYLE_SOCIAL_VISITS_1_1", enforce_numeric_codes=True
        )

        # NOTE: I have made negative codes exclusive here, even though the questionnaire logic does not, because it seems like a mistake that the user could choose both valid options and something like "I don't know" or "Prefer not to answer" at the same time.
        LIFESTYLE_SOCIAL_REC_1_M = generate_codes(
            self.fake,
            "LIFESTYLE_SOCIAL_REC_1_M",
            exclusive_codes=ExclusiveCodes(
                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
            ),
            enforce_numeric_codes=True,
        )

        if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
            LIFESTYLE_OUTDOOR_SUM_HRS_1_1 = generate_code(
                self.fake, "LIFESTYLE_OUTDOOR_SUM_HRS_1_1", enforce_numeric_codes=True
            )
        else:
            # NOTE: The questionnaire has no upper bound for this question, so I have enforced 24
            LIFESTYLE_OUTDOOR_SUM_HRS_1_1 = self.fake.random_int(min=0, max=24)

        if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
            LIFESTYLE_OUTDOOR_WIN_HRS_1_1 = generate_code(
                self.fake, "LIFESTYLE_OUTDOOR_WIN_HRS_1_1", enforce_numeric_codes=True
            )
        else:
            # NOTE: The questionnaire has no upper bound for this question, so I have enforced 24
            LIFESTYLE_OUTDOOR_WIN_HRS_1_1 = self.fake.random_int(min=0, max=24)

        if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
            LIFESTYLE_SCREEN_TV_HRS_2_1 = generate_code(
                self.fake, "LIFESTYLE_SCREEN_TV_HRS_2_1", enforce_numeric_codes=True
            )
        else:
            # NOTE: The questionnaire has no upper bound for this question, so I have enforced 24
            LIFESTYLE_SCREEN_TV_HRS_2_1 = self.fake.random_int(min=0, max=24)

        if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
            LIFESTYLE_SCREEN_PC_HRS_2_1 = generate_code(
                self.fake, "LIFESTYLE_SCREEN_PC_HRS_2_1", enforce_numeric_codes=True
            )
        else:
            # NOTE: The questionnaire has no upper bound for this question, so I have enforced 24
            LIFESTYLE_SCREEN_PC_HRS_2_1 = self.fake.random_int(min=0, max=24)

        if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
            LIFESTYLE_DRIVE_HRS_1_1 = generate_code(
                self.fake, "LIFESTYLE_DRIVE_HRS_1_1", enforce_numeric_codes=True
            )
        else:
            # NOTE: The questionnaire has no upper bound for this question, so I have enforced 24
            LIFESTYLE_DRIVE_HRS_1_1 = self.fake.random_int(min=0, max=24)

        if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
            SLEEP_HRS_1_1 = generate_code(
                self.fake, "SLEEP_HRS_1_1", enforce_numeric_codes=True
            )
        else:
            # NOTE: The questionnaire has no upper bound for this question, so I have enforced 24
            SLEEP_HRS_1_1 = self.fake.random_int(min=0, max=24)

        SLEEP_WAKING_1_1 = generate_code(
            self.fake, "SLEEP_WAKING_1_1", enforce_numeric_codes=True
        )

        SLEEP_CHRONOTYPE_1_1 = generate_code(
            self.fake, "SLEEP_CHRONOTYPE_1_1", enforce_numeric_codes=True
        )

        SLEEP_NAPPING_1_1 = generate_code(
            self.fake, "SLEEP_NAPPING_1_1", enforce_numeric_codes=True
        )

        SLEEP_DAYTIME_1_1 = generate_code(
            self.fake, "SLEEP_DAYTIME_1_1", enforce_numeric_codes=True
        )

        SLEEP_TROUBLE_1_1 = generate_code(
            self.fake, "SLEEP_TROUBLE_1_1", enforce_numeric_codes=True
        )

        SLEEP_SNORING_1_1 = generate_code(
            self.fake, "SLEEP_SNORING_1_1", enforce_numeric_codes=True
        )

        SMOKE_TOBACCO_TYPE_1_M = generate_codes(
            self.fake,
            "SMOKE_TOBACCO_TYPE_1_M",
            exclusive_codes=ExclusiveCodes(
                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE,
                special_exclusive_codes=[6],
            ),
            enforce_numeric_codes=True,
        )

        if 0 in SMOKE_TOBACCO_TYPE_1_M:
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                SMOKE_TOBACCO_AGE_1_1 = generate_code(
                    self.fake, "SMOKE_TOBACCO_AGE_1_1", enforce_numeric_codes=True
                )
            else:
                # NOTE: There are no bounds on this in the questionnaire, so I have assumed sensible ones
                SMOKE_TOBACCO_AGE_1_1 = self.fake.random_int(min=0, max=current_age)

            SMOKE_100_TIMES_2_1 = generate_code(
                self.fake, "SMOKE_100_TIMES_2_1", enforce_numeric_codes=True
            )

        if 1 in SMOKE_TOBACCO_TYPE_1_M:
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                SMOKE_VAPE_AGE_2_1 = generate_code(
                    self.fake, "SMOKE_VAPE_AGE_2_1", enforce_numeric_codes=True
                )
            else:
                # NOTE: There are no bounds on this in the questionnaire, so I have assumed sensible ones
                SMOKE_VAPE_AGE_2_1 = self.fake.random_int(min=0, max=current_age)

        if any(code in (0, 1, 2, 3, 4, 5, -3) for code in SMOKE_TOBACCO_TYPE_1_M):
            SMOKE_REG_1_M = generate_codes(
                self.fake,
                "SMOKE_REG_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

            if 0 in SMOKE_REG_1_M:
                if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                    SMOKE_REG_FIRST_AGE_2_1 = generate_code(
                        self.fake, "SMOKE_REG_FIRST_AGE_2_1", enforce_numeric_codes=True
                    )
                else:
                    # NOTE: There are no bounds on this in the questionnaire, so I have assumed sensible ones
                    SMOKE_REG_FIRST_AGE_2_1 = self.fake.random_int(
                        min=0, max=current_age
                    )
                SMOKE_REG_TYPE_2_1 = generate_code(
                    self.fake, "SMOKE_REG_TYPE_2_1", enforce_numeric_codes=True
                )
                SMOKE_STATUS_2_1 = generate_code(
                    self.fake, "SMOKE_STATUS_2_1", enforce_numeric_codes=True
                )

                if SMOKE_STATUS_2_1 in (2, 3, 0):
                    SMOKE_PREV_REG_2_1 = generate_code(
                        self.fake, "SMOKE_PREV_REG_2_1", enforce_numeric_codes=True
                    )

                    if SMOKE_PREV_REG_2_1 == 1:
                        if self.fake.pybool(
                            truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE
                        ):
                            SMOKE_FIRST_AGE_2_1 = generate_code(
                                self.fake,
                                "SMOKE_FIRST_AGE_2_1",
                                enforce_numeric_codes=True,
                            )
                        else:
                            # NOTE: There are no bounds on this in the questionnaire, so I have assumed sensible ones
                            SMOKE_FIRST_AGE_2_1 = self.fake.random_int(
                                min=0, max=current_age
                            )
                        if self.fake.pybool(
                            truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE
                        ):
                            SMOKE_PREV_AGE_2_1 = generate_code(
                                self.fake,
                                "SMOKE_PREV_AGE_2_1",
                                enforce_numeric_codes=True,
                            )
                        else:
                            # NOTE: There are no bounds on this in the questionnaire, so I have assumed sensible ones
                            SMOKE_PREV_AGE_2_1 = self.fake.random_int(
                                min=0, max=current_age
                            )
                        if self.fake.pybool(
                            truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE
                        ):
                            SMOKE_AVG_2_1 = generate_code(
                                self.fake, "SMOKE_AVG_2_1", enforce_numeric_codes=True
                            )
                        else:
                            # NOTE: There are no bounds on this in the questionnaire, so I have assumed sensible ones
                            SMOKE_AVG_2_1 = self.fake.random_int(min=0, max=999)
                        SMOKE_PREV_REDUCE_REASON_2_M = generate_codes(
                            self.fake,
                            "SMOKE_PREV_REDUCE_REASON_2_M",
                            exclusive_codes=ExclusiveCodes(
                                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                            ),
                            enforce_numeric_codes=True,
                        )

                if SMOKE_STATUS_2_1 == 1:
                    if self.fake.pybool(
                        truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ):
                        SMOKE_REG_DAY_2_1 = generate_code(
                            self.fake, "SMOKE_REG_DAY_2_1", enforce_numeric_codes=True
                        )
                    else:
                        # NOTE: There are no bounds on this in the questionnaire, so I have assumed sensible ones
                        SMOKE_REG_DAY_2_1 = self.fake.random_int(min=0, max=999)

                if (SMOKE_STATUS_2_1 == 1 and SMOKE_REG_DAY_2_1 is not None) or (
                    SMOKE_STATUS_2_1 in (2, 3, 0) and SMOKE_PREV_REG_2_1 in (0, -3)
                ):
                    SMOKE_CHG_2_1 = generate_code(
                        self.fake, "SMOKE_CHG_2_1", enforce_numeric_codes=True
                    )

                    if SMOKE_CHG_2_1 == 3:
                        SMOKE_CHG_REDUCE_REASON_2_M = generate_codes(
                            self.fake,
                            "SMOKE_CHG_REDUCE_REASON_2_M",
                            exclusive_codes=ExclusiveCodes(
                                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                            ),
                            enforce_numeric_codes=True,
                        )
                        SMOKE_CHG_REDUCE_ABST_1_1 = generate_code(
                            self.fake,
                            "SMOKE_CHG_REDUCE_ABST_1_1",
                            enforce_numeric_codes=True,
                        )

                        if SMOKE_CHG_REDUCE_ABST_1_1 == 1:
                            SMOKE_CHG_REDUCE_ABST_REASON_1_M = generate_codes(
                                self.fake,
                                "SMOKE_CHG_REDUCE_ABST_REASON_1_M",
                                exclusive_codes=ExclusiveCodes(
                                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                                ),
                                enforce_numeric_codes=True,
                            )

                    if SMOKE_CHG_2_1 in (1, 2, -3):
                        SMOKE_CHG_ABST_2_1 = generate_code(
                            self.fake, "SMOKE_CHG_ABST_2_1", enforce_numeric_codes=True
                        )

                        if SMOKE_CHG_ABST_2_1 == 1:
                            SMOKE_CHG_ABST_REASON_1_M = generate_codes(
                                self.fake,
                                "SMOKE_CHG_ABST_REASON_1_M",
                                exclusive_codes=ExclusiveCodes(
                                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                                ),
                                enforce_numeric_codes=True,
                            )

        # NOTE: source questionnaire_logic.csv references [SMOKE_REG_1], which isn't a real
        # field - almost certainly meant to be SMOKE_REG_1_M, so that's used here.
        # NOTE: this condition is odd because if 1 is in SMOKE_TOBACCO_TYPE_1_M then it's definitely not null
        # so the first half of the or is redundant, but it's kept here to match the source questionnaire_logic.csv
        if (1 in SMOKE_TOBACCO_TYPE_1_M and 1 in SMOKE_REG_1_M) or (
            SMOKE_TOBACCO_TYPE_1_M is not None
            and SMOKE_REG_1_M is not None
            and 1 in SMOKE_REG_1_M
        ):
            SMOKE_VAPE_AVG_2_1 = generate_code(
                self.fake, "SMOKE_VAPE_AVG_2_1", enforce_numeric_codes=True
            )
            SMOKE_VAPE_TYPE_2_M = generate_codes(
                self.fake,
                "SMOKE_VAPE_TYPE_2_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        SMOKE_EXPOSURE_1_1 = generate_code(
            self.fake, "SMOKE_EXPOSURE_1_1", enforce_numeric_codes=True
        )

        if SMOKE_EXPOSURE_1_1 in (1, 2, 3, 5, 6):
            SMOKE_EXPOSURE_HRS_1_1 = generate_code(
                self.fake, "SMOKE_EXPOSURE_HRS_1_1", enforce_numeric_codes=True
            )

        ALCOHOL_CURR_1_1 = generate_code(
            self.fake, "ALCOHOL_CURR_1_1", enforce_numeric_codes=True
        )

        if ALCOHOL_CURR_1_1 == 6:
            ALCOHOL_PREV_1_1 = generate_code(
                self.fake, "ALCOHOL_PREV_1_1", enforce_numeric_codes=True
            )

        if ALCOHOL_CURR_1_1 in (4, 5):
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                ALCOHOL_WINE_RED_MTH_2_1 = generate_code(
                    self.fake, "ALCOHOL_WINE_RED_MTH_2_1", enforce_numeric_codes=True
                )
            else:
                ALCOHOL_WINE_RED_MTH_2_1 = self.fake.random_int(min=0, max=999)
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                ALCOHOL_WINE_WHITE_MTH_2_1 = generate_code(
                    self.fake, "ALCOHOL_WINE_WHITE_MTH_2_1", enforce_numeric_codes=True
                )
            else:
                ALCOHOL_WINE_WHITE_MTH_2_1 = self.fake.random_int(min=0, max=999)
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                ALCOHOL_BEER_MTH_2_1 = generate_code(
                    self.fake, "ALCOHOL_BEER_MTH_2_1", enforce_numeric_codes=True
                )
            else:
                ALCOHOL_BEER_MTH_2_1 = self.fake.random_int(min=0, max=999)
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                ALCOHOL_SPIRITS_MTH_2_1 = generate_code(
                    self.fake, "ALCOHOL_SPIRITS_MTH_2_1", enforce_numeric_codes=True
                )
            else:
                ALCOHOL_SPIRITS_MTH_2_1 = self.fake.random_int(min=0, max=999)
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                ALCOHOL_WINE_FORT_MTH_2_1 = generate_code(
                    self.fake, "ALCOHOL_WINE_FORT_MTH_2_1", enforce_numeric_codes=True
                )
            else:
                ALCOHOL_WINE_FORT_MTH_2_1 = self.fake.random_int(min=0, max=999)
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                ALCOHOL_OTHER_MTH_2_1 = generate_code(
                    self.fake, "ALCOHOL_OTHER_MTH_2_1", enforce_numeric_codes=True
                )
            else:
                ALCOHOL_OTHER_MTH_2_1 = self.fake.random_int(min=0, max=999)

        if ALCOHOL_CURR_1_1 in (1, 2, 3):
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                ALCOHOL_WINE_RED_WK_1_1 = generate_code(
                    self.fake, "ALCOHOL_WINE_RED_WK_1_1", enforce_numeric_codes=True
                )
            else:
                ALCOHOL_WINE_RED_WK_1_1 = self.fake.random_int(min=0, max=999)
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                ALCOHOL_WINE_WHITE_WK_1_1 = generate_code(
                    self.fake, "ALCOHOL_WINE_WHITE_WK_1_1", enforce_numeric_codes=True
                )
            else:
                ALCOHOL_WINE_WHITE_WK_1_1 = self.fake.random_int(min=0, max=999)
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                ALCOHOL_BEER_WK_1_1 = generate_code(
                    self.fake, "ALCOHOL_BEER_WK_1_1", enforce_numeric_codes=True
                )
            else:
                ALCOHOL_BEER_WK_1_1 = self.fake.random_int(min=0, max=999)
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                ALCOHOL_SPIRITS_WK_1_1 = generate_code(
                    self.fake, "ALCOHOL_SPIRITS_WK_1_1", enforce_numeric_codes=True
                )
            else:
                ALCOHOL_SPIRITS_WK_1_1 = self.fake.random_int(min=0, max=999)
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                ALCOHOL_WINE_FORT_WK_1_1 = generate_code(
                    self.fake, "ALCOHOL_WINE_FORT_WK_1_1", enforce_numeric_codes=True
                )
            else:
                ALCOHOL_WINE_FORT_WK_1_1 = self.fake.random_int(min=0, max=999)
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                ALCOHOL_OTHER_WK_1_1 = generate_code(
                    self.fake, "ALCOHOL_OTHER_WK_1_1", enforce_numeric_codes=True
                )
            else:
                ALCOHOL_OTHER_WK_1_1 = self.fake.random_int(min=0, max=999)

        if ALCOHOL_CURR_1_1 in (1, 2, 3, 4, 5):
            ALCOHOL_FOOD_1_1 = generate_code(
                self.fake, "ALCOHOL_FOOD_1_1", enforce_numeric_codes=True
            )
            ALCOHOL_CHG_1_1 = generate_code(
                self.fake, "ALCOHOL_CHG_1_1", enforce_numeric_codes=True
            )

            if ALCOHOL_CHG_1_1 == 3:
                ALCOHOL_CHG_REDUCE_REASON_2_M = generate_codes(
                    self.fake,
                    "ALCOHOL_CHG_REDUCE_REASON_2_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

        if ALCOHOL_CURR_1_1 == 6 and ALCOHOL_PREV_1_1 == 1:
            ALCOHOL_CHG_ABST_REASON_2_M = generate_codes(
                self.fake,
                "ALCOHOL_CHG_ABST_REASON_2_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        # 4. Family health history
        BIRTH_PLACE_1_1 = None
        IMMIGRATE_UK_YR_1_1 = None
        ADOPTION_STATUS_1_1 = None
        FATHER_ALIVE_1_1 = None
        FATHER_AGE_1_1 = None
        FATHER_AGE_DECEASED_1_1 = None
        FATHER_DIAG_A_2_M = None
        FATHER_DIAG_AUTO_1_M = None
        FATHER_DIAG_ANAEMIA_1_M = None
        FATHER_DIAG_CANCER_1_M = None
        FATHER_DIAG_CANCER_SKIN_1_M = None
        FATHER_DIAG_GASTRO_1_M = None
        FATHER_DIAG_ENDOCR_1_M = None
        FATHER_DIAG_OPTHAL_1_M = None
        FATHER_DIAG_OSTEO_1_M = None
        FATHER_DIAG_CVD_1_M = None
        FATHER_DIAG_UROL_1_M = None
        FATHER_DIAG_RESP_1_M = None
        FATHER_DIAG_PSYCH_1_M = None
        FATHER_DIAG_PSYCH_ANX_1_M = None
        FATHER_DIAG_PSYCH_DEPR_1_M = None
        FATHER_DIAG_PSYCH_EAT_1_M = None
        FATHER_DIAG_NEURO_DEV_1_M = None
        FATHER_DIAG_NEURO_1_M = None
        FATHER_DIAG_REPRO_1_M = None
        MOTHER_ALIVE_1_1 = None
        MOTHER_AGE_1_1 = None
        MOTHER_AGE_DECEASED_1_1 = None
        MOTHER_DIAG_A_2_M = None
        MOTHER_DIAG_AUTO_1_M = None
        MOTHER_DIAG_ANAEMIA_1_M = None
        MOTHER_DIAG_CANCER_1_M = None
        MOTHER_DIAG_CANCER_SKIN_1_M = None
        MOTHER_DIAG_GASTRO_1_M = None
        MOTHER_DIAG_ENDOCR_1_M = None
        MOTHER_DIAG_OPTHAL_1_M = None
        MOTHER_DIAG_OSTEO_1_M = None
        MOTHER_DIAG_CVD_1_M = None
        MOTHER_DIAG_UROL_1_M = None
        MOTHER_DIAG_RESP_1_M = None
        MOTHER_DIAG_PSYCH_1_M = None
        MOTHER_DIAG_PSYCH_ANX_1_M = None
        MOTHER_DIAG_PSYCH_DEPR_1_M = None
        MOTHER_DIAG_PSYCH_EAT_1_M = None
        MOTHER_DIAG_NEURO_DEV_1_M = None
        MOTHER_DIAG_NEURO_1_M = None
        MOTHER_DIAG_REPRO_1_M = None
        SIBLING_NUM_BROTHERS_1_1 = None
        SIBLING_NUM_SISTERS_1_1 = None
        SIBLING_DIAG_A_2_M = None
        SIBLING_DIAG_AUTO_1_M = None
        SIBLING_DIAG_ANAEMIA_1_M = None
        SIBLING_DIAG_CANCER_1_M = None
        SIBLING_DIAG_CANCER_SKIN_1_M = None
        SIBLING_DIAG_GASTRO_1_M = None
        SIBLING_DIAG_ENDOCR_1_M = None
        SIBLING_DIAG_OPTHAL_1_M = None
        SIBLING_DIAG_OSTEO_1_M = None
        SIBLING_DIAG_CVD_1_M = None
        SIBLING_DIAG_UROL_1_M = None
        SIBLING_DIAG_RESP_1_M = None
        SIBLING_DIAG_PSYCH_1_M = None
        SIBLING_DIAG_PSYCH_ANX_1_M = None
        SIBLING_DIAG_PSYCH_DEPR_1_M = None
        SIBLING_DIAG_PSYCH_EAT_1_M = None
        SIBLING_DIAG_NEURO_DEV_1_M = None
        SIBLING_DIAG_NEURO_1_M = None
        SIBLING_DIAG_REPRO_1_M = None

        BIRTH_PLACE_1_1 = generate_code(
            self.fake, "BIRTH_PLACE_1_1", enforce_numeric_codes=True
        )

        if BIRTH_PLACE_1_1 in (6, 7, 8, 9, 10):
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                IMMIGRATE_UK_YR_1_1 = generate_code(
                    self.fake, "IMMIGRATE_UK_YR_1_1", enforce_numeric_codes=True
                )
            else:
                IMMIGRATE_UK_YR_1_1 = self.fake.random_int(
                    min=birth_date.year, max=SUBMISSION_DATE.year
                )

        ADOPTION_STATUS_1_1 = generate_code(
            self.fake, "ADOPTION_STATUS_1_1", enforce_numeric_codes=True
        )

        FATHER_ALIVE_1_1 = generate_code(
            self.fake, "FATHER_ALIVE_1_1", enforce_numeric_codes=True
        )

        if FATHER_ALIVE_1_1 == 1:
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                FATHER_AGE_1_1 = generate_code(
                    self.fake, "FATHER_AGE_1_1", enforce_numeric_codes=True
                )
            else:
                FATHER_AGE_1_1 = self.fake.random_int(min=current_age + 1, max=122)

        if FATHER_ALIVE_1_1 == 0:
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                FATHER_AGE_DECEASED_1_1 = generate_code(
                    self.fake, "FATHER_AGE_DECEASED_1_1", enforce_numeric_codes=True
                )
            else:
                FATHER_AGE_DECEASED_1_1 = self.fake.random_int(min=10, max=122)

        FATHER_DIAG_A_2_M = generate_codes(
            self.fake,
            "FATHER_DIAG_A_2_M",
            exclusive_codes=ExclusiveCodes(
                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
            ),
            enforce_numeric_codes=True,
        )

        if 1 in FATHER_DIAG_A_2_M:
            FATHER_DIAG_AUTO_1_M = generate_codes(
                self.fake,
                "FATHER_DIAG_AUTO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 2 in FATHER_DIAG_A_2_M:
            FATHER_DIAG_ANAEMIA_1_M = generate_codes(
                self.fake,
                "FATHER_DIAG_ANAEMIA_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 3 in FATHER_DIAG_A_2_M:
            FATHER_DIAG_CANCER_1_M = generate_codes(
                self.fake,
                "FATHER_DIAG_CANCER_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE,
                    special_non_exclusive_codes=[-1],
                ),
                enforce_numeric_codes=True,
            )

            if 18 in FATHER_DIAG_CANCER_1_M:
                FATHER_DIAG_CANCER_SKIN_1_M = generate_codes(
                    self.fake,
                    "FATHER_DIAG_CANCER_SKIN_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

        if 4 in FATHER_DIAG_A_2_M:
            FATHER_DIAG_GASTRO_1_M = generate_codes(
                self.fake,
                "FATHER_DIAG_GASTRO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 5 in FATHER_DIAG_A_2_M:
            FATHER_DIAG_ENDOCR_1_M = generate_codes(
                self.fake,
                "FATHER_DIAG_ENDOCR_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 6 in FATHER_DIAG_A_2_M:
            FATHER_DIAG_OPTHAL_1_M = generate_codes(
                self.fake,
                "FATHER_DIAG_OPTHAL_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 7 in FATHER_DIAG_A_2_M:
            FATHER_DIAG_OSTEO_1_M = generate_codes(
                self.fake,
                "FATHER_DIAG_OSTEO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 8 in FATHER_DIAG_A_2_M:
            FATHER_DIAG_CVD_1_M = generate_codes(
                self.fake,
                "FATHER_DIAG_CVD_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 9 in FATHER_DIAG_A_2_M:
            FATHER_DIAG_UROL_1_M = generate_codes(
                self.fake,
                "FATHER_DIAG_UROL_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 10 in FATHER_DIAG_A_2_M:
            FATHER_DIAG_RESP_1_M = generate_codes(
                self.fake,
                "FATHER_DIAG_RESP_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 11 in FATHER_DIAG_A_2_M:
            FATHER_DIAG_PSYCH_1_M = generate_codes(
                self.fake,
                "FATHER_DIAG_PSYCH_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

            if 1 in FATHER_DIAG_PSYCH_1_M:
                FATHER_DIAG_PSYCH_ANX_1_M = generate_codes(
                    self.fake,
                    "FATHER_DIAG_PSYCH_ANX_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 4 in FATHER_DIAG_PSYCH_1_M:
                FATHER_DIAG_PSYCH_DEPR_1_M = generate_codes(
                    self.fake,
                    "FATHER_DIAG_PSYCH_DEPR_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 8 in FATHER_DIAG_PSYCH_1_M:
                FATHER_DIAG_PSYCH_EAT_1_M = generate_codes(
                    self.fake,
                    "FATHER_DIAG_PSYCH_EAT_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

        if 12 in FATHER_DIAG_A_2_M:
            FATHER_DIAG_NEURO_DEV_1_M = generate_codes(
                self.fake,
                "FATHER_DIAG_NEURO_DEV_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 13 in FATHER_DIAG_A_2_M:
            FATHER_DIAG_NEURO_1_M = generate_codes(
                self.fake,
                "FATHER_DIAG_NEURO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 14 in FATHER_DIAG_A_2_M:
            FATHER_DIAG_REPRO_1_M = generate_codes(
                self.fake,
                "FATHER_DIAG_REPRO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        # NOTE: source questionnaire_logic.csv has MOTHER_ALIVE_1_1 and MOTHER_AGE_1_1's
        # question_type/show_if swapped relative to the equivalent FATHER_ALIVE_1_1 /
        # FATHER_AGE_1_1 pair. Treating MOTHER_ALIVE_1_1 as core (like FATHER_ALIVE_1_1) and
        # MOTHER_AGE_1_1 as dynamic on it (like FATHER_AGE_1_1) to match.
        MOTHER_ALIVE_1_1 = generate_code(
            self.fake, "MOTHER_ALIVE_1_1", enforce_numeric_codes=True
        )

        if MOTHER_ALIVE_1_1 == 1:
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                MOTHER_AGE_1_1 = generate_code(
                    self.fake, "MOTHER_AGE_1_1", enforce_numeric_codes=True
                )
            else:
                MOTHER_AGE_1_1 = self.fake.random_int(min=current_age + 1, max=122)

        if MOTHER_ALIVE_1_1 == 0:
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                MOTHER_AGE_DECEASED_1_1 = generate_code(
                    self.fake, "MOTHER_AGE_DECEASED_1_1", enforce_numeric_codes=True
                )
            else:
                MOTHER_AGE_DECEASED_1_1 = self.fake.random_int(min=10, max=122)

        MOTHER_DIAG_A_2_M = generate_codes(
            self.fake,
            "MOTHER_DIAG_A_2_M",
            exclusive_codes=ExclusiveCodes(
                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
            ),
            enforce_numeric_codes=True,
        )

        if 1 in MOTHER_DIAG_A_2_M:
            MOTHER_DIAG_AUTO_1_M = generate_codes(
                self.fake,
                "MOTHER_DIAG_AUTO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 2 in MOTHER_DIAG_A_2_M:
            MOTHER_DIAG_ANAEMIA_1_M = generate_codes(
                self.fake,
                "MOTHER_DIAG_ANAEMIA_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 3 in MOTHER_DIAG_A_2_M:
            MOTHER_DIAG_CANCER_1_M = generate_codes(
                self.fake,
                "MOTHER_DIAG_CANCER_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE,
                    special_non_exclusive_codes=[-1],
                ),
                enforce_numeric_codes=True,
            )

            if 18 in MOTHER_DIAG_CANCER_1_M:
                MOTHER_DIAG_CANCER_SKIN_1_M = generate_codes(
                    self.fake,
                    "MOTHER_DIAG_CANCER_SKIN_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

        if 4 in MOTHER_DIAG_A_2_M:
            MOTHER_DIAG_GASTRO_1_M = generate_codes(
                self.fake,
                "MOTHER_DIAG_GASTRO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 5 in MOTHER_DIAG_A_2_M:
            MOTHER_DIAG_ENDOCR_1_M = generate_codes(
                self.fake,
                "MOTHER_DIAG_ENDOCR_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 6 in MOTHER_DIAG_A_2_M:
            MOTHER_DIAG_OPTHAL_1_M = generate_codes(
                self.fake,
                "MOTHER_DIAG_OPTHAL_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 7 in MOTHER_DIAG_A_2_M:
            MOTHER_DIAG_OSTEO_1_M = generate_codes(
                self.fake,
                "MOTHER_DIAG_OSTEO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 8 in MOTHER_DIAG_A_2_M:
            MOTHER_DIAG_CVD_1_M = generate_codes(
                self.fake,
                "MOTHER_DIAG_CVD_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 9 in MOTHER_DIAG_A_2_M:
            MOTHER_DIAG_UROL_1_M = generate_codes(
                self.fake,
                "MOTHER_DIAG_UROL_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 10 in MOTHER_DIAG_A_2_M:
            MOTHER_DIAG_RESP_1_M = generate_codes(
                self.fake,
                "MOTHER_DIAG_RESP_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 11 in MOTHER_DIAG_A_2_M:
            MOTHER_DIAG_PSYCH_1_M = generate_codes(
                self.fake,
                "MOTHER_DIAG_PSYCH_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

            if 1 in MOTHER_DIAG_PSYCH_1_M:
                MOTHER_DIAG_PSYCH_ANX_1_M = generate_codes(
                    self.fake,
                    "MOTHER_DIAG_PSYCH_ANX_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 4 in MOTHER_DIAG_PSYCH_1_M:
                MOTHER_DIAG_PSYCH_DEPR_1_M = generate_codes(
                    self.fake,
                    "MOTHER_DIAG_PSYCH_DEPR_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 8 in MOTHER_DIAG_PSYCH_1_M:
                MOTHER_DIAG_PSYCH_EAT_1_M = generate_codes(
                    self.fake,
                    "MOTHER_DIAG_PSYCH_EAT_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

        if 12 in MOTHER_DIAG_A_2_M:
            MOTHER_DIAG_NEURO_DEV_1_M = generate_codes(
                self.fake,
                "MOTHER_DIAG_NEURO_DEV_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 13 in MOTHER_DIAG_A_2_M:
            MOTHER_DIAG_NEURO_1_M = generate_codes(
                self.fake,
                "MOTHER_DIAG_NEURO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 14 in MOTHER_DIAG_A_2_M:
            MOTHER_DIAG_REPRO_1_M = generate_codes(
                self.fake,
                "MOTHER_DIAG_REPRO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
            SIBLING_NUM_BROTHERS_1_1 = generate_code(
                self.fake, "SIBLING_NUM_BROTHERS_1_1", enforce_numeric_codes=True
            )
        else:
            SIBLING_NUM_BROTHERS_1_1 = self.fake.random_int(min=0, max=25)

        if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
            SIBLING_NUM_SISTERS_1_1 = generate_code(
                self.fake, "SIBLING_NUM_SISTERS_1_1", enforce_numeric_codes=True
            )
        else:
            SIBLING_NUM_SISTERS_1_1 = self.fake.random_int(min=0, max=25)

        if SIBLING_NUM_BROTHERS_1_1 > 0 or SIBLING_NUM_SISTERS_1_1 > 0:
            SIBLING_DIAG_A_2_M = generate_codes(
                self.fake,
                "SIBLING_DIAG_A_2_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

            if 1 in SIBLING_DIAG_A_2_M:
                SIBLING_DIAG_AUTO_1_M = generate_codes(
                    self.fake,
                    "SIBLING_DIAG_AUTO_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 2 in SIBLING_DIAG_A_2_M:
                SIBLING_DIAG_ANAEMIA_1_M = generate_codes(
                    self.fake,
                    "SIBLING_DIAG_ANAEMIA_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 3 in SIBLING_DIAG_A_2_M:
                SIBLING_DIAG_CANCER_1_M = generate_codes(
                    self.fake,
                    "SIBLING_DIAG_CANCER_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

                if 18 in SIBLING_DIAG_CANCER_1_M:
                    SIBLING_DIAG_CANCER_SKIN_1_M = generate_codes(
                        self.fake,
                        "SIBLING_DIAG_CANCER_SKIN_1_M",
                        exclusive_codes=ExclusiveCodes(
                            exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                        ),
                        enforce_numeric_codes=True,
                    )

            if 4 in SIBLING_DIAG_A_2_M:
                SIBLING_DIAG_GASTRO_1_M = generate_codes(
                    self.fake,
                    "SIBLING_DIAG_GASTRO_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 5 in SIBLING_DIAG_A_2_M:
                SIBLING_DIAG_ENDOCR_1_M = generate_codes(
                    self.fake,
                    "SIBLING_DIAG_ENDOCR_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 6 in SIBLING_DIAG_A_2_M:
                SIBLING_DIAG_OPTHAL_1_M = generate_codes(
                    self.fake,
                    "SIBLING_DIAG_OPTHAL_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 7 in SIBLING_DIAG_A_2_M:
                SIBLING_DIAG_OSTEO_1_M = generate_codes(
                    self.fake,
                    "SIBLING_DIAG_OSTEO_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 8 in SIBLING_DIAG_A_2_M:
                SIBLING_DIAG_CVD_1_M = generate_codes(
                    self.fake,
                    "SIBLING_DIAG_CVD_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 9 in SIBLING_DIAG_A_2_M:
                SIBLING_DIAG_UROL_1_M = generate_codes(
                    self.fake,
                    "SIBLING_DIAG_UROL_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 10 in SIBLING_DIAG_A_2_M:
                SIBLING_DIAG_RESP_1_M = generate_codes(
                    self.fake,
                    "SIBLING_DIAG_RESP_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 11 in SIBLING_DIAG_A_2_M:
                SIBLING_DIAG_PSYCH_1_M = generate_codes(
                    self.fake,
                    "SIBLING_DIAG_PSYCH_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

                if 1 in SIBLING_DIAG_PSYCH_1_M:
                    SIBLING_DIAG_PSYCH_ANX_1_M = generate_codes(
                        self.fake,
                        "SIBLING_DIAG_PSYCH_ANX_1_M",
                        exclusive_codes=ExclusiveCodes(
                            exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                        ),
                        enforce_numeric_codes=True,
                    )

                if 4 in SIBLING_DIAG_PSYCH_1_M:
                    SIBLING_DIAG_PSYCH_DEPR_1_M = generate_codes(
                        self.fake,
                        "SIBLING_DIAG_PSYCH_DEPR_1_M",
                        exclusive_codes=ExclusiveCodes(
                            exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                        ),
                        enforce_numeric_codes=True,
                    )

                if 8 in SIBLING_DIAG_PSYCH_1_M:
                    SIBLING_DIAG_PSYCH_EAT_1_M = generate_codes(
                        self.fake,
                        "SIBLING_DIAG_PSYCH_EAT_1_M",
                        exclusive_codes=ExclusiveCodes(
                            exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                        ),
                        enforce_numeric_codes=True,
                    )

            if 12 in SIBLING_DIAG_A_2_M:
                SIBLING_DIAG_NEURO_DEV_1_M = generate_codes(
                    self.fake,
                    "SIBLING_DIAG_NEURO_DEV_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 13 in SIBLING_DIAG_A_2_M:
                SIBLING_DIAG_NEURO_1_M = generate_codes(
                    self.fake,
                    "SIBLING_DIAG_NEURO_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 14 in SIBLING_DIAG_A_2_M:
                SIBLING_DIAG_REPRO_1_M = generate_codes(
                    self.fake,
                    "SIBLING_DIAG_REPRO_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

        # 5. Your health history
        HEALTH_STATUS_CURR_1_1 = None
        HEALTH_STATUS_CHRONIC_1_1 = None
        HEALTH_STATUS_DISABILITY_SUPPORT_1_M = None
        HEALTH_STATUS_PRIVATE_HEALTHCARE_1_1 = None
        HEALTH_COVID_1_1 = None
        HEALTH_SUN_PROTECT_1_1 = None
        HEALTH_DENTAL_1_M = None
        HEALTH_FALLS_1_1 = None
        HEALTH_WEIGHT_CHG_1_1 = None
        HEALTH_RESP_WHEEZE_1_1 = None
        HEALTH_RESP_SHORT_1_1 = None
        HEALTH_PAIN_LEG_1_1 = None
        HEALTH_AMPUTATION_1_1 = None
        HEALTH_PAIN_ACUTE_2_M = None
        HEALTH_PAIN_CHRONIC_1_M = None
        HEALTH_PAIN_CHEST_1_1 = None
        HEALTH_PAIN_CHEST_WALK_1_1 = None
        HEALTH_PAIN_CHEST_WALK_UPHILL_1_1 = None
        HEALTH_PAIN_CHEST_SUBSIDE_1_1 = None
        HEALTH_CHECK_COLORECTAL_1_1 = None
        HEALTH_CHECK_COLORECTAL_YRS_1_1 = None
        HEALTH_CHECK_PROSTATE_1_1 = None
        HEALTH_CHECK_PROSTATE_YRS_1_1 = None
        CHILDREN_BIO_NUM_2_1 = None
        CHILDREN_BIO_FIRST_AGE_1_1 = None
        CHILDREN_BIO_LAST_AGE_1_1 = None
        HEALTH_CHECK_MAMMOGRAM_1_1 = None
        HEALTH_CHECK_MAMMOGRAM_YRS_1_1 = None
        HEALTH_CHECK_SMEAR_1_1 = None
        HEALTH_CHECK_SMEAR_YRS_1_1 = None
        GYN_MENSTR_AGE_1_1 = None
        GYN_MENOPAUSE_2_1 = None
        GYN_MENOPAUSE_LAST_PERIOD_AGE_2_1 = None
        GYN_MENSTR_LAST_PERIOD_DAYS_2_1 = None
        GYN_MENSTR_CYCLE_DAYS_2_1 = None
        CHILDREN_BIRTHED_NUM_1_1 = None
        CHILDREN_BIRTHED_FIRST_AGE_1_1 = None
        CHILDREN_BIRTHED_LAST_AGE_1_1 = None
        GYN_CONTRACEPT_IMPLANT_1_1 = None
        GYN_CONTRACEPT_METHODS_1_M = None
        GYN_CONTRACEPT_PILL_FIRST_AGE_1_1 = None
        GYN_CONTRACEPT_PILL_LAST_AGE_1_1 = None
        GYN_HRT_1_1 = None
        GYN_HRT_FIRST_TRT_AGE_1_1 = None
        GYN_HRT_LAST_TRT_AGE_1_1 = None
        GYN_HYST_1_1 = None
        GYN_HYST_AGE_1_1 = None
        GYN_OOPH_1_1 = None
        GYN_OOPH_AGE_1_1 = None
        DIAG_2_M = None
        DIAG_AUTO_1_M = None
        DIAG_ANAEMIA_1_M = None
        DIAG_CANCER_1_M = None
        DIAG_CANCER_SKIN_1_M = None
        DIAG_OB_1_M = None
        DIAG_GASTRO_1_M = None
        DIAG_ENDOCR_1_M = None
        DIAG_OPTHAL_1_M = None
        DIAG_OSTEO_1_M = None
        DIAG_CVD_1_M = None
        DIAG_UROL_1_M = None
        DIAG_RESP_1_M = None
        DIAG_PSYCH_1_M = None
        DIAG_PSYCH_ANX_1_M = None
        DIAG_PSYCH_DEPR_1_M = None
        DIAG_PSYCH_EAT_1_M = None
        DIAG_NEURO_DEV_1_M = None
        DIAG_NEURO_1_M = None
        DIAG_REPRO_1_M = None
        MEDICAT_1_M = None
        MEDICAT_AUTO_1_M = None
        MEDICAT_OSTEO_1_M = None
        MEDICAT_CANCER_1_M = None
        MEDICAT_DIAB_1_M = None
        MEDICAT_GASTRO_1_M = None
        MEDICAT_ENDOCR_1_M = None
        MEDICAT_CVD_1_M = None
        MEDICAT_RESP_1_M = None
        MEDICAT_PSYCH_1_M = None
        MEDICAT_PSYCH_ANTIDEPR_1_M = None
        MEDICAT_PSYCH_ANTIPSYCH_1_M = None
        MEDICAT_NEURO_1_M = None
        MEDICAT_PAIN_1_M = None
        MEDICAT_REPRO_1_M = None
        MEDICAT_REPRO_CONTRACEPT_1_M = None
        MEDICAT_SUPPL_1_M = None
        SKIP_PHQ9_GAD7_1_1 = None
        PHQ9_ITEM1_INTEREST_1_1 = None
        PHQ9_ITEM2_DOWN_1_1 = None
        PHQ9_ITEM3_SLEEP_1_1 = None
        PHQ9_ITEM4_ENERGY_1_1 = None
        PHQ9_ITEM5_APPETITE_1_1 = None
        PHQ9_ITEM6_BAD_1_1 = None
        PHQ9_ITEM7_CONCENTR_1_1 = None
        PHQ9_ITEM8_MOVEMENT_1_1 = None
        PHQ9_ITEM9_HARM_1_1 = None
        PHQ9_IMPAIR_1_1 = None
        GAD7_ITEM1_ANX_1_1 = None
        GAD7_ITEM2_WORRY_CONTROL_1_1 = None
        GAD7_ITEM3_WORRY_AMOUNT_1_1 = None
        GAD7_ITEM4_RELAX_1_1 = None
        GAD7_ITEM5_RESTLESS_1_1 = None
        GAD7_ITEM6_ANNOYED_1_1 = None
        GAD7_ITEM7_AFRAID_1_1 = None
        GAD7_IMPAIR_1_1 = None

        HEALTH_STATUS_CURR_1_1 = generate_code(
            self.fake, "HEALTH_STATUS_CURR_1_1", enforce_numeric_codes=True
        )
        HEALTH_STATUS_CHRONIC_1_1 = generate_code(
            self.fake, "HEALTH_STATUS_CHRONIC_1_1", enforce_numeric_codes=True
        )

        if HEALTH_STATUS_CHRONIC_1_1 in (1, -1, -3):
            HEALTH_STATUS_DISABILITY_SUPPORT_1_M = generate_codes(
                self.fake,
                "HEALTH_STATUS_DISABILITY_SUPPORT_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        HEALTH_STATUS_PRIVATE_HEALTHCARE_1_1 = generate_code(
            self.fake,
            "HEALTH_STATUS_PRIVATE_HEALTHCARE_1_1",
            enforce_numeric_codes=True,
        )

        HEALTH_COVID_1_1 = generate_code(
            self.fake, "HEALTH_COVID_1_1", enforce_numeric_codes=True
        )

        HEALTH_SUN_PROTECT_1_1 = generate_code(
            self.fake, "HEALTH_SUN_PROTECT_1_1", enforce_numeric_codes=True
        )

        HEALTH_DENTAL_1_M = generate_codes(
            self.fake,
            "HEALTH_DENTAL_1_M",
            exclusive_codes=ExclusiveCodes(
                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
            ),
            enforce_numeric_codes=True,
        )

        HEALTH_FALLS_1_1 = generate_code(
            self.fake, "HEALTH_FALLS_1_1", enforce_numeric_codes=True
        )

        HEALTH_WEIGHT_CHG_1_1 = generate_code(
            self.fake, "HEALTH_WEIGHT_CHG_1_1", enforce_numeric_codes=True
        )

        HEALTH_RESP_WHEEZE_1_1 = generate_code(
            self.fake, "HEALTH_RESP_WHEEZE_1_1", enforce_numeric_codes=True
        )

        if 0 <= ACTIVITY_WALK_DAYS_2_1 <= 7 or ACTIVITY_WALK_DAYS_2_1 in (-3, -1):
            HEALTH_RESP_SHORT_1_1 = generate_code(
                self.fake, "HEALTH_RESP_SHORT_1_1", enforce_numeric_codes=True
            )
            HEALTH_PAIN_LEG_1_1 = generate_code(
                self.fake, "HEALTH_PAIN_LEG_1_1", enforce_numeric_codes=True
            )

        HEALTH_AMPUTATION_1_1 = generate_code(
            self.fake, "HEALTH_AMPUTATION_1_1", enforce_numeric_codes=True
        )

        HEALTH_PAIN_ACUTE_2_M = generate_codes(
            self.fake,
            "HEALTH_PAIN_ACUTE_2_M",
            exclusive_codes=ExclusiveCodes(
                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
            ),
            enforce_numeric_codes=True,
        )

        HEALTH_PAIN_CHRONIC_1_M = generate_codes(
            self.fake,
            "HEALTH_PAIN_CHRONIC_1_M",
            exclusive_codes=ExclusiveCodes(
                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
            ),
            enforce_numeric_codes=True,
        )

        HEALTH_PAIN_CHEST_1_1 = generate_code(
            self.fake, "HEALTH_PAIN_CHEST_1_1", enforce_numeric_codes=True
        )

        if HEALTH_PAIN_CHEST_1_1 == 1:
            HEALTH_PAIN_CHEST_WALK_1_1 = generate_code(
                self.fake, "HEALTH_PAIN_CHEST_WALK_1_1", enforce_numeric_codes=True
            )

            if HEALTH_PAIN_CHEST_WALK_1_1 == 0:
                HEALTH_PAIN_CHEST_WALK_UPHILL_1_1 = generate_code(
                    self.fake,
                    "HEALTH_PAIN_CHEST_WALK_UPHILL_1_1",
                    enforce_numeric_codes=True,
                )

            # NOTE: source questionnaire_logic.csv's show_if for this field has one unbalanced
            # trailing ')'. Dropped it; the resulting condition is a sensible mirror of the
            # walking/uphill branching used by the two questions above it.
            if (
                HEALTH_PAIN_CHEST_WALK_1_1 == 1
                and HEALTH_PAIN_CHEST_WALK_UPHILL_1_1 is None
            ) or (
                HEALTH_PAIN_CHEST_WALK_1_1 == 0
                and HEALTH_PAIN_CHEST_WALK_UPHILL_1_1 == 1
            ):
                HEALTH_PAIN_CHEST_SUBSIDE_1_1 = generate_code(
                    self.fake,
                    "HEALTH_PAIN_CHEST_SUBSIDE_1_1",
                    enforce_numeric_codes=True,
                )

        HEALTH_CHECK_COLORECTAL_1_1 = generate_code(
            self.fake, "HEALTH_CHECK_COLORECTAL_1_1", enforce_numeric_codes=True
        )

        if HEALTH_CHECK_COLORECTAL_1_1 == 1:
            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                HEALTH_CHECK_COLORECTAL_YRS_1_1 = generate_code(
                    self.fake,
                    "HEALTH_CHECK_COLORECTAL_YRS_1_1",
                    enforce_numeric_codes=True,
                )
            else:
                HEALTH_CHECK_COLORECTAL_YRS_1_1 = self.fake.random_int(
                    min=0, max=current_age
                )

        if DEMOG_SEX_2_1 in (1, 3, -3):
            HEALTH_CHECK_PROSTATE_1_1 = generate_code(
                self.fake, "HEALTH_CHECK_PROSTATE_1_1", enforce_numeric_codes=True
            )

            if HEALTH_CHECK_PROSTATE_1_1 == 1:
                if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                    HEALTH_CHECK_PROSTATE_YRS_1_1 = generate_code(
                        self.fake,
                        "HEALTH_CHECK_PROSTATE_YRS_1_1",
                        enforce_numeric_codes=True,
                    )
                else:
                    HEALTH_CHECK_PROSTATE_YRS_1_1 = self.fake.random_int(
                        min=0, max=current_age
                    )

            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                CHILDREN_BIO_NUM_2_1 = generate_code(
                    self.fake, "CHILDREN_BIO_NUM_2_1", enforce_numeric_codes=True
                )
            else:
                CHILDREN_BIO_NUM_2_1 = self.fake.random_int(min=0, max=200)

            if CHILDREN_BIO_NUM_2_1 > 1 or CHILDREN_BIO_NUM_2_1 in (-1, -3, -999):
                if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                    CHILDREN_BIO_FIRST_AGE_1_1 = generate_code(
                        self.fake,
                        "CHILDREN_BIO_FIRST_AGE_1_1",
                        enforce_numeric_codes=True,
                    )
                else:
                    CHILDREN_BIO_FIRST_AGE_1_1 = self.fake.random_int(
                        min=8, max=current_age
                    )

            if CHILDREN_BIO_NUM_2_1 > 1 or CHILDREN_BIO_NUM_2_1 in (-1, -3, -999):
                if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                    CHILDREN_BIO_LAST_AGE_1_1 = generate_code(
                        self.fake,
                        "CHILDREN_BIO_LAST_AGE_1_1",
                        enforce_numeric_codes=True,
                    )
                else:
                    CHILDREN_BIO_LAST_AGE_1_1 = self.fake.random_int(
                        min=8, max=current_age
                    )

        if DEMOG_SEX_2_1 in (2, 3, -3):
            HEALTH_CHECK_MAMMOGRAM_1_1 = generate_code(
                self.fake, "HEALTH_CHECK_MAMMOGRAM_1_1", enforce_numeric_codes=True
            )

            if HEALTH_CHECK_MAMMOGRAM_1_1 == 1:
                if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                    HEALTH_CHECK_MAMMOGRAM_YRS_1_1 = generate_code(
                        self.fake,
                        "HEALTH_CHECK_MAMMOGRAM_YRS_1_1",
                        enforce_numeric_codes=True,
                    )
                else:
                    HEALTH_CHECK_MAMMOGRAM_YRS_1_1 = self.fake.random_int(
                        min=0, max=current_age
                    )

            HEALTH_CHECK_SMEAR_1_1 = generate_code(
                self.fake, "HEALTH_CHECK_SMEAR_1_1", enforce_numeric_codes=True
            )

            if HEALTH_CHECK_SMEAR_1_1 == 1:
                if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                    HEALTH_CHECK_SMEAR_YRS_1_1 = generate_code(
                        self.fake,
                        "HEALTH_CHECK_SMEAR_YRS_1_1",
                        enforce_numeric_codes=True,
                    )
                else:
                    HEALTH_CHECK_SMEAR_YRS_1_1 = self.fake.random_int(
                        min=0, max=current_age
                    )

            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                GYN_MENSTR_AGE_1_1 = generate_code(
                    self.fake, "GYN_MENSTR_AGE_1_1", enforce_numeric_codes=True
                )
            else:
                GYN_MENSTR_AGE_1_1 = self.fake.random_int(min=5, max=current_age)

            GYN_MENOPAUSE_2_1 = generate_code(
                self.fake, "GYN_MENOPAUSE_2_1", enforce_numeric_codes=True
            )

            if GYN_MENOPAUSE_2_1 == 1:
                if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                    GYN_MENOPAUSE_LAST_PERIOD_AGE_2_1 = generate_code(
                        self.fake,
                        "GYN_MENOPAUSE_LAST_PERIOD_AGE_2_1",
                        enforce_numeric_codes=True,
                    )
                else:
                    GYN_MENOPAUSE_LAST_PERIOD_AGE_2_1 = self.fake.random_int(
                        min=GYN_MENSTR_AGE_1_1, max=current_age
                    )

            if GYN_MENOPAUSE_2_1 in (0, 3):
                if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                    GYN_MENSTR_LAST_PERIOD_DAYS_2_1 = generate_code(
                        self.fake,
                        "GYN_MENSTR_LAST_PERIOD_DAYS_2_1",
                        enforce_numeric_codes=True,
                    )
                else:
                    GYN_MENSTR_LAST_PERIOD_DAYS_2_1 = self.fake.random_int(
                        min=0, max=365
                    )
                if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                    GYN_MENSTR_CYCLE_DAYS_2_1 = generate_code(
                        self.fake,
                        "GYN_MENSTR_CYCLE_DAYS_2_1",
                        enforce_numeric_codes=True,
                    )
                else:
                    GYN_MENSTR_CYCLE_DAYS_2_1 = self.fake.random_int(min=7, max=365)

            if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                CHILDREN_BIRTHED_NUM_1_1 = generate_code(
                    self.fake, "CHILDREN_BIRTHED_NUM_1_1", enforce_numeric_codes=True
                )
            else:
                CHILDREN_BIRTHED_NUM_1_1 = self.fake.random_int(min=0, max=25)

            if CHILDREN_BIRTHED_NUM_1_1 > 0 or CHILDREN_BIRTHED_NUM_1_1 in (
                -1,
                -3,
                -999,
            ):
                if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                    CHILDREN_BIRTHED_FIRST_AGE_1_1 = generate_code(
                        self.fake,
                        "CHILDREN_BIRTHED_FIRST_AGE_1_1",
                        enforce_numeric_codes=True,
                    )
                else:
                    # NOTE: questionnaire has this as min age 0, but other questions have min age 8, so it is 8 here
                    CHILDREN_BIRTHED_FIRST_AGE_1_1 = self.fake.random_int(
                        min=8, max=current_age
                    )

            if CHILDREN_BIRTHED_NUM_1_1 > 1 or CHILDREN_BIRTHED_NUM_1_1 in (
                -1,
                -3,
                -999,
            ):
                if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                    CHILDREN_BIRTHED_LAST_AGE_1_1 = generate_code(
                        self.fake,
                        "CHILDREN_BIRTHED_LAST_AGE_1_1",
                        enforce_numeric_codes=True,
                    )
                else:
                    CHILDREN_BIRTHED_LAST_AGE_1_1 = self.fake.random_int(
                        min=8, max=current_age
                    )

            GYN_CONTRACEPT_IMPLANT_1_1 = generate_code(
                self.fake, "GYN_CONTRACEPT_IMPLANT_1_1", enforce_numeric_codes=True
            )

            if GYN_CONTRACEPT_IMPLANT_1_1 == 1:
                GYN_CONTRACEPT_METHODS_1_M = generate_codes(
                    self.fake,
                    "GYN_CONTRACEPT_METHODS_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

                if any(code in (1, 5) for code in GYN_CONTRACEPT_METHODS_1_M):
                    if self.fake.pybool(
                        truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ):
                        GYN_CONTRACEPT_PILL_FIRST_AGE_1_1 = generate_code(
                            self.fake,
                            "GYN_CONTRACEPT_PILL_FIRST_AGE_1_1",
                            enforce_numeric_codes=True,
                        )
                    else:
                        GYN_CONTRACEPT_PILL_FIRST_AGE_1_1 = self.fake.random_int(
                            min=5, max=current_age
                        )
                    if self.fake.pybool(
                        truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ):
                        GYN_CONTRACEPT_PILL_LAST_AGE_1_1 = generate_code(
                            self.fake,
                            "GYN_CONTRACEPT_PILL_LAST_AGE_1_1",
                            enforce_numeric_codes=True,
                        )
                    else:
                        # NOTE: questionnaire says this just has to be greater than GYN_CONTRACEPT_PILL_FIRST_AGE_1_1, but if that takes a negative code
                        # this could be a negative age, so we enforce a minimum of 5 here
                        GYN_CONTRACEPT_PILL_LAST_AGE_1_1 = self.fake.random_int(
                            min=max(5, GYN_CONTRACEPT_PILL_FIRST_AGE_1_1),
                            max=current_age,
                        )

            GYN_HRT_1_1 = generate_code(
                self.fake, "GYN_HRT_1_1", enforce_numeric_codes=True
            )

            if GYN_HRT_1_1 == 1:
                if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                    GYN_HRT_FIRST_TRT_AGE_1_1 = generate_code(
                        self.fake,
                        "GYN_HRT_FIRST_TRT_AGE_1_1",
                        enforce_numeric_codes=True,
                    )
                else:
                    GYN_HRT_FIRST_TRT_AGE_1_1 = self.fake.random_int(
                        min=16, max=current_age
                    )
                if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                    GYN_HRT_LAST_TRT_AGE_1_1 = generate_code(
                        self.fake,
                        "GYN_HRT_LAST_TRT_AGE_1_1",
                        enforce_numeric_codes=True,
                    )
                else:
                    # NOTE: questionnaire says this just has to be greater than GYN_HRT_FIRST_TRT_AGE_1_1, but if that takes a negative code
                    # this could be a negative age, so we enforce a minimum of 16 here
                    GYN_HRT_LAST_TRT_AGE_1_1 = self.fake.random_int(
                        min=max(16, GYN_HRT_FIRST_TRT_AGE_1_1), max=current_age
                    )

            GYN_HYST_1_1 = generate_code(
                self.fake, "GYN_HYST_1_1", enforce_numeric_codes=True
            )

            if GYN_HYST_1_1 == 1:
                if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                    GYN_HYST_AGE_1_1 = generate_code(
                        self.fake, "GYN_HYST_AGE_1_1", enforce_numeric_codes=True
                    )
                else:
                    GYN_HYST_AGE_1_1 = self.fake.random_int(min=0, max=current_age)

            GYN_OOPH_1_1 = generate_code(
                self.fake, "GYN_OOPH_1_1", enforce_numeric_codes=True
            )

            if GYN_OOPH_1_1 == 1:
                if self.fake.pybool(truth_probability=PREFER_NOT_TO_ANSWER_PERCENTAGE):
                    GYN_OOPH_AGE_1_1 = generate_code(
                        self.fake, "GYN_OOPH_AGE_1_1", enforce_numeric_codes=True
                    )
                else:
                    GYN_OOPH_AGE_1_1 = self.fake.random_int(min=0, max=current_age)

        DIAG_2_M = generate_codes(
            self.fake,
            "DIAG_2_M",
            exclusive_codes=ExclusiveCodes(
                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
            ),
            enforce_numeric_codes=True,
        )

        if 1 in DIAG_2_M:
            DIAG_AUTO_1_M = generate_codes(
                self.fake,
                "DIAG_AUTO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 2 in DIAG_2_M:
            DIAG_ANAEMIA_1_M = generate_codes(
                self.fake,
                "DIAG_ANAEMIA_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 3 in DIAG_2_M:
            DIAG_CANCER_1_M = generate_codes(
                self.fake,
                "DIAG_CANCER_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE,
                    special_non_exclusive_codes=[-1],
                ),
                enforce_numeric_codes=True,
            )

            if 18 in DIAG_CANCER_1_M:
                DIAG_CANCER_SKIN_1_M = generate_codes(
                    self.fake,
                    "DIAG_CANCER_SKIN_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

        if 4 in DIAG_2_M:
            DIAG_OB_1_M = generate_codes(
                self.fake,
                "DIAG_OB_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 5 in DIAG_2_M:
            DIAG_GASTRO_1_M = generate_codes(
                self.fake,
                "DIAG_GASTRO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 6 in DIAG_2_M:
            DIAG_ENDOCR_1_M = generate_codes(
                self.fake,
                "DIAG_ENDOCR_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 7 in DIAG_2_M:
            DIAG_OPTHAL_1_M = generate_codes(
                self.fake,
                "DIAG_OPTHAL_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 8 in DIAG_2_M:
            DIAG_OSTEO_1_M = generate_codes(
                self.fake,
                "DIAG_OSTEO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 9 in DIAG_2_M:
            DIAG_CVD_1_M = generate_codes(
                self.fake,
                "DIAG_CVD_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 10 in DIAG_2_M:
            DIAG_UROL_1_M = generate_codes(
                self.fake,
                "DIAG_UROL_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 11 in DIAG_2_M:
            DIAG_RESP_1_M = generate_codes(
                self.fake,
                "DIAG_RESP_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 12 in DIAG_2_M:
            DIAG_PSYCH_1_M = generate_codes(
                self.fake,
                "DIAG_PSYCH_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

            if 1 in DIAG_PSYCH_1_M:
                DIAG_PSYCH_ANX_1_M = generate_codes(
                    self.fake,
                    "DIAG_PSYCH_ANX_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 4 in DIAG_PSYCH_1_M:
                DIAG_PSYCH_DEPR_1_M = generate_codes(
                    self.fake,
                    "DIAG_PSYCH_DEPR_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 8 in DIAG_PSYCH_1_M:
                DIAG_PSYCH_EAT_1_M = generate_codes(
                    self.fake,
                    "DIAG_PSYCH_EAT_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

        if 13 in DIAG_2_M:
            DIAG_NEURO_DEV_1_M = generate_codes(
                self.fake,
                "DIAG_NEURO_DEV_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 14 in DIAG_2_M:
            DIAG_NEURO_1_M = generate_codes(
                self.fake,
                "DIAG_NEURO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 15 in DIAG_2_M:
            DIAG_REPRO_1_M = generate_codes(
                self.fake,
                "DIAG_REPRO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        # NOTE: source questionnaire_logic.csv has this row's field_name as "eb", which isn't a
        # real field. The question text ("Do you regularly take medications for any of the
        # following reasons?") matches MEDICAT_1_M exactly, so that's what's used here.
        MEDICAT_1_M = generate_codes(
            self.fake,
            "MEDICAT_1_M",
            exclusive_codes=ExclusiveCodes(
                exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
            ),
            enforce_numeric_codes=True,
        )

        if 1 in MEDICAT_1_M:
            MEDICAT_AUTO_1_M = generate_codes(
                self.fake,
                "MEDICAT_AUTO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 2 in MEDICAT_1_M:
            MEDICAT_OSTEO_1_M = generate_codes(
                self.fake,
                "MEDICAT_OSTEO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 3 in MEDICAT_1_M:
            MEDICAT_CANCER_1_M = generate_codes(
                self.fake,
                "MEDICAT_CANCER_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 4 in MEDICAT_1_M:
            MEDICAT_DIAB_1_M = generate_codes(
                self.fake,
                "MEDICAT_DIAB_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 5 in MEDICAT_1_M:
            MEDICAT_GASTRO_1_M = generate_codes(
                self.fake,
                "MEDICAT_GASTRO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 6 in MEDICAT_1_M:
            MEDICAT_ENDOCR_1_M = generate_codes(
                self.fake,
                "MEDICAT_ENDOCR_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 7 in MEDICAT_1_M:
            MEDICAT_CVD_1_M = generate_codes(
                self.fake,
                "MEDICAT_CVD_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 8 in MEDICAT_1_M:
            MEDICAT_RESP_1_M = generate_codes(
                self.fake,
                "MEDICAT_RESP_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 9 in MEDICAT_1_M:
            MEDICAT_PSYCH_1_M = generate_codes(
                self.fake,
                "MEDICAT_PSYCH_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

            if 1 in MEDICAT_PSYCH_1_M:
                MEDICAT_PSYCH_ANTIDEPR_1_M = generate_codes(
                    self.fake,
                    "MEDICAT_PSYCH_ANTIDEPR_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

            if 2 in MEDICAT_PSYCH_1_M:
                MEDICAT_PSYCH_ANTIPSYCH_1_M = generate_codes(
                    self.fake,
                    "MEDICAT_PSYCH_ANTIPSYCH_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

        if 10 in MEDICAT_1_M:
            MEDICAT_NEURO_1_M = generate_codes(
                self.fake,
                "MEDICAT_NEURO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 11 in MEDICAT_1_M:
            MEDICAT_PAIN_1_M = generate_codes(
                self.fake,
                "MEDICAT_PAIN_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        if 12 in MEDICAT_1_M:
            MEDICAT_REPRO_1_M = generate_codes(
                self.fake,
                "MEDICAT_REPRO_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

            if 1 in MEDICAT_REPRO_1_M:
                MEDICAT_REPRO_CONTRACEPT_1_M = generate_codes(
                    self.fake,
                    "MEDICAT_REPRO_CONTRACEPT_1_M",
                    exclusive_codes=ExclusiveCodes(
                        exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                    ),
                    enforce_numeric_codes=True,
                )

        if 13 in MEDICAT_1_M:
            MEDICAT_SUPPL_1_M = generate_codes(
                self.fake,
                "MEDICAT_SUPPL_1_M",
                exclusive_codes=ExclusiveCodes(
                    exclusive_percentage=PREFER_NOT_TO_ANSWER_PERCENTAGE
                ),
                enforce_numeric_codes=True,
            )

        SKIP_PHQ9_GAD7_1_1 = generate_code(
            self.fake, "SKIP_PHQ9_GAD7_1_1", enforce_numeric_codes=True
        )

        if SKIP_PHQ9_GAD7_1_1 == 0:
            PHQ9_ITEM1_INTEREST_1_1 = generate_code(
                self.fake, "PHQ9_ITEM1_INTEREST_1_1", enforce_numeric_codes=True
            )
            PHQ9_ITEM2_DOWN_1_1 = generate_code(
                self.fake, "PHQ9_ITEM2_DOWN_1_1", enforce_numeric_codes=True
            )
            PHQ9_ITEM3_SLEEP_1_1 = generate_code(
                self.fake, "PHQ9_ITEM3_SLEEP_1_1", enforce_numeric_codes=True
            )
            PHQ9_ITEM4_ENERGY_1_1 = generate_code(
                self.fake, "PHQ9_ITEM4_ENERGY_1_1", enforce_numeric_codes=True
            )
            PHQ9_ITEM5_APPETITE_1_1 = generate_code(
                self.fake, "PHQ9_ITEM5_APPETITE_1_1", enforce_numeric_codes=True
            )
            PHQ9_ITEM6_BAD_1_1 = generate_code(
                self.fake, "PHQ9_ITEM6_BAD_1_1", enforce_numeric_codes=True
            )
            PHQ9_ITEM7_CONCENTR_1_1 = generate_code(
                self.fake, "PHQ9_ITEM7_CONCENTR_1_1", enforce_numeric_codes=True
            )
            PHQ9_ITEM8_MOVEMENT_1_1 = generate_code(
                self.fake, "PHQ9_ITEM8_MOVEMENT_1_1", enforce_numeric_codes=True
            )
            PHQ9_ITEM9_HARM_1_1 = generate_code(
                self.fake, "PHQ9_ITEM9_HARM_1_1", enforce_numeric_codes=True
            )
            PHQ9_IMPAIR_1_1 = generate_code(
                self.fake, "PHQ9_IMPAIR_1_1", enforce_numeric_codes=True
            )

            GAD7_ITEM1_ANX_1_1 = generate_code(
                self.fake, "GAD7_ITEM1_ANX_1_1", enforce_numeric_codes=True
            )
            GAD7_ITEM2_WORRY_CONTROL_1_1 = generate_code(
                self.fake, "GAD7_ITEM2_WORRY_CONTROL_1_1", enforce_numeric_codes=True
            )
            GAD7_ITEM3_WORRY_AMOUNT_1_1 = generate_code(
                self.fake, "GAD7_ITEM3_WORRY_AMOUNT_1_1", enforce_numeric_codes=True
            )
            GAD7_ITEM4_RELAX_1_1 = generate_code(
                self.fake, "GAD7_ITEM4_RELAX_1_1", enforce_numeric_codes=True
            )
            GAD7_ITEM5_RESTLESS_1_1 = generate_code(
                self.fake, "GAD7_ITEM5_RESTLESS_1_1", enforce_numeric_codes=True
            )
            GAD7_ITEM6_ANNOYED_1_1 = generate_code(
                self.fake, "GAD7_ITEM6_ANNOYED_1_1", enforce_numeric_codes=True
            )
            GAD7_ITEM7_AFRAID_1_1 = generate_code(
                self.fake, "GAD7_ITEM7_AFRAID_1_1", enforce_numeric_codes=True
            )
            GAD7_IMPAIR_1_1 = generate_code(
                self.fake, "GAD7_IMPAIR_1_1", enforce_numeric_codes=True
            )

        return Questionnaire(
            ID=ID,
            PID=PID,
            QUESTIONNAIRE_VERSION=QUESTIONNAIRE_VERSION,
            SUBMISSION_DATE=SUBMISSION_DATE,
            DEMOG_TRANSGENDER_1_1=DEMOG_TRANSGENDER_1_1,
            DEMOG_SEXUAL_ORIENTATION_1_1=DEMOG_SEXUAL_ORIENTATION_1_1,
            DEMOG_HEIGHT_ENTER_UNIT_1_1=DEMOG_HEIGHT_ENTER_UNIT_1_1,
            DEMOG_HEIGHT_1_1=DEMOG_HEIGHT_1_1,
            DEMOG_WEIGHT_ENTER_UNIT_1_1=DEMOG_WEIGHT_ENTER_UNIT_1_1,
            DEMOG_WEIGHT_1_1=DEMOG_WEIGHT_1_1,
            DEMOG_LANGUAGE_1_1=DEMOG_LANGUAGE_1_1,
            DEMOG_RELATSH_STATUS_2_1=DEMOG_RELATSH_STATUS_2_1,
            DEMOG_RELATSH_MARR_CURR_1_1=DEMOG_RELATSH_MARR_CURR_1_1,
            DEMOG_RELATSH_CIVIL_CURR_1_1=DEMOG_RELATSH_CIVIL_CURR_1_1,
            DEMOG_RELATSH_MARR_PREV_1_1=DEMOG_RELATSH_MARR_PREV_1_1,
            DEMOG_RELATSH_CIVIL_PREV_1_1=DEMOG_RELATSH_CIVIL_PREV_1_1,
            HOUSING_TYPE_1_1=HOUSING_TYPE_1_1,
            HOUSING_TENURE_1_1=HOUSING_TENURE_1_1,
            HOUSING_ENERGY_1_M=HOUSING_ENERGY_1_M,
            HOUSING_HEAT_1_M=HOUSING_HEAT_1_M,
            HOUSING_CURR_ADD_YRS_1_1=HOUSING_CURR_ADD_YRS_1_1,
            HOUSING_PEOPLE_1_1=HOUSING_PEOPLE_1_1,
            HOUSING_PEOPLE_RELATE_1_M=HOUSING_PEOPLE_RELATE_1_M,
            HOUSING_VEHICLES_1_1=HOUSING_VEHICLES_1_1,
            WORK_STATUS_2_M=WORK_STATUS_2_M,
            WORK_YRS_1_1=WORK_YRS_1_1,
            WORK_WK_HRS_1_1=WORK_WK_HRS_1_1,
            WORK_WK_TRAVEL_1_1=WORK_WK_TRAVEL_1_1,
            WORK_TRANSPORT_1_M=WORK_TRANSPORT_1_M,
            WORK_DISTANCE_1_1=WORK_DISTANCE_1_1,
            WORK_WALK_STAND_1_1=WORK_WALK_STAND_1_1,
            WORK_MANUAL_LABOUR_1_1=WORK_MANUAL_LABOUR_1_1,
            WORK_SHIFTS_1_1=WORK_SHIFTS_1_1,
            WORK_NIGHTS_1_1=WORK_NIGHTS_1_1,
            EDU_QUAL_1_M=EDU_QUAL_1_M,
            EDU_COMP_AGE_2_1=EDU_COMP_AGE_2_1,
            HOUSING_INCOME_1_1=HOUSING_INCOME_1_1,
            ACTIVITY_WALK_DAYS_2_1=ACTIVITY_WALK_DAYS_2_1,
            ACTIVITY_WALK_MINS_2_1=ACTIVITY_WALK_MINS_2_1,
            ACTIVITY_MOD_DAYS_2_1=ACTIVITY_MOD_DAYS_2_1,
            ACTIVITY_MOD_MINS_2_1=ACTIVITY_MOD_MINS_2_1,
            ACTIVITY_VIG_DAYS_2_1=ACTIVITY_VIG_DAYS_2_1,
            ACTIVITY_VIG_MINS_2_1=ACTIVITY_VIG_MINS_2_1,
            ACTIVITY_WALK_PACE_1_1=ACTIVITY_WALK_PACE_1_1,
            ACTIVITY_STAIRS_1_1=ACTIVITY_STAIRS_1_1,
            ACTIVITY_TRANSPORT_1_M=ACTIVITY_TRANSPORT_1_M,
            ACTIVITY_TYPE_1_M=ACTIVITY_TYPE_1_M,
            ACTIVITY_TYPE_WALK_1_1=ACTIVITY_TYPE_WALK_1_1,
            ACTIVITY_TYPE_WALK_DUR_1_1=ACTIVITY_TYPE_WALK_DUR_1_1,
            ACTIVITY_TYPE_EXERCISE_1_1=ACTIVITY_TYPE_EXERCISE_1_1,
            ACTIVITY_TYPE_EXERCISE_DUR_1_1=ACTIVITY_TYPE_EXERCISE_DUR_1_1,
            ACTIVITY_TYPE_STREN_1_1=ACTIVITY_TYPE_STREN_1_1,
            ACTIVITY_TYPE_STREN_DUR_1_1=ACTIVITY_TYPE_STREN_DUR_1_1,
            ACTIVITY_TYPE_DIY_LIGHT_1_1=ACTIVITY_TYPE_DIY_LIGHT_1_1,
            ACTIVITY_TYPE_DIY_LIGHT_DUR_1_1=ACTIVITY_TYPE_DIY_LIGHT_DUR_1_1,
            ACTIVITY_TYPE_DIY_HEAVY_1_1=ACTIVITY_TYPE_DIY_HEAVY_1_1,
            ACTIVITY_TYPE_DIY_HEAVY_DUR_1_1=ACTIVITY_TYPE_DIY_HEAVY_DUR_1_1,
            LIFESTYLE_SOCIAL_VISITS_1_1=LIFESTYLE_SOCIAL_VISITS_1_1,
            LIFESTYLE_SOCIAL_REC_1_M=LIFESTYLE_SOCIAL_REC_1_M,
            LIFESTYLE_OUTDOOR_SUM_HRS_1_1=LIFESTYLE_OUTDOOR_SUM_HRS_1_1,
            LIFESTYLE_OUTDOOR_WIN_HRS_1_1=LIFESTYLE_OUTDOOR_WIN_HRS_1_1,
            LIFESTYLE_SCREEN_TV_HRS_2_1=LIFESTYLE_SCREEN_TV_HRS_2_1,
            LIFESTYLE_SCREEN_PC_HRS_2_1=LIFESTYLE_SCREEN_PC_HRS_2_1,
            LIFESTYLE_DRIVE_HRS_1_1=LIFESTYLE_DRIVE_HRS_1_1,
            SLEEP_HRS_1_1=SLEEP_HRS_1_1,
            SLEEP_WAKING_1_1=SLEEP_WAKING_1_1,
            SLEEP_CHRONOTYPE_1_1=SLEEP_CHRONOTYPE_1_1,
            SLEEP_NAPPING_1_1=SLEEP_NAPPING_1_1,
            SLEEP_DAYTIME_1_1=SLEEP_DAYTIME_1_1,
            SLEEP_TROUBLE_1_1=SLEEP_TROUBLE_1_1,
            SLEEP_SNORING_1_1=SLEEP_SNORING_1_1,
            SMOKE_TOBACCO_TYPE_1_M=SMOKE_TOBACCO_TYPE_1_M,
            SMOKE_TOBACCO_AGE_1_1=SMOKE_TOBACCO_AGE_1_1,
            SMOKE_100_TIMES_2_1=SMOKE_100_TIMES_2_1,
            SMOKE_VAPE_AGE_2_1=SMOKE_VAPE_AGE_2_1,
            SMOKE_VAPE_USE_2_1=SMOKE_VAPE_USE_2_1,
            SMOKE_REG_1_M=SMOKE_REG_1_M,
            SMOKE_REG_FIRST_AGE_2_1=SMOKE_REG_FIRST_AGE_2_1,
            SMOKE_REG_TYPE_2_1=SMOKE_REG_TYPE_2_1,
            SMOKE_STATUS_2_1=SMOKE_STATUS_2_1,
            SMOKE_PREV_REG_2_1=SMOKE_PREV_REG_2_1,
            SMOKE_FIRST_AGE_2_1=SMOKE_FIRST_AGE_2_1,
            SMOKE_PREV_AGE_2_1=SMOKE_PREV_AGE_2_1,
            SMOKE_AVG_2_1=SMOKE_AVG_2_1,
            SMOKE_PREV_REDUCE_REASON_2_M=SMOKE_PREV_REDUCE_REASON_2_M,
            SMOKE_REG_DAY_2_1=SMOKE_REG_DAY_2_1,
            SMOKE_CHG_2_1=SMOKE_CHG_2_1,
            SMOKE_CHG_REDUCE_REASON_2_M=SMOKE_CHG_REDUCE_REASON_2_M,
            SMOKE_CHG_REDUCE_ABST_1_1=SMOKE_CHG_REDUCE_ABST_1_1,
            SMOKE_CHG_REDUCE_ABST_REASON_1_M=SMOKE_CHG_REDUCE_ABST_REASON_1_M,
            SMOKE_CHG_ABST_2_1=SMOKE_CHG_ABST_2_1,
            SMOKE_CHG_ABST_REASON_1_M=SMOKE_CHG_ABST_REASON_1_M,
            SMOKE_VAPE_AVG_2_1=SMOKE_VAPE_AVG_2_1,
            SMOKE_VAPE_TYPE_2_M=SMOKE_VAPE_TYPE_2_M,
            SMOKE_EXPOSURE_1_1=SMOKE_EXPOSURE_1_1,
            SMOKE_EXPOSURE_HRS_1_1=SMOKE_EXPOSURE_HRS_1_1,
            ALCOHOL_CURR_1_1=ALCOHOL_CURR_1_1,
            ALCOHOL_PREV_1_1=ALCOHOL_PREV_1_1,
            ALCOHOL_WINE_RED_MTH_2_1=ALCOHOL_WINE_RED_MTH_2_1,
            ALCOHOL_WINE_WHITE_MTH_2_1=ALCOHOL_WINE_WHITE_MTH_2_1,
            ALCOHOL_BEER_MTH_2_1=ALCOHOL_BEER_MTH_2_1,
            ALCOHOL_SPIRITS_MTH_2_1=ALCOHOL_SPIRITS_MTH_2_1,
            ALCOHOL_WINE_FORT_MTH_2_1=ALCOHOL_WINE_FORT_MTH_2_1,
            ALCOHOL_OTHER_MTH_2_1=ALCOHOL_OTHER_MTH_2_1,
            ALCOHOL_WINE_RED_WK_1_1=ALCOHOL_WINE_RED_WK_1_1,
            ALCOHOL_WINE_WHITE_WK_1_1=ALCOHOL_WINE_WHITE_WK_1_1,
            ALCOHOL_BEER_WK_1_1=ALCOHOL_BEER_WK_1_1,
            ALCOHOL_SPIRITS_WK_1_1=ALCOHOL_SPIRITS_WK_1_1,
            ALCOHOL_WINE_FORT_WK_1_1=ALCOHOL_WINE_FORT_WK_1_1,
            ALCOHOL_OTHER_WK_1_1=ALCOHOL_OTHER_WK_1_1,
            ALCOHOL_FOOD_1_1=ALCOHOL_FOOD_1_1,
            ALCOHOL_CHG_1_1=ALCOHOL_CHG_1_1,
            ALCOHOL_CHG_REDUCE_REASON_2_M=ALCOHOL_CHG_REDUCE_REASON_2_M,
            ALCOHOL_CHG_ABST_REASON_2_M=ALCOHOL_CHG_ABST_REASON_2_M,
            BIRTH_PLACE_1_1=BIRTH_PLACE_1_1,
            IMMIGRATE_UK_YR_1_1=IMMIGRATE_UK_YR_1_1,
            ADOPTION_STATUS_1_1=ADOPTION_STATUS_1_1,
            FATHER_ALIVE_1_1=FATHER_ALIVE_1_1,
            FATHER_AGE_1_1=FATHER_AGE_1_1,
            FATHER_AGE_DECEASED_1_1=FATHER_AGE_DECEASED_1_1,
            FATHER_DIAG_A_2_M=FATHER_DIAG_A_2_M,
            FATHER_DIAG_AUTO_1_M=FATHER_DIAG_AUTO_1_M,
            FATHER_DIAG_ANAEMIA_1_M=FATHER_DIAG_ANAEMIA_1_M,
            FATHER_DIAG_CANCER_1_M=FATHER_DIAG_CANCER_1_M,
            FATHER_DIAG_CANCER_SKIN_1_M=FATHER_DIAG_CANCER_SKIN_1_M,
            FATHER_DIAG_GASTRO_1_M=FATHER_DIAG_GASTRO_1_M,
            FATHER_DIAG_ENDOCR_1_M=FATHER_DIAG_ENDOCR_1_M,
            FATHER_DIAG_OPTHAL_1_M=FATHER_DIAG_OPTHAL_1_M,
            FATHER_DIAG_OSTEO_1_M=FATHER_DIAG_OSTEO_1_M,
            FATHER_DIAG_CVD_1_M=FATHER_DIAG_CVD_1_M,
            FATHER_DIAG_UROL_1_M=FATHER_DIAG_UROL_1_M,
            FATHER_DIAG_RESP_1_M=FATHER_DIAG_RESP_1_M,
            FATHER_DIAG_PSYCH_1_M=FATHER_DIAG_PSYCH_1_M,
            FATHER_DIAG_PSYCH_ANX_1_M=FATHER_DIAG_PSYCH_ANX_1_M,
            FATHER_DIAG_PSYCH_DEPR_1_M=FATHER_DIAG_PSYCH_DEPR_1_M,
            FATHER_DIAG_PSYCH_EAT_1_M=FATHER_DIAG_PSYCH_EAT_1_M,
            FATHER_DIAG_NEURO_DEV_1_M=FATHER_DIAG_NEURO_DEV_1_M,
            FATHER_DIAG_NEURO_1_M=FATHER_DIAG_NEURO_1_M,
            FATHER_DIAG_REPRO_1_M=FATHER_DIAG_REPRO_1_M,
            MOTHER_ALIVE_1_1=MOTHER_ALIVE_1_1,
            MOTHER_AGE_1_1=MOTHER_AGE_1_1,
            MOTHER_AGE_DECEASED_1_1=MOTHER_AGE_DECEASED_1_1,
            MOTHER_DIAG_A_2_M=MOTHER_DIAG_A_2_M,
            MOTHER_DIAG_AUTO_1_M=MOTHER_DIAG_AUTO_1_M,
            MOTHER_DIAG_ANAEMIA_1_M=MOTHER_DIAG_ANAEMIA_1_M,
            MOTHER_DIAG_CANCER_1_M=MOTHER_DIAG_CANCER_1_M,
            MOTHER_DIAG_CANCER_SKIN_1_M=MOTHER_DIAG_CANCER_SKIN_1_M,
            MOTHER_DIAG_GASTRO_1_M=MOTHER_DIAG_GASTRO_1_M,
            MOTHER_DIAG_ENDOCR_1_M=MOTHER_DIAG_ENDOCR_1_M,
            MOTHER_DIAG_OPTHAL_1_M=MOTHER_DIAG_OPTHAL_1_M,
            MOTHER_DIAG_OSTEO_1_M=MOTHER_DIAG_OSTEO_1_M,
            MOTHER_DIAG_CVD_1_M=MOTHER_DIAG_CVD_1_M,
            MOTHER_DIAG_UROL_1_M=MOTHER_DIAG_UROL_1_M,
            MOTHER_DIAG_RESP_1_M=MOTHER_DIAG_RESP_1_M,
            MOTHER_DIAG_PSYCH_1_M=MOTHER_DIAG_PSYCH_1_M,
            MOTHER_DIAG_PSYCH_ANX_1_M=MOTHER_DIAG_PSYCH_ANX_1_M,
            MOTHER_DIAG_PSYCH_DEPR_1_M=MOTHER_DIAG_PSYCH_DEPR_1_M,
            MOTHER_DIAG_PSYCH_EAT_1_M=MOTHER_DIAG_PSYCH_EAT_1_M,
            MOTHER_DIAG_NEURO_DEV_1_M=MOTHER_DIAG_NEURO_DEV_1_M,
            MOTHER_DIAG_NEURO_1_M=MOTHER_DIAG_NEURO_1_M,
            MOTHER_DIAG_REPRO_1_M=MOTHER_DIAG_REPRO_1_M,
            SIBLING_NUM_BROTHERS_1_1=SIBLING_NUM_BROTHERS_1_1,
            SIBLING_NUM_SISTERS_1_1=SIBLING_NUM_SISTERS_1_1,
            SIBLING_DIAG_A_2_M=SIBLING_DIAG_A_2_M,
            SIBLING_DIAG_AUTO_1_M=SIBLING_DIAG_AUTO_1_M,
            SIBLING_DIAG_ANAEMIA_1_M=SIBLING_DIAG_ANAEMIA_1_M,
            SIBLING_DIAG_CANCER_1_M=SIBLING_DIAG_CANCER_1_M,
            SIBLING_DIAG_CANCER_SKIN_1_M=SIBLING_DIAG_CANCER_SKIN_1_M,
            SIBLING_DIAG_GASTRO_1_M=SIBLING_DIAG_GASTRO_1_M,
            SIBLING_DIAG_ENDOCR_1_M=SIBLING_DIAG_ENDOCR_1_M,
            SIBLING_DIAG_OPTHAL_1_M=SIBLING_DIAG_OPTHAL_1_M,
            SIBLING_DIAG_OSTEO_1_M=SIBLING_DIAG_OSTEO_1_M,
            SIBLING_DIAG_CVD_1_M=SIBLING_DIAG_CVD_1_M,
            SIBLING_DIAG_UROL_1_M=SIBLING_DIAG_UROL_1_M,
            SIBLING_DIAG_RESP_1_M=SIBLING_DIAG_RESP_1_M,
            SIBLING_DIAG_PSYCH_1_M=SIBLING_DIAG_PSYCH_1_M,
            SIBLING_DIAG_PSYCH_ANX_1_M=SIBLING_DIAG_PSYCH_ANX_1_M,
            SIBLING_DIAG_PSYCH_DEPR_1_M=SIBLING_DIAG_PSYCH_DEPR_1_M,
            SIBLING_DIAG_PSYCH_EAT_1_M=SIBLING_DIAG_PSYCH_EAT_1_M,
            SIBLING_DIAG_NEURO_DEV_1_M=SIBLING_DIAG_NEURO_DEV_1_M,
            SIBLING_DIAG_NEURO_1_M=SIBLING_DIAG_NEURO_1_M,
            SIBLING_DIAG_REPRO_1_M=SIBLING_DIAG_REPRO_1_M,
            HEALTH_STATUS_CURR_1_1=HEALTH_STATUS_CURR_1_1,
            HEALTH_STATUS_CHRONIC_1_1=HEALTH_STATUS_CHRONIC_1_1,
            HEALTH_STATUS_DISABILITY_SUPPORT_1_M=HEALTH_STATUS_DISABILITY_SUPPORT_1_M,
            HEALTH_STATUS_PRIVATE_HEALTHCARE_1_1=HEALTH_STATUS_PRIVATE_HEALTHCARE_1_1,
            HEALTH_COVID_1_1=HEALTH_COVID_1_1,
            HEALTH_SUN_PROTECT_1_1=HEALTH_SUN_PROTECT_1_1,
            HEALTH_DENTAL_1_M=HEALTH_DENTAL_1_M,
            HEALTH_FALLS_1_1=HEALTH_FALLS_1_1,
            HEALTH_WEIGHT_CHG_1_1=HEALTH_WEIGHT_CHG_1_1,
            HEALTH_RESP_WHEEZE_1_1=HEALTH_RESP_WHEEZE_1_1,
            HEALTH_RESP_SHORT_1_1=HEALTH_RESP_SHORT_1_1,
            HEALTH_PAIN_LEG_1_1=HEALTH_PAIN_LEG_1_1,
            HEALTH_AMPUTATION_1_1=HEALTH_AMPUTATION_1_1,
            HEALTH_PAIN_ACUTE_2_M=HEALTH_PAIN_ACUTE_2_M,
            HEALTH_PAIN_CHRONIC_1_M=HEALTH_PAIN_CHRONIC_1_M,
            HEALTH_PAIN_CHEST_1_1=HEALTH_PAIN_CHEST_1_1,
            HEALTH_PAIN_CHEST_WALK_1_1=HEALTH_PAIN_CHEST_WALK_1_1,
            HEALTH_PAIN_CHEST_WALK_UPHILL_1_1=HEALTH_PAIN_CHEST_WALK_UPHILL_1_1,
            HEALTH_PAIN_CHEST_SUBSIDE_1_1=HEALTH_PAIN_CHEST_SUBSIDE_1_1,
            HEALTH_CHECK_COLORECTAL_1_1=HEALTH_CHECK_COLORECTAL_1_1,
            HEALTH_CHECK_COLORECTAL_YRS_1_1=HEALTH_CHECK_COLORECTAL_YRS_1_1,
            HEALTH_CHECK_PROSTATE_1_1=HEALTH_CHECK_PROSTATE_1_1,
            HEALTH_CHECK_PROSTATE_YRS_1_1=HEALTH_CHECK_PROSTATE_YRS_1_1,
            CHILDREN_BIO_NUM_2_1=CHILDREN_BIO_NUM_2_1,
            CHILDREN_BIO_FIRST_AGE_1_1=CHILDREN_BIO_FIRST_AGE_1_1,
            CHILDREN_BIO_LAST_AGE_1_1=CHILDREN_BIO_LAST_AGE_1_1,
            HEALTH_CHECK_MAMMOGRAM_1_1=HEALTH_CHECK_MAMMOGRAM_1_1,
            HEALTH_CHECK_MAMMOGRAM_YRS_1_1=HEALTH_CHECK_MAMMOGRAM_YRS_1_1,
            HEALTH_CHECK_SMEAR_1_1=HEALTH_CHECK_SMEAR_1_1,
            HEALTH_CHECK_SMEAR_YRS_1_1=HEALTH_CHECK_SMEAR_YRS_1_1,
            GYN_MENSTR_AGE_1_1=GYN_MENSTR_AGE_1_1,
            GYN_MENOPAUSE_2_1=GYN_MENOPAUSE_2_1,
            GYN_MENOPAUSE_LAST_PERIOD_AGE_2_1=GYN_MENOPAUSE_LAST_PERIOD_AGE_2_1,
            GYN_MENSTR_LAST_PERIOD_DAYS_2_1=GYN_MENSTR_LAST_PERIOD_DAYS_2_1,
            GYN_MENSTR_CYCLE_DAYS_2_1=GYN_MENSTR_CYCLE_DAYS_2_1,
            CHILDREN_BIRTHED_NUM_1_1=CHILDREN_BIRTHED_NUM_1_1,
            CHILDREN_BIRTHED_FIRST_AGE_1_1=CHILDREN_BIRTHED_FIRST_AGE_1_1,
            CHILDREN_BIRTHED_LAST_AGE_1_1=CHILDREN_BIRTHED_LAST_AGE_1_1,
            GYN_CONTRACEPT_IMPLANT_1_1=GYN_CONTRACEPT_IMPLANT_1_1,
            GYN_CONTRACEPT_METHODS_1_M=GYN_CONTRACEPT_METHODS_1_M,
            GYN_CONTRACEPT_PILL_FIRST_AGE_1_1=GYN_CONTRACEPT_PILL_FIRST_AGE_1_1,
            GYN_CONTRACEPT_PILL_LAST_AGE_1_1=GYN_CONTRACEPT_PILL_LAST_AGE_1_1,
            GYN_HRT_1_1=GYN_HRT_1_1,
            GYN_HRT_FIRST_TRT_AGE_1_1=GYN_HRT_FIRST_TRT_AGE_1_1,
            GYN_HRT_LAST_TRT_AGE_1_1=GYN_HRT_LAST_TRT_AGE_1_1,
            GYN_HYST_1_1=GYN_HYST_1_1,
            GYN_HYST_AGE_1_1=GYN_HYST_AGE_1_1,
            GYN_OOPH_1_1=GYN_OOPH_1_1,
            GYN_OOPH_AGE_1_1=GYN_OOPH_AGE_1_1,
            DIAG_2_M=DIAG_2_M,
            DIAG_AUTO_1_M=DIAG_AUTO_1_M,
            DIAG_ANAEMIA_1_M=DIAG_ANAEMIA_1_M,
            DIAG_CANCER_1_M=DIAG_CANCER_1_M,
            DIAG_CANCER_SKIN_1_M=DIAG_CANCER_SKIN_1_M,
            DIAG_OB_1_M=DIAG_OB_1_M,
            DIAG_GASTRO_1_M=DIAG_GASTRO_1_M,
            DIAG_ENDOCR_1_M=DIAG_ENDOCR_1_M,
            DIAG_OPTHAL_1_M=DIAG_OPTHAL_1_M,
            DIAG_OSTEO_1_M=DIAG_OSTEO_1_M,
            DIAG_CVD_1_M=DIAG_CVD_1_M,
            DIAG_UROL_1_M=DIAG_UROL_1_M,
            DIAG_RESP_1_M=DIAG_RESP_1_M,
            DIAG_PSYCH_1_M=DIAG_PSYCH_1_M,
            DIAG_PSYCH_ANX_1_M=DIAG_PSYCH_ANX_1_M,
            DIAG_PSYCH_DEPR_1_M=DIAG_PSYCH_DEPR_1_M,
            DIAG_PSYCH_EAT_1_M=DIAG_PSYCH_EAT_1_M,
            DIAG_NEURO_DEV_1_M=DIAG_NEURO_DEV_1_M,
            DIAG_NEURO_1_M=DIAG_NEURO_1_M,
            DIAG_REPRO_1_M=DIAG_REPRO_1_M,
            MEDICAT_1_M=MEDICAT_1_M,
            MEDICAT_AUTO_1_M=MEDICAT_AUTO_1_M,
            MEDICAT_OSTEO_1_M=MEDICAT_OSTEO_1_M,
            MEDICAT_CANCER_1_M=MEDICAT_CANCER_1_M,
            MEDICAT_DIAB_1_M=MEDICAT_DIAB_1_M,
            MEDICAT_GASTRO_1_M=MEDICAT_GASTRO_1_M,
            MEDICAT_ENDOCR_1_M=MEDICAT_ENDOCR_1_M,
            MEDICAT_CVD_1_M=MEDICAT_CVD_1_M,
            MEDICAT_RESP_1_M=MEDICAT_RESP_1_M,
            MEDICAT_PSYCH_1_M=MEDICAT_PSYCH_1_M,
            MEDICAT_PSYCH_ANTIDEPR_1_M=MEDICAT_PSYCH_ANTIDEPR_1_M,
            MEDICAT_PSYCH_ANTIPSYCH_1_M=MEDICAT_PSYCH_ANTIPSYCH_1_M,
            MEDICAT_NEURO_1_M=MEDICAT_NEURO_1_M,
            MEDICAT_PAIN_1_M=MEDICAT_PAIN_1_M,
            MEDICAT_REPRO_1_M=MEDICAT_REPRO_1_M,
            MEDICAT_REPRO_CONTRACEPT_1_M=MEDICAT_REPRO_CONTRACEPT_1_M,
            MEDICAT_SUPPL_1_M=MEDICAT_SUPPL_1_M,
            SKIP_PHQ9_GAD7_1_1=SKIP_PHQ9_GAD7_1_1,
            PHQ9_ITEM1_INTEREST_1_1=PHQ9_ITEM1_INTEREST_1_1,
            PHQ9_ITEM2_DOWN_1_1=PHQ9_ITEM2_DOWN_1_1,
            PHQ9_ITEM3_SLEEP_1_1=PHQ9_ITEM3_SLEEP_1_1,
            PHQ9_ITEM4_ENERGY_1_1=PHQ9_ITEM4_ENERGY_1_1,
            PHQ9_ITEM5_APPETITE_1_1=PHQ9_ITEM5_APPETITE_1_1,
            PHQ9_ITEM6_BAD_1_1=PHQ9_ITEM6_BAD_1_1,
            PHQ9_ITEM7_CONCENTR_1_1=PHQ9_ITEM7_CONCENTR_1_1,
            PHQ9_ITEM8_MOVEMENT_1_1=PHQ9_ITEM8_MOVEMENT_1_1,
            PHQ9_ITEM9_HARM_1_1=PHQ9_ITEM9_HARM_1_1,
            PHQ9_IMPAIR_1_1=PHQ9_IMPAIR_1_1,
            GAD7_ITEM1_ANX_1_1=GAD7_ITEM1_ANX_1_1,
            GAD7_ITEM2_WORRY_CONTROL_1_1=GAD7_ITEM2_WORRY_CONTROL_1_1,
            GAD7_ITEM3_WORRY_AMOUNT_1_1=GAD7_ITEM3_WORRY_AMOUNT_1_1,
            GAD7_ITEM4_RELAX_1_1=GAD7_ITEM4_RELAX_1_1,
            GAD7_ITEM5_RESTLESS_1_1=GAD7_ITEM5_RESTLESS_1_1,
            GAD7_ITEM6_ANNOYED_1_1=GAD7_ITEM6_ANNOYED_1_1,
            GAD7_ITEM7_AFRAID_1_1=GAD7_ITEM7_AFRAID_1_1,
            GAD7_IMPAIR_1_1=GAD7_IMPAIR_1_1,
        )
