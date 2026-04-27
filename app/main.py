import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="African Climate Insights Dashboard",
    page_icon="🌍",
    layout="wide"
)

sns.set_style("whitegrid")

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("🌍 African Climate Insights Dashboard")
st.markdown("Interactive dashboard for comparing climate patterns across five African countries.")

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
files = {
    "Ethiopia": "data/ethiopia_clean.csv",
    "Kenya": "data/kenya_clean.csv",
    "Nigeria": "data/nigeria_clean.csv",
    "Sudan": "data/sudan_clean.csv",
    "Tanzania": "data/tanzania_clean.csv"
}

dfs = []

for country, path in files.items():
    if os.path.exists(path):
        df = pd.read_csv(path)
        df["Country"] = country
        dfs.append(df)

if not dfs:
    st.error("No cleaned CSV files found in the data folder.")
    st.stop()

df = pd.concat(dfs, ignore_index=True)

# ---------------------------------------------------
# DATE PROCESSING
# ---------------------------------------------------
if "DATE" in df.columns:
    df["DATE"] = pd.to_datetime(df["DATE"])
    df["YEAR"] = df["DATE"].dt.year
else:
    st.error("DATE column not found in datasets.")
    st.stop()

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------
st.sidebar.header("🔍 Filters")

countries = st.sidebar.multiselect(
    "Select Countries",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=int(df["YEAR"].min()),
    max_value=int(df["YEAR"].max()),
    value=(2015, 2026)
)

variable_labels = {
    "Temperature (T2M)": "T2M",
    "Rainfall (PRECTOTCORR)": "PRECTOTCORR",
    "Humidity (RH2M)": "RH2M"
}

selected_label = st.sidebar.selectbox(
    "Select Variable",
    list(variable_labels.keys())
)

variable = variable_labels[selected_label]

# ---------------------------------------------------
# FILTER DATA
# ---------------------------------------------------
filtered = df[
    (df["Country"].isin(countries)) &
    (df["YEAR"] >= year_range[0]) &
    (df["YEAR"] <= year_range[1])
]

# ---------------------------------------------------
# KPI METRICS
# ---------------------------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Countries Selected", len(countries))
col2.metric("Years Covered", f"{year_range[0]} - {year_range[1]}")
col3.metric("Records Loaded", f"{len(filtered):,}")

st.markdown("---")

# ---------------------------------------------------
# CLIMATE TREND CHART
# ---------------------------------------------------
st.subheader("📈 Climate Trend Comparison")

trend = filtered.groupby(["YEAR", "Country"])[variable].mean().reset_index()

fig, ax = plt.subplots(figsize=(12, 5))

sns.lineplot(
    data=trend,
    x="YEAR",
    y=variable,
    hue="Country",
    marker="o",
    linewidth=2,
    ax=ax
)

ax.set_title(f"Average {selected_label} Over Time")
ax.set_xlabel("Year")
ax.set_ylabel(selected_label)

st.pyplot(fig)

# ---------------------------------------------------
# PRECIPITATION BOXPLOT
# ---------------------------------------------------
st.subheader("🌧️ Precipitation Distribution")

fig2, ax2 = plt.subplots(figsize=(12, 5))

sns.boxplot(
    data=filtered,
    x="Country",
    y="PRECTOTCORR",
    ax=ax2
)

ax2.set_title("Rainfall Distribution by Country")
ax2.set_xlabel("Country")
ax2.set_ylabel("PRECTOTCORR (mm/day)")

st.pyplot(fig2)

# ---------------------------------------------------
# DOWNLOAD BUTTON
# ---------------------------------------------------
st.subheader("⬇️ Download Filtered Dataset")

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_climate_data.csv",
    mime="text/csv"
)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")
st.caption("Climate Challenge Dashboard | Built with Streamlit | Interactive Climate Analytics")