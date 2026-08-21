import sqlite3

from ofh_synthetic_data_generator.constants import HEALTH_CODINGS_DB_PATH


def get_codes(coding_name: str) -> list[str]:
    with sqlite3.connect(HEALTH_CODINGS_DB_PATH) as connection:
        rows = connection.execute(
            """
            SELECT *
            FROM codes
            WHERE coding_name = ?
            ORDER BY display_order
            """,
            (coding_name,),
        ).fetchall()

    return rows
