The Stage 1 dataset must satisfy these conditions:

- `production_id` is unique.
- All required fields are present.
- `target_output` is greater than zero.
- `actual_output` is zero or greater.
- `downtime_minutes` is zero or greater.
- `defect_count` is zero or greater.
- `total_units` is greater than zero.
- `defect_count` does not exceed `total_units`.
- Machine identifiers are `M-A01`, `M-A02` or `M-A03`.
- Shift values are `A` or `B`.
- Machine status is `RUNNING`, `WARNING` or `CRITICAL`.
- Timestamps use ISO 8601-compatible notation.

The dataset is synthetic and does not establish industrial validity.

Thresholds in the analytical layer are demonstrator assumptions and require validation with representative production data and domain experts.
