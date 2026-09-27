from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ProductionRecordOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    production_id: str
    timestamp: datetime
    machine_id: str
    product_type: str
    order_id: str
    shift: str
    target_output: int
    actual_output: int
    downtime_minutes: int
    defect_count: int
    total_units: int
    machine_temperature_c: float
    machine_status: str


class AnalysisResult(BaseModel):
    production_id: str
    output_deviation_pct: float
    defect_rate_pct: float
    severity: str
    deviation_detected: bool
    contributing_factors: list[str]
    explanation: str
    recommendation: str


class DecisionCreate(BaseModel):
    production_id: str

    decision: str = Field(
        pattern="^(investigate|accept|dismiss|escalate)$"
    )

    comment: str | None = Field(
        default=None,
        max_length=1000,
    )


class DecisionOut(DecisionCreate):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
