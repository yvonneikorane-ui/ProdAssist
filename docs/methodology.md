## 1. Research Context

ProdAssist is a human-in-the-loop digital decision-support demonstrator for production management.

The system investigates how production, machine, and quality indicators can be combined to identify production deviations, explain the factors contributing to those deviations, and provide actionable recommendations to a human production manager or operator.

ProdAssist is designed as a decision-support system rather than an autonomous control system. The system does not automatically modify production processes or machine parameters. Instead, it presents analytical findings and recommendations while leaving the final decision to the human user.


## 2. Research Objective

The primary objective is to develop and evaluate a transparent digital assistance framework that supports production management decisions when production performance deviates from expected conditions.

The demonstrator follows the workflow:

Production Data
→
Data Analysis
→
Deviation Detection
→
Explanation
→
Recommendation
→
Human Decision
→
Decision Record

The research focuses on whether this workflow can provide useful, understandable, and actionable assistance to production decision-makers.


## 3. Research Question

### Primary Research Question

How can production, machine, and quality indicators be combined to detect meaningful production deviations and provide transparent explanations and actionable recommendations while keeping the human decision-maker in control?

### Supporting Questions

1. Which production indicators provide useful signals for identifying deviations from expected production performance?

2. How can multiple indicators be combined to distinguish normal production conditions from potentially problematic conditions?

3. How can a digital assistance system explain why a deviation has been detected?

4. How can detected deviations be translated into actionable recommendations?

5. How can human decisions and responses to recommendations be captured for subsequent evaluation?



## 4. Research Approach

ProdAssist uses a design-and-evaluation approach.

The research process consists of the following stages:

1. Define the production-management decision problem.
2. Define relevant production, machine, and quality indicators.
3. Construct a structured production dataset.
4. Implement transparent deviation-detection rules.
5. Generate contextual explanations from contributing indicators.
6. Generate recommendations based on detected conditions.
7. Present findings through a web-based assistance interface.
8. Allow the human user to accept, dismiss, investigate, or escalate a recommendation.
9. Record the human decision.
10. Evaluate detection, explanation, recommendation, and interaction performance.

The initial demonstrator uses deterministic analytical rules rather than a machine-learning model. This makes the reasoning process explicit and reproducible and provides a foundation for future comparison with statistical or machine-learning approaches.


## 5. Data Model

ProdAssist uses production records containing three primary categories of information.

### Production Indicators

Examples include:

- Target production quantity
- Actual production quantity
- Output deviation
- Production duration
- Downtime

### Machine Indicators

Examples include:

- Machine identifier
- Machine status
- Temperature
- Operating condition
- Downtime

### Quality Indicators

Examples include:

- Defect quantity
- Defect rate
- Quality status

The dataset is designed to represent production scenarios rather than real confidential industrial data.

All synthetic or illustrative data used by the demonstrator must be clearly identified as such.


## 6. Deviation Detection

Deviation detection is based on transparent thresholds and relationships between production indicators.

For each production record, ProdAssist calculates relevant performance indicators.

### Output Deviation

Output deviation is calculated as:

    output_deviation_percentage =
        ((actual_output - target_output) / target_output) * 100

A negative value indicates production below the target.

### Example

If:

- Target output = 500 units
- Actual output = 392 units

Then:

    ((392 - 500) / 500) * 100 = -21.6%

The system therefore identifies a significant negative output deviation.


## 7. Contributing Indicators

Output deviation is not evaluated in isolation.

ProdAssist examines additional indicators that may provide contextual information, including:

- Downtime
- Defect rate
- Machine temperature
- Machine status
- Production duration

For example, a low production output combined with elevated downtime and increased defect rate provides a different context from low output occurring while machine and quality indicators remain normal.

The purpose of combining indicators is to provide a more informative explanation of the production condition.


## 8. Rule-Based Assessment

The initial demonstrator uses explicit rules.

Illustrative rules include:

### Output Rule

If output deviation is below the defined threshold, flag the production record for investigation.

### Downtime Rule

If downtime exceeds the defined threshold, identify downtime as a contributing factor.

### Quality Rule

If defect rate exceeds the defined threshold, identify quality performance as a contributing factor.

### Temperature Rule

If machine temperature exceeds the defined threshold, identify elevated temperature as a contributing machine condition.

### Machine Status Rule

If the machine is reported as stopped, critical, or otherwise abnormal, identify the machine state as a contributing factor.

The thresholds are configurable and are considered demonstrator assumptions rather than universal industrial standards.


