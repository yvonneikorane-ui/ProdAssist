from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class ProductionRecord(Base):
    __tablename__ = "production_records"

    production_id: Mapped[str] = mapped_column(
        String(20),
        primary_key=True,
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        index=True,
    )

    machine_id: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        index=True,
    )

    product_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    order_id: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    shift: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    target_output: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    actual_output: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    downtime_minutes: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    defect_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    total_units: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    machine_temperature_c: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    machine_status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )


class HumanDecision(Base):
    __tablename__ = "human_decisions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    production_id: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        index=True,
    )

    decision: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    comment: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )
