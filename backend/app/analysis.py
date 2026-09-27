from dataclasses import dataclass

from .models import ProductionRecord


OUTPUT_DEVIATION_THRESHOLD = -10.0
DOWNTIME_THRESHOLD_MINUTES = 30
DEFECT_RATE_THRESHOLD = 5.0
TEMPERATURE_THRESHOLD_C = 78.0


@dataclass(frozen=True)
class Analysis:
    output_deviation_pct: float
    defect_rate_pct: float
    severity: str
    deviation_detected: bool
    contributing_factors: list[str]
    explanation: str
    recommendation: str


def analyze_record(record: ProductionRecord) -> Analysis:
    if record.target_output <= 0:
        raise ValueError("target_output must be greater than zero")

    if record.total_units <= 0:
        raise ValueError("total_units must be greater than zero")

    output_deviation = (
        (record.actual_output - record.target_output)
        / record.target_output
        * 100
    )

    defect_rate = (
        record.defect_count
        / record.total_units
        * 100
    )

    factors: list[str] = []

    if output_deviation <= OUTPUT_DEVIATION_THRESHOLD:
        factors.append("output below target")

    if record.downtime_minutes >= DOWNTIME_THRESHOLD_MINUTES:
        factors.append("elevated downtime")

    if defect_rate >= DEFECT_RATE_THRESHOLD:
        factors.append("elevated defect rate")

    if record.machine_temperature_c >= TEMPERATURE_THRESHOLD_C:
        factors.append("elevated machine temperature")

    if record.machine_status in {"WARNING", "CRITICAL"}:
        factors.append(
            f"machine status {record.machine_status.lower()}"
        )

    deviation_detected = (
        output_deviation <= OUTPUT_DEVIATION_THRESHOLD
    )

    if record.machine_status == "CRITICAL" or output_deviation <= -20:
        severity = "critical" if deviation_detected else "watch"
    elif deviation_detected:
        severity = "warning"
    else:
        severity = "normal"

    if deviation_detected:
        context = (
            factors[1:]
            if factors and factors[0] == "output below target"
            else factors
        )

        if context:
            explanation = (
                f"Actual output is {abs(output_deviation):.1f}% below target. "
                f"Additional indicators are: {', '.join(context)}."
            )
        else:
            explanation = (
                f"Actual output is {abs(output_deviation):.1f}% below target."
            )

        recommendation = (
            "Investigate the production run and review the machine "
            "and process conditions before deciding whether production "
            "should continue."
        )

    elif factors:
        explanation = (
            "Output is within the primary deviation threshold, "
            "but contextual indicators require monitoring."
        )

        recommendation = (
            "Monitor the production run and review the highlighted "
            "indicators if they persist."
        )

    else:
        explanation = (
            "No material production deviation was detected using "
            "the current demonstrator thresholds."
        )

        recommendation = "Continue monitoring the production run."

    return Analysis(
        output_deviation_pct=round(output_deviation, 2),
        defect_rate_pct=round(defect_rate, 2),
        severity=severity,
        deviation_detected=deviation_detected,
        contributing_factors=factors,
        explanation=explanation,
        recommendation=recommendation,
    )