## 9. Severity Classification

ProdAssist assigns a condition based on the combination and severity of detected indicators.

The initial conceptual categories are:

- Normal
- Warning
- Critical

Severity is determined using transparent rules rather than an opaque model.

The exact thresholds are documented in the application configuration and data-quality documentation so that they can be modified for future industrial datasets.


## 10. Explanation Generation

For each detected deviation, ProdAssist generates an explanation based on the indicators that triggered the assessment.

Example:

> Actual output was 21.6% below target. Elevated downtime and defect rate were also detected, while the machine temperature exceeded the configured threshold.

The explanation is intended to answer:

**"Why did the system flag this production record?"**

The explanation should be traceable to measurable indicators in the underlying production record.


## 11. Recommendation Generation

Following deviation detection and explanation, ProdAssist generates a recommended action.

Recommendations are contextual rather than automatic commands.

Examples include:

- Investigate production run
- Review machine condition
- Review downtime causes
- Inspect quality-related process conditions
- Escalate for further investigation

The recommendation does not directly control the machine or production process.


## 12. Human-in-the-Loop Decision

The human user remains responsible for the final decision.

The interface provides decision actions such as:

- Investigate
- Accept
- Dismiss
- Escalate

The selected decision is recorded together with the relevant production record.

This creates a human-in-the-loop feedback point between system recommendation and operational decision-making.


## 13. System Architecture

The demonstrator consists of the following logical layers:

### Data Layer

Production records stored in PostgreSQL.

### Analysis Layer

Python-based analytical logic responsible for:

- Calculating production indicators
- Detecting deviations
- Identifying contributing factors
- Assigning severity
- Generating explanations
- Generating recommendations

### API Layer

FastAPI exposes the analytical functionality and production records to the user interface.

### Interface Layer

A TypeScript/React web interface presents:

- Production overview
- Production records
- Detected deviations
- Explanations
- Recommendations
- Human decisions

### Infrastructure Layer

Docker provides containerized execution.

GitHub Actions provides automated testing and continuous integration.


## 14. Technology Stack

The demonstrator uses:

- Python
- FastAPI
- Pandas
- SQLAlchemy
- PostgreSQL
- TypeScript
- React
- Vite
- HTML/CSS
- Docker
- Docker Compose
- GitHub Actions
- Pytest

The technology choices support a web-based, containerized, testable digital assistance demonstrator.


## 15. Reproducibility

The project is designed so that another researcher or developer can reproduce the demonstrator using the repository.

Reproducibility is supported through:

- Version-controlled source code
- Structured CSV data
- Documented assumptions
- Automated tests
- Docker configuration
- Dependency versioning
- GitHub Actions continuous integration
- Documented research methodology


## 16. Assumptions

The initial demonstrator assumes that:

1. Production records are available in a structured format.
2. Target and actual production quantities are measurable.
3. Machine and quality indicators can be associated with production records.
4. The configured thresholds are suitable for demonstration purposes.
5. The production dataset is sufficiently structured for analytical processing.
6. Human users can review the recommendations through the web interface.

These assumptions must be validated against real production environments before industrial deployment.


## 17. Limitations

The current demonstrator has several limitations.

### Synthetic Data

The initial dataset is demonstrative and does not represent a validated industrial production dataset.

### Rule-Based Analysis

The initial system uses explicit rules rather than machine-learning models.

### Threshold Validity

The thresholds are illustrative and may not be appropriate for every machine, product, process, or production environment.

### Limited Context

The demonstrator does not yet incorporate all possible production-management variables such as:

- Operator information
- Maintenance history
- Material availability
- Energy consumption
- Supply-chain conditions
- Shift patterns
- Historical machine failure data

### Human Evaluation

The initial implementation does not yet provide a large-scale human-subject evaluation.


## 18. Future Research

Future development may investigate:

- Machine-learning-based anomaly detection
- Time-series analysis
- Predictive maintenance indicators
- Digital-twin integration
- Historical production learning
- More advanced recommendation models
- Confidence scores
- Explainable AI techniques
- Operator feedback learning
- Multi-machine production networks
- Real-time production data
- Integration with industrial systems
- Comparative evaluation of rule-based and machine-learning approaches

These extensions would allow the demonstrator to evolve from a transparent research prototype toward a more advanced production assistance system.


## 19. Research Principle

The central design principle of ProdAssist is:

**The system assists the decision; the human makes the decision.**

The demonstrator therefore prioritizes transparency, traceability, explainability, and human control over fully autonomous decision-making.
