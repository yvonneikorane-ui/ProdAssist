| Field | Type | Unit / Format | Description |
|---|---|---|---|
| `production_id` | string | P#### | Unique production observation identifier |
| `timestamp` | datetime | ISO 8601 | Observation date and time |
| `machine_id` | string | M-A## | Production machine identifier |
| `product_type` | string | category | Product manufactured |
| `order_id` | string | ORD-### | Production order identifier |
| `shift` | string | A / B | Production shift |
| `target_output` | integer | units | Planned production quantity |
| `actual_output` | integer | units | Actual production quantity |
| `downtime_minutes` | integer | minutes | Recorded downtime |
| `defect_count` | integer | units | Defective units |
| `total_units` | integer | units | Units included in quality observation |
| `machine_temperature_c` | decimal | °C | Machine temperature |
| `machine_status` | string | RUNNING / WARNING / CRITICAL | Recorded machine state |

## Derived indicators

These are calculated later and are not stored in the raw CSV.

### Output deviation

(actual_output - target_output) / target_output * 100
