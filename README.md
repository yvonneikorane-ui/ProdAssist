# ProdAssist

## Human-in-the-Loop Digital Decision-Support Framework for Production Deviation Detection

ProdAssist is a research-oriented prototype of a digital assistance system for production management.

The system combines production, machine, and quality indicators to:

1. Detect production deviations
2. Identify contributing factors
3. Explain why a deviation was detected
4. Recommend an appropriate action
5. Present the recommendation to a human decision-maker
6. Record the human decision

The central principle is:

> The system assists the decision; the human makes the decision.

ProdAssist is therefore designed as a decision-support system rather than an autonomous production-control system.



# 1. Research Objective

The primary research objective is to investigate how production, machine, and quality indicators can be combined to detect meaningful production deviations and provide transparent explanations and actionable recommendations while keeping the human decision-maker in control.

## Docker provides containerization and GitHub Actions provides continuous integration.

Technology Stack

Backend: Python, FastAPI, Pandas, SQLAlchemy, Pydantic
Frontend: TypeScript, React, Vite, HTML/CSS
Database: PostgreSQL
Infrastructure: Docker, Docker Compose
CI/CD: GitHub Actions
Testing: Pytest

## Deviation Detection

ProdAssist initially uses transparent rule-based analysis.

The system calculates production output deviation:

((Actual Output - Target Output) / Target Output) × 100

It then evaluates contextual indicators such as downtime, defect rate, machine temperature, and machine status to identify contributing factors and classify the production condition.

The thresholds are configurable and documented as prototype assumptions rather than universal industrial standards.

## Human-in-the-Loop

ProdAssist does not automatically control production processes.

After detecting and explaining a deviation, the system presents a recommended action to the human decision-maker.

Possible decisions include:

Investigate
Accept
Dismiss
Escalate

The human decision is recorded, creating a traceable interaction between system assistance and human judgement.

## Research Prototype Status

ProdAssist is a reproducible proof-of-concept demonstrating:

Production-data analysis
Deviation detection
Contextual explanation
Action recommendation
Human decision capture
REST API
TypeScript/React interface
PostgreSQL persistence
Automated testing
Docker containerization
GitHub Actions CI

The current implementation uses synthetic/illustrative production data and transparent rule-based analysis.

## Limitations
Initial dataset is synthetic/illustrative.
Detection thresholds require validation against real production data.
The current analysis is rule-based rather than machine-learning based.
The prototype has not yet been validated in a live industrial environment.
Human evaluation is currently limited to prototype-level testing.

## Future Research

Potential extensions include:

Statistical and machine-learning anomaly detection
Time-series analysis
Predictive maintenance
Digital-twin integration
Real-time production data
Multi-machine production networks
Explainable AI
Operator feedback learning
Comparison of rule-based and machine-learning approaches

## Project Goal

To demonstrate a transparent, reproducible human-in-the-loop digital assistance system that transforms production data into detection, explanation, recommendation, and human decision support.

```text
Repository Structure
ProdAssist/
├── .github/workflows/ci.yml
├── backend/
│   ├── app/
│   └── tests/
├── data/
├── docs/
├── frontend/
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md


```text
The core workflow is:


Production Data
      ↓
Data Analysis
      ↓
Deviation Detection
      ↓
Explanation
      ↓
Recommendation
      ↓
Human Decision
      ↓
Decision Record


```text
The prototype uses a layered architecture:

React / TypeScript
        ↓
FastAPI REST API
        ↓
Python Analysis Layer
        ↓
PostgreSQL
