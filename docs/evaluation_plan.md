## 1. Evaluation Objective

The evaluation aims to determine whether ProdAssist can:

1. Detect meaningful production deviations.
2. Correctly identify contributing indicators.
3. Provide understandable explanations.
4. Generate relevant recommendations.
5. Support a human production-management decision.
6. Record the human response to the recommendation.

The evaluation focuses on the usefulness and transparency of the digital assistance workflow rather than autonomous control.


## 2. Evaluation Framework

The evaluation follows the complete ProdAssist workflow:

Production Data
→
Deviation Detection
→
Explanation
→
Recommendation
→
Human Decision

Each stage is evaluated separately and then considered as part of the complete decision-support process.


## 3. Evaluation Dataset

The initial evaluation dataset consists of structured production records representing different production conditions.

The dataset should include examples of:

### Normal Conditions

Production output is close to target and machine and quality indicators remain within expected limits.

### Output Deviation

Actual output is materially below target.

### Downtime Condition

Production output is affected by elevated downtime.

### Quality Condition

Production output or performance is affected by an elevated defect rate.

### Machine Condition

Machine indicators such as temperature or machine status indicate a potentially abnormal condition.

### Multiple-Factor Deviation

Several indicators simultaneously indicate a potentially problematic production condition.

### Conflicting Indicators

One indicator indicates a problem while other indicators remain within expected ranges.

These scenarios are important for testing whether the system provides contextual rather than purely single-variable decisions.


## 4. Evaluation Metrics

### 4.1 Deviation Detection Accuracy

The system's detected condition is compared against the expected condition defined for each evaluation case.

For a labelled evaluation dataset:

    Detection Accuracy =
    Correctly Classified Cases / Total Evaluation Cases

Where appropriate, precision, recall, and F1-score may also be calculated.


## 5. Explanation Evaluation

Each explanation is evaluated against the indicators that actually triggered the system's assessment.

The evaluation considers:

### Correctness

Does the explanation accurately represent the underlying production data?

### Completeness

Does the explanation identify the important contributing indicators?

### Traceability

Can the explanation be traced back to measurable values in the production record?

### Clarity

Can a human user understand why the production record was flagged?

An explanation should not identify a factor that is unsupported by the underlying data.


## 6. Recommendation Evaluation

Recommendations are evaluated against the detected production condition.

The evaluation considers:

- Relevance
- Actionability
- Consistency
- Traceability
- Appropriateness to the detected condition

For example, a production record showing elevated downtime should produce a recommendation related to investigating downtime or machine/process conditions rather than an unrelated action.


## 7. Human Decision Evaluation

The human-in-the-loop component records the user's response to the system recommendation.

Possible decisions include:

- Investigate
- Accept
- Dismiss
- Escalate

The evaluation records:

- Recommended action
- Human decision
- Optional human comment
- Decision timestamp
- Production record
- Detected severity

This creates a traceable record of the interaction between the assistance system and the human decision-maker.


## 8. Decision Time

Where human testing is conducted, the time required to reach a decision may be measured.

A possible measure is:

    Decision Time =
    Time of Human Decision - Time of Case Presentation

The measure can be used to investigate whether the system provides information efficiently enough to support production-management decisions.

Decision time should not be interpreted independently of decision quality.


## 9. Human Acceptance and Rejection

The system may calculate:

    Acceptance Rate =
    Accepted Recommendations / Total Recommendations

and:

    Rejection Rate =
    Rejected or Dismissed Recommendations / Total Recommendations

These measures describe interaction patterns.

They should not automatically be interpreted as proof that a recommendation was correct or incorrect because a human may reject a recommendation for reasons that are not captured by the prototype.


## 10. Recommendation Relevance

Human evaluators may rate recommendations using a simple scale.

Example:

1. Not relevant
2. Slightly relevant
3. Moderately relevant
4. Relevant
5. Highly relevant

The evaluator should also be able to provide a short explanation for the rating.

The purpose is to assess whether recommendations correspond meaningfully to the detected production condition.


## 11. Explanation Understandability

Human evaluators may assess whether an explanation answers the question:

**"Why did ProdAssist flag this production condition?"**

A five-point scale may be used:

1. Very difficult to understand
2. Difficult to understand
3. Neutral
4. Easy to understand
5. Very easy to understand

The evaluation should also capture qualitative comments where possible.


## 12. Suggested Evaluation Scenarios

The following scenarios should be included in the demonstrator evaluation.

### Scenario A — Normal Production

Expected result:

- No significant deviation
- Normal status
- No unnecessary escalation

### Scenario B — Low Output

Expected result:

- Deviation detected
- Output shortfall identified
- Explanation identifies the output deviation
- Recommendation requests investigation

### Scenario C — High Downtime

Expected result:

- Production deviation detected where appropriate
- Downtime identified as a contributing factor
- Recommendation focuses on investigating downtime

### Scenario D — Quality Degradation

Expected result:

- Elevated defect rate identified
- Quality issue included in explanation
- Recommendation includes quality/process investigation

### Scenario E — Machine Condition

Expected result:

- Abnormal machine indicator identified
- Machine condition included in explanation
- Recommendation directs attention toward machine/process conditions

### Scenario F — Multiple Contributing Factors

Expected result:

- Multiple indicators identified
- Explanation combines the relevant factors
- Recommendation reflects the broader production condition

### Scenario G — Human Rejection

Expected result:

- System produces a recommendation
- Human selects "Dismiss"
- Decision is recorded
- System does not automatically override the human decision

### Scenario H — Human Escalation

Expected result:

- System identifies a potentially critical condition
- Human selects "Escalate"
- Decision is recorded for further investigation


## 13. Technical Testing

Automated tests should verify the core application behaviour.

### Analysis Tests

Test:

- Output deviation calculation
- Threshold detection
- Severity classification
- Contributing-factor detection
- Explanation generation
- Recommendation generation

### API Tests

Test:

- Health endpoint
- Production endpoint
- Production detail endpoint
- Dashboard/summary endpoints where implemented
- Invalid request handling

### Database Tests

Test:

- Database connection
- Production record persistence
- Retrieval of records
- Human decision persistence where implemented

### Frontend Tests

Where practical, test:

- API communication
- Rendering of production records
- Display of deviations
- Decision actions
- Error states


## 14. Research Evaluation Matrix

| Evaluation Area | Measure | Evidence |
|---|---|---|
| Deviation detection | Accuracy / Precision / Recall / F1 | Evaluation dataset |
| Explanation | Correctness and traceability | Expected vs generated explanation |
| Recommendation | Relevance and actionability | Human assessment |
| Human interaction | Acceptance/rejection/escalation | Decision records |
| Decision support | Decision time | Interaction timestamps |
| Transparency | Indicator-to-explanation traceability | Production data |
| Reliability | Automated test results | Pytest / CI |
| Reproducibility | Successful environment setup | Docker / repository |


## 15. Baseline

The initial baseline is a transparent rule-based system.

This provides a reference implementation against which future approaches can be compared.

Possible future comparisons include:

- Rule-based deviation detection
- Statistical anomaly detection
- Machine-learning anomaly detection
- Hybrid rule-based and machine-learning approaches

The baseline is intentionally transparent so that future improvements can be evaluated against a clearly understood starting point.


## 16. Evaluation Procedure

A complete evaluation can follow these steps:

1. Prepare the labelled evaluation dataset.
2. Run each production case through ProdAssist.
3. Record the detected condition.
4. Compare the system result with the expected condition.
5. Examine the generated explanation.
6. Verify that explanation factors are supported by the underlying data.
7. Examine the recommendation.
8. Have the human evaluator review the recommendation.
9. Record the human decision.
10. Record decision time where applicable.
11. Calculate quantitative metrics.
12. Review qualitative feedback.
13. Identify false positives and false negatives.
14. Identify weaknesses in explanations or recommendations.
15. Document findings and limitations.


## 17. Error Analysis

Incorrect or questionable results should be investigated rather than simply removed from the evaluation.

The analysis should distinguish between:

### False Positive

The system identifies a deviation where the expected condition is normal.

### False Negative

The system fails to identify a deviation that is present.

### Explanation Error

The system detects the correct condition but provides an explanation that is incomplete or unsupported.

### Recommendation Error

The system identifies the condition correctly but produces a recommendation that is not sufficiently relevant or actionable.

### Data Quality Error

The result is affected by missing, invalid, inconsistent, or incorrectly structured data.

Error analysis is important because the objective is not only to measure whether the system flags a condition, but also whether it provides useful decision support.


## 18. Evaluation Limitations

The initial evaluation has several limitations.

### Synthetic Dataset

Synthetic data cannot fully reproduce the complexity and variability of an industrial production environment.

### Limited Human Participants

A small demonstration involving a limited number of users cannot establish general conclusions about production-management users.

### Illustrative Thresholds

The thresholds used by the prototype require validation against real production data.

### Prototype Environment

The evaluation does not initially measure performance under a live industrial production environment.

### Domain Expertise

Industrial validation should involve production-management and domain experts.


## 19. Future Evaluation

Future research can expand the evaluation through:

- Real industrial datasets
- Longitudinal production data
- Multiple production lines
- Multiple machine types
- Expert user studies
- Controlled usability studies
- Comparison with existing production-management workflows
- Machine-learning baselines
- Real-time evaluation
- Digital-twin environments
- Larger human-in-the-loop studies

Future evaluation should also investigate whether the system improves decision quality, reduces unnecessary investigation time, and increases the transparency of production-management decisio

## 20. Success Criteria for the MVP

The MVP will be considered technically successful when:

1. Production data can be loaded and stored.
2. Production indicators can be calculated correctly.
3. Deviations can be detected using documented rules.
4. Contributing indicators can be identified.
5. Explanations can be generated from the underlying data.
6. Recommendations can be generated.
7. A human can make a decision through the interface.
8. The decision can be recorded.
9. The API and frontend operate together.
10. Automated tests pass.
11. The application runs through Docker Compose.
12. GitHub Actions successfully executes the test/build pipeline.
13. The methodology and limitations are documented.
14. The demonstrator can be reproduced from the repository.


## 21. Research Outcome

The intended outcome is a reproducible proof-of-concept demonstrating how a human-in-the-loop digital assistance system can transform structured production data into:

**Detection → Explanation → Recommendation → Human Decision**

The prototype provides a foundation for subsequent research into more advanced production-assistance systems, including statistical analysis, machine learning, explainable AI, digital twins, and networked production-management assistance.
