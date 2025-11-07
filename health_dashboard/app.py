# app.py — Basic Streamlit Health Data Dashboard

import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration

st.set_page_config(
    page_title="Health Metrics Dashboard",
    page_icon="💊",
    layout="wide"
)


# Load Data

@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_health_metrics.csv")
    return df

df = load_data()

st.title("💊 Health Metrics Dashboard")
st.markdown("An interactive dashboard to explore anonymized patient health metrics.")


# Sidebar Filters

st.sidebar.header("🔍 Filters")

# Age range filter
age_min, age_max = int(df["Age"].min()), int(df["Age"].max())
age_range = st.sidebar.slider("Select Age Range:", age_min, age_max, (age_min, age_max))

# Disease status filter
disease_options = st.sidebar.multiselect(
    "Select Disease Status:",
    options=df["Has_Disease"].unique(),
    default=df["Has_Disease"].unique()
)

# Cholesterol filter
chol_options = st.sidebar.multiselect(
    "Select Cholesterol Levels:",
    options=df["Cholesterol"].unique(),
    default=df["Cholesterol"].unique()
)

# Apply filters
df_filtered = df[
    (df["Age"].between(age_range[0], age_range[1])) &
    (df["Has_Disease"].isin(disease_options)) &
    (df["Cholesterol"].isin(chol_options))
]

st.sidebar.markdown("---")
st.sidebar.write(f"Total Records Shown: **{len(df_filtered)}**")


# Main Dashboard Content


# KPIs
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Average Age", f"{df_filtered['Age'].mean():.1f} yrs")
with col2:
    st.metric("Average BMI", f"{df_filtered['BMI'].mean():.1f}")
with col3:
    disease_rate = (df_filtered["Has_Disease"].mean() * 100)
    st.metric("Disease Prevalence", f"{disease_rate:.1f}%")

st.markdown("---")

# Plots


# Age Distribution
fig_age = px.histogram(df_filtered, x="Age", nbins=20, title="Age Distribution", color_discrete_sequence=["skyblue"])
st.plotly_chart(fig_age, use_container_width=True)

# BMI Distribution
fig_bmi = px.histogram(df_filtered, x="BMI", nbins=20, title="BMI Distribution", color_discrete_sequence=["lightgreen"])
st.plotly_chart(fig_bmi, use_container_width=True)

# Cholesterol vs Disease
fig_chol = px.histogram(
    df_filtered,
    x="Cholesterol",
    color="Has_Disease",
    barmode="group",
    title="Cholesterol Level vs Disease Status",
    color_discrete_sequence=px.colors.qualitative.Set2
)
st.plotly_chart(fig_chol, use_container_width=True)

# Activity Level
fig_act = px.histogram(
    df_filtered,
    x="Activity_Level",
    nbins=10,
    title="Activity Level Distribution",
    color_discrete_sequence=["orange"]
)
st.plotly_chart(fig_act, use_container_width=True)


# Data Table

st.markdown("### 📋 Filtered Data Preview")
st.dataframe(df_filtered.head(20))
