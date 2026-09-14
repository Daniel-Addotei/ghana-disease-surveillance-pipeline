# Ghana Disease Surveillance Data Pipeline

## Overview

The **Ghana Disease Surveillance Data Pipeline** is a learning and portfolio project for developing practical data engineering skills using a public health surveillance use case.

The project explores how data from multiple public health information sources can be collected, structured, transformed, stored, and prepared for analysis and decision-making.

The project is being developed progressively as part of my Data Engineering studies, beginning with Python fundamentals and advancing through Pandas, SQL, PostgreSQL, ETL, data pipelines, and analytical outputs.

---

## Public Health Context

Public health decision-making depends on data generated from multiple systems and sources, including:

- DHIMS2
- SORMAS
- Laboratory information systems
- Hospital information systems
- Field investigation reports
- Outbreak line lists
- Health facilities and districts

These data may exist in different formats and structures.

A data engineering pipeline provides a systematic way to move data from these different sources into a structured environment where they can be cleaned, integrated, analysed, and used for public health intelligence.

The conceptual workflow for this project is:

```text
DHIMS2 ──────────────┐
SORMAS ──────────────┤
Laboratory Systems ──┤
Hospital Systems ────┼──> Data Ingestion
Field Reports ───────┤
Other Data Sources ──┘
                           │
                           ▼
                    Python / Pandas
                           │
                           ▼
                  Cleaning & Transformation
                           │
                           ▼
                       PostgreSQL
                           │
                           ▼
                Integrated Public Health Data
                           │
                    ┌──────┴──────┐
                    ▼             ▼
                Analysis       Reporting
                    │             │
                    ▼             ▼
               Dashboards       SitReps
```

---

## Learning Objectives

Through this project, I aim to develop practical skills in:

1. Python programming for data engineering
2. Working with lists, dictionaries, and other Python data structures
3. Data manipulation using Pandas
4. SQL and relational database concepts
5. PostgreSQL database development
6. Data Definition Language (DDL)
7. Data cleaning and transformation
8. Extract, Transform, Load (ETL) workflows
9. Database integration with Python
10. Development of reproducible data pipelines
11. Data quality and validation
12. Preparation of data for dashboards, Situation Reports (SitReps), and public health decision-making

---

## Project Architecture

The project is being developed using the following structure:

```text
ghana-disease-surveillance-pipeline/
│
├── config/              # Configuration files
│
├── dags/                # Workflow orchestration scripts
│
├── data/
│   ├── raw/             # Original source data
│   ├── processed/       # Cleaned and transformed data
│   └── reference/       # Reference data
│
├── docs/                # Project documentation
│
├── logs/                # Pipeline logs
│
├── notebooks/           # Exploratory analysis and learning notebooks
│
├── scripts/             # Python data engineering scripts
│
├── sql/                 # PostgreSQL and SQL scripts
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Current Python Work

The `scripts/` directory contains exercises used to build the Python foundations required for data engineering.

Current scripts include:

```text
hello_public_health.py
surveillance_lists.py
surveillance_dictionary.py
first_dataframe.py
surveillance_dataset.py
```

These scripts progressively introduce Python concepts using public health surveillance examples.

### Example progression

```text
Python variables
      ↓
Lists
      ↓
Dictionaries
      ↓
Pandas DataFrames
      ↓
Structured surveillance datasets
      ↓
Database loading
      ↓
Data pipelines
```

---

## Database Development

The next stage of the project introduces relational database development using **PostgreSQL**.

The planned database is:

```text
ghana_public_health
│
├── districts
├── facilities
├── events
├── surveillance_cases
└── laboratory_results
```

The database will be developed progressively to demonstrate:

- `CREATE DATABASE`
- `CREATE TABLE`
- Data types
- Primary keys
- Foreign keys
- Constraints
- Table relationships
- Data insertion
- Data modification
- SQL queries
- Joins
- Data quality rules

### Proposed relationships

```text
districts
    │
    ├──────── facilities
    │             │
    │             ▼
    │      surveillance_cases
    │             │
    │             ▼
    │      laboratory_results
    │
    └────────── events
```

The exact schema will evolve as database design concepts are introduced.

---

## Data Engineering Roadmap

### Phase 1 — Python Foundations
- [x] Python environment setup
- [x] Variables and basic Python syntax
- [x] Lists
- [x] Dictionaries
- [x] Introduction to Pandas
- [x] Creating DataFrames

### Phase 2 — SQL and Databases
- [x] PostgreSQL installation
- [x] pgAdmin setup
- [ ] Create `ghana_public_health` database
- [ ] Create reference tables
- [ ] Create surveillance tables
- [ ] Create laboratory tables
- [ ] Define primary and foreign keys
- [ ] Practice SQL queries and joins

### Phase 3 — Data Engineering
- [ ] Import CSV data
- [ ] Extract data from source files
- [ ] Clean and transform data with Pandas
- [ ] Load transformed data into PostgreSQL
- [ ] Develop reusable ETL scripts
- [ ] Implement data validation and quality checks

### Phase 4 — Pipeline Development
- [ ] Automate ETL processes
- [ ] Introduce workflow orchestration
- [ ] Add logging
- [ ] Add error handling
- [ ] Add pipeline monitoring

### Phase 5 — Public Health Intelligence
- [ ] Generate surveillance indicators
- [ ] Prepare analysis-ready datasets
- [ ] Produce automated summary outputs
- [ ] Develop dashboard-ready datasets
- [ ] Support automated Situation Report outputs

---

## Technologies

The project currently uses or plans to introduce:

| Technology | Purpose |
|---|---|
| Python | Data processing and pipeline development |
| Pandas | Data manipulation and transformation |
| NumPy | Numerical operations |
| PostgreSQL | Relational data storage |
| SQL | Database definition and querying |
| pgAdmin | PostgreSQL administration |
| VS Code | Development environment |
| Git | Version control |
| GitHub | Code repository and project documentation |

Additional tools will be introduced as the project progresses.

---

## Data Governance

This repository is intended for learning and demonstration.

Public health examples used in the project should use **simulated, synthetic, anonymised, or otherwise appropriate training data**. Personally identifiable information, confidential surveillance data, database passwords, API credentials, and other sensitive information should not be committed to the repository.

Environment variables and credentials should be stored locally and excluded through `.gitignore`.

---

## Expected Outcome

The final project will demonstrate an end-to-end public health data engineering workflow:

```text
SOURCE SYSTEMS
      ↓
EXTRACT
      ↓
TRANSFORM
      ↓
VALIDATE
      ↓
LOAD
      ↓
POSTGRESQL
      ↓
ANALYSIS-READY DATA
      ↓
PUBLIC HEALTH INTELLIGENCE
      ↓
DASHBOARDS / SITREPs / DECISION SUPPORT
```

The goal is not only to learn individual programming commands, but to understand how Python, SQL, databases, and data pipelines work together to support timely and reliable public health decision-making.

---

## Project Status

**Status:** In development

**Current focus:** Python/Pandas foundations and introduction to SQL/PostgreSQL database development.

---

## Author

**Daniel Addotei Kpakpo**

Public health epidemiology, surveillance intelligence, health informatics, and data engineering.