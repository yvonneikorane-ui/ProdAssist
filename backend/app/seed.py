import csv
from datetime import datetime
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session

from .config import settings
from .models import ProductionRecord


def resolve_data_file() -> Path:
    path = Path(settings.data_file)

    if path.is_absolute():
        return path

    return Path(__file__).resolve().parents[2] / path


def seed_database(db: Session) -> int:
    existing = db.scalar(
        select(ProductionRecord).limit(1)
    )

    if existing is not None:
        return 0

    data_file = resolve_data_file()

    if not data_file.exists():
        raise FileNotFoundError(
            f"Production data file not found: {data_file}"
        )

    with data_file.open(
        newline="",
        encoding="utf-8",
    ) as handle:

        reader = csv.DictReader(handle)

        records = [
            ProductionRecord(
                production_id=row["production_id"],
                timestamp=datetime.fromisoformat(
                    row["timestamp"]
                ),
                machine_id=row["machine_id"],
                product_type=row["product_type"],
                order_id=row["order_id"],
                shift=row["shift"],
                target_output=int(row["target_output"]),
                actual_output=int(row["actual_output"]),
                downtime_minutes=int(
                    row["downtime_minutes"]
                ),
                defect_count=int(
                    row["defect_count"]
                ),
                total_units=int(
                    row["total_units"]
                ),
                machine_temperature_c=float(
                    row["machine_temperature_c"]
                ),
                machine_status=row["machine_status"],
            )
            for row in reader
        ]

    db.add_all(records)
    db.commit()

    return len(records)
