# 🌍 Climate Challenge Week 0

## Cross-Country Climate Data Analysis for COP32 Readiness

This repository contains a complete climate data analysis project focused on five African countries:

* Ethiopia
* Kenya
* Nigeria
* Sudan
* Tanzania

The project combines **Git best practices, data cleaning, exploratory data analysis (EDA), cross-country comparison, climate vulnerability ranking, and an interactive dashboard** to generate evidence-based insights relevant to **COP32 climate policy discussions**.


# 📌 Project Objectives

The challenge was completed in four parts:

1. **Task 1:** Git & Environment Setup
2. **Task 2:** Data Profiling, Cleaning & Country-Level EDA
3. **Task 3:** Cross-Country Comparison & Climate Vulnerability Ranking
4. **Bonus Task:** Interactive Streamlit Dashboard

# 🛠 Tech Stack

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy
* Streamlit
* Git
* GitHub Actions

# 📂 Repository Structure

```text
climate-challenge-week0/
│── .github/
│   └── workflows/
│       └── ci.yml
│
│── app/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
│
│── notebooks/
│   ├── ethiopia_eda.ipynb
│   ├── kenya_eda.ipynb
│   ├── nigeria_eda.ipynb
│   ├── sudan_eda.ipynb
│   ├── tanzania_eda.ipynb
│   └── compare_countries.ipynb
│
│── scripts/
│── tests/
│── requirements.txt
│── README.md
│── .gitignore
```

> `data/` and cleaned CSV files are intentionally excluded via `.gitignore`.


# ✅ Task 1: Git & Environment Setup

## Deliverables

* Initialized GitHub repository: `climate-challenge-week0`
* Configured Python virtual environment
* Added `.gitignore`
* Added `requirements.txt`
* Added GitHub Actions CI workflow
* Used Conventional Commits
* Merged setup branch into `main`

## Example Commits

```text
init: add .gitignore
chore: venv setup
ci: add GitHub Actions workflow
```

## CI Workflow

GitHub Actions runs dependency installation and environment checks on push to `main`.

# 📊 Task 2: Country-Level Data Profiling, Cleaning & EDA

Separate notebooks were created for each country:

* `ethiopia_eda.ipynb`
* `kenya_eda.ipynb`
* `nigeria_eda.ipynb`
* `sudan_eda.ipynb`
* `tanzania_eda.ipynb`

## Workflow Per Country

### Data Cleaning

* Loaded raw CSV files using Pandas
* Replaced NASA missing-value sentinel `-999` with `NaN`
* Removed duplicate rows
* Parsed `YEAR` + `DOY` into proper dates
* Created `Month` column
* Exported cleaned datasets locally

### Outlier Detection

Z-score analysis performed on:

* T2M
* T2M_MAX
* T2M_MIN
* PRECTOTCORR
* RH2M
* WS2M
* WS2M_MAX

### Exploratory Data Analysis

#### Time Series

* Monthly average temperature trends
* Monthly rainfall totals
* Warmest / coolest months
* Rainy season identification

#### Correlation Analysis

* Correlation heatmaps
* Scatter plots:

  * T2M vs RH2M
  * T2M_RANGE vs WS2M

#### Distribution Analysis

* Rainfall histograms
* Bubble charts:

  * Temperature vs Humidity
  * Bubble size = Rainfall

Each notebook includes markdown insights and interpretations.


# 🌍 Task 3: Cross-Country Comparison & Climate Vulnerability Ranking

Notebook:

```text
notebooks/compare_countries.ipynb
```

## Countries Compared

* Ethiopia
* Kenya
* Nigeria
* Sudan
* Tanzania

## Analyses Performed

### Temperature Comparison

* Monthly average T2M line chart (2015–2026)
* Mean / Median / Std summary table

### Precipitation Comparison

* Side-by-side rainfall boxplots
* Mean / Median / Std summary table

### Extreme Events

* Days above 35°C
* Consecutive dry days (<1 mm rainfall)

### Statistical Testing

* One-way ANOVA across countries

### Climate Vulnerability Index

A normalized composite score based on:

* Average temperature
* Rainfall variability
* Extreme heat frequency
* Dry-day frequency

## Final Ranking

1. Sudan
2. Tanzania
3. Nigeria
4. Kenya
5. Ethiopia

## Key Finding

Sudan emerged as the most climate-vulnerable country due to:

* Highest average temperatures
* Highest dry-day frequency
* Significant extreme heat exposure


# 🚀 Bonus Task: Interactive Dashboard

Branch:

```text
dashboard-dev
```

Main app:

```text
app/main.py
```

## Features

* Country multi-select filter
* Year range slider
* Variable selector (Temperature / Rainfall / Humidity)
* Climate trend line chart
* Rainfall distribution boxplot
* KPI summary metrics
* Download filtered data option

## Run Locally

```bash
streamlit run app/main.py
```


# 📈 Key Insights from the Project

* Sudan shows the strongest combined heat and drought stress.
* Tanzania exhibits high rainfall instability.
* Nigeria demonstrates warming with moderate variability.
* Kenya faces recurring dry-day exposure.
* Ethiopia remains climate-sensitive due to rainfall dependence.


# ⚙️ Installation & Reproducibility

## Clone Repository

```bash
git clone https://github.com/eyerus-getachew/climate-challenge-week0
cd climate-challenge-week0
```

## Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

## Install Requirements

```bash
pip install -r requirements.txt
```


# 🌿 Branch Structure

```text
main
setup-task
eda-ethiopia
eda-kenya
eda-nigeria
eda-sudan
eda-tanzania
compare-countries
dashboard-dev
```


# 📌 Final Outcome

This project demonstrates practical skills in:

* Version control with Git
* Reproducible environments
* Data cleaning
* Exploratory data analysis
* Statistical testing
* Climate risk ranking
* Dashboard development
* Communicating policy-relevant insights 
