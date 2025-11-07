# 💊 Health Metrics Dashboard

An interactive Streamlit dashboard with exploratory data analysis (EDA) for anonymized patient health metrics — includes visualizations, filters, and insights on age, BMI, cholesterol, glucose, and disease prevalence.

---

## 🧠 Project Overview
This project performs full exploratory data analysis (EDA) and builds an interactive web-based dashboard to visualize anonymized patient health data.

The dataset includes demographic, lifestyle, and metabolic variables such as:
- **Age**
- **BMI**
- **Cholesterol**
- **Glucose**
- **Activity Level**
- **Disease Status**

The dashboard (built with **Streamlit** and **Plotly**) allows users to:
- Explore distributions of key health metrics  
- Apply dynamic filters (age range, cholesterol level, disease status, etc.)  
- View KPIs (average age, BMI, disease prevalence)  
- Visualize patterns and correlations among health indicators  
- Analyze trends in BMI, activity level, and glucose level  

---

## 🧰 Tech Stack
- **Python 3**
- **Streamlit** – for interactive dashboard
- **Plotly** – for dynamic visualizations
- **Pandas, NumPy** – for data processing
- **Seaborn, Matplotlib** – for EDA visualization
- **h5py** – for data generation and loading

---

## 📊 Features
✅ Data Cleaning and Preprocessing  
✅ Univariate and Bivariate EDA  
✅ Correlation Analysis  
✅ Group Comparisons (Healthy vs Diseased)  
✅ Interactive Filters for Age, Cholesterol, and Disease  
✅ Dynamic KPI Cards  
✅ Downloadable Filtered Data  

---

## 🧩 Folder Structure
```
health-metrics-dashboard/
├── app.py                         # Streamlit dashboard app
├── cleaned_health_metrics.csv      # Cleaned dataset
├── health_metrics.h5               # Raw dataset
├── data.ipynb                      # Jupyter notebook for data exploration
├── requirements.txt                # List of dependencies
└── README.md                       # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ullasmanjunatha/health-metrics-dashboard.git
cd health-metrics-dashboard
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app
```bash
streamlit run app.py
```

### 4️⃣ Open in your browser
Go to the URL shown in the terminal, typically:
```
http://localhost:8501
```

---

## 🧮 Example Insights
- Patients with **high cholesterol** or **very high glucose** show a higher disease prevalence.
- Disease rate increases significantly among **obese** and **low-activity** groups.
- Strong positive correlation between **BMI** and **glucose** levels.
- Majority of the dataset consists of individuals aged **36–65 years**.



## 🚀 Future Enhancements
- Add machine learning model to predict disease likelihood  
- Integrate database backend for live data  
- Enhance dashboard styling and responsiveness  
- Deploy on Streamlit Cloud or Heroku  

---

## 👤 Author
**Ullas Manjunatha**  
📧 Email: [your-email@example.com]  
🔗 GitHub: [https://github.com/ullasmanjunatha](https://github.com/ullasmanjunatha)

---

© 2025 Ullas Manjunatha — All rights reserved.
