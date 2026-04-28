# 📓 Notebooks Directory

This folder contains all Jupyter Notebooks developed for the **Climate Challenge Week 0** project.

The notebooks cover country-level climate data cleaning, exploratory data analysis (EDA), and cross-country climate comparisons using datasets from five African countries.

---

# 📂 Included Notebooks

## Country-Level EDA

* `ethiopia_eda.ipynb` – Climate analysis for Ethiopia
* `kenya_eda.ipynb` – Climate analysis for Kenya
* `nigeria_eda.ipynb` – Climate analysis for Nigeria
* `sudan_eda.ipynb` – Climate analysis for Sudan
* `tanzania_eda.ipynb` – Climate analysis for Tanzania

Each notebook includes:

* Data loading and preprocessing
* Missing value treatment (`-999` replacement)
* Duplicate removal
* Date parsing (`YEAR` + `DOY`)
* Outlier detection using Z-scores
* Monthly temperature trend analysis
* Rainfall seasonality analysis
* Correlation heatmaps
* Scatter plots for climate relationships
* Distribution analysis
* Markdown interpretations and findings

---

## Cross-Country Comparison

* `compare_countries.ipynb`

This notebook combines all cleaned datasets and performs comparative analysis across the five countries.

### Includes:

* Temperature trend comparison
* Rainfall variability comparison
* Extreme heat event frequency
* Dry-day analysis
* Statistical significance testing (ANOVA)
* Climate vulnerability ranking

---

# 🌍 Countries Covered

* Ethiopia
* Kenya
* Nigeria
* Sudan
* Tanzania

---

# ▶️ How to Use

Open any notebook using Jupyter Notebook or VS Code:

```bash id="j6n6tz"
jupyter notebook
```

or

```bash id="4mxs8e"
code .
```

Then navigate to the `notebooks/` folder.

---

# 📌 Notes

* Cleaned CSV files are stored locally in the `data/` folder and excluded from GitHub.
* Each notebook is self-contained and includes markdown explanations for all visualizations.
* Recommended execution environment: Python virtual environment with packages listed in `requirements.txt`.

---

# 📈 Purpose

These notebooks were created to generate data-driven climate insights relevant to **COP32 policy discussions**, focusing on regional warming, precipitation instability, drought exposure, and climate vulnerability across Africa.
