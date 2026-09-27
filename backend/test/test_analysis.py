from types import SimpleNamespace

from app.analysis import analyze_record


def make_record(**overrides):
    values = {
        "production_id": "TEST-001",
        "target_output": 500,
        "actual_output": 360,
        "downtime_minutes": 47,
        "defect_count": 42,
        "total_units": 500,
        "machine_temperature_c": 81.0,
        "machine_status": "WARNING",
    }

    values.update(overrides)

    return SimpleNamespace(**values)


def test_detects_material_output_deviation():
    result = analyze_record(make_record())

    assert result.deviation_detected is True
    assert result.output_deviation_pct == -28.0
    assert result.defect_rate_pct == 8.4
    assert result.severity == "warning"
    assert "elevated downtime" in result.contributing_factors


def test_normal_run_is_not_flagged():
    result = analyze_record(
        make_record(
            actual_output=498,
            downtime_minutes=4,
            defect_count=5,
            total_units=500,
            machine_temperature_c=71.0,
            machine_status="RUNNING",
        )
    )

    assert result.deviation_detected is False
    assert result.severity == "normal"


def test_critical_machine_state_produces_critical_severity_when_deviation_exists():
    result = analyze_record(
        make_record(
            actual_output=390,
            machine_status="CRITICAL",
        )
    )

    assert result.deviation_detected is True
    assert result.severity == "critical"


def test_invalid_target_is_rejected():
    try:
        analyze_record(
            make_record(
                target_output=0
            )
        )

    except ValueError as exc:
        assert "target_output" in str(exc)

    else:
        raise AssertionError(
            "Expected ValueError"
        )
