# ❤️ Heart Disease Prediction Dashboard - Streamlit Web Application

## Overview

This is an **interactive web application** for AI-assisted heart disease prediction using the trained Random Forest model from the CCS 230 Final Project. The dashboard provides real-time clinical risk assessment with comprehensive visualizations and clinician-friendly interpretation.

## Features

### 🎯 **Risk Prediction Tab**
- **Random Forest Model** (Recommended): 86% accuracy, 88.89% recall
- **Decision Tree Model**: 81.33% accuracy, 79.17% recall
- Real-time risk scoring with confidence intervals
- Color-coded risk levels (Green/Yellow/Red)
- Clinical interpretation and actionable recommendations

### 📊 **Model Comparison Tab**
- Side-by-side performance metrics
- Accuracy, Recall, Precision, F1-Score comparison
- Clinical advantage explanation (Random Forest saves 7 additional lives per 72 cases)
- False negative reduction analysis (46.7% improvement)

### 🔬 **Cluster Analysis Tab**
- K-Means clustering for patient risk stratification
- Three distinct patient phenotypes:
  - **Cluster 0**: Young/Active (24.5% disease rate)
  - **Cluster 1**: Middle-aged Risk (63.7% disease rate)
  - **Cluster 2**: Older/Hypertensive (60.3% disease rate)
- Personalized intervention recommendations

### 📈 **Feature Analysis Tab**
- Feature importance visualization
- Clinical indicator assessment
- Patient's personal feature profile
- Benchmark against population norms

## Patient Input Parameters

### Demographics
- **Age**: 29-77 years
- **Sex**: Male/Female

### Cardiac Parameters
- **Resting Blood Pressure**: 94-200 mmHg
- **Cholesterol**: 126-564 mg/dL
- **Max Heart Rate**: 71-202 bpm
- **ST Depression (Oldpeak)**: 0-6.2 mm

### Diagnostic Parameters
- **Fasting Blood Sugar**: Yes/No (>120 mg/dL)
- **Chest Pain Type**: Typical/Atypical/Non-anginal/Asymptomatic
- **Resting ECG**: Normal/ST-T Abnormality/LV Hypertrophy
- **Exercise-Induced Angina**: Yes/No
- **ST Slope**: Up/Flat/Down

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager
- Virtual environment (recommended)

### Step 1: Clone/Navigate to Project Directory
```bash
cd "c:\Users\TONI\OneDrive\Desktop\Data Mining\Final project"
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
python -m venv streamlit_env
# Activate it
streamlit_env\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
streamlit run streamlit_app.py
```

The application will open in your default browser at `http://localhost:8501`

## Application Structure

```
streamlit_app.py
├── Page Configuration
├── Session State & Model Loading
├── Utility Functions
│   ├── get_risk_category()
│   ├── get_clinical_interpretation()
│   └── get_cluster_interpretation()
├── Sidebar (Patient Input)
└── Main Content (4 Tabs)
    ├── Risk Prediction
    ├── Model Comparison
    ├── Cluster Analysis
    └── Feature Analysis
```

## Clinical Interpretation Guide

### Risk Categories

**🔴 HIGH RISK (≥70% probability)**
- Immediate cardiologist referral required
- ECG and stress testing recommended
- Consider preventive medications
- Follow-up within 1-2 weeks

**🟠 MODERATE RISK (50-70% probability)**
- Close monitoring and further evaluation
- Cardiology consultation recommended
- Implement lifestyle modifications
- Follow-up in 2-4 weeks

**🟢 LOW RISK (<50% probability)**
- Continue routine monitoring
- Annual cardiovascular screening
- Maintain healthy lifestyle
- Follow scheduled checkups

## Model Performance Metrics

### Random Forest Classifier (RECOMMENDED)
| Metric | Value |
|--------|-------|
| Accuracy | 86.00% |
| Recall (Sensitivity) | 88.89% |
| Precision | 83.12% |
| F1-Score | 0.8591 |
| True Positives | 64 out of 72 |
| False Negatives | 8 |

### Decision Tree Classifier
| Metric | Value |
|--------|-------|
| Accuracy | 81.33% |
| Recall (Sensitivity) | 79.17% |
| Precision | 81.43% |
| F1-Score | 0.8028 |
| True Positives | 57 out of 72 |
| False Negatives | 15 |

### Clinical Advantage
- **7 Additional Cases Caught**: Random Forest identifies 7 more disease cases per cohort
- **46.7% FN Reduction**: Dangerous missed diagnoses reduced by nearly half
- **9.72% Recall Improvement**: Significant clinical advantage for patient safety

## Feature Importance Rankings

1. **ST Depression (Oldpeak)**: 0.35 - Strong predictor
2. **Age**: 0.22 - Moderate risk factor
3. **Resting BP**: 0.18 - Important factor
4. **Fasting BS**: 0.12 - Minor contributor
5. **Cholesterol**: 0.08 - Weak indicator
6. **Max Heart Rate**: 0.05 - Protective factor

## Cluster Characteristics

### Cluster 0: Young/Active Patients
- Average Age: 45.3 years
- Average Max HR: 158.5 bpm (excellent exercise capacity)
- Disease Rate: 24.5% (lowest risk)
- Recommendation: Routine preventive care

### Cluster 1: Middle-aged Risk Group
- Average Age: 58.7 years
- Average Max HR: 121.5 bpm (declining capacity)
- Disease Rate: 63.7% (highest risk)
- Recommendation: Intensive management

### Cluster 2: Older/Hypertensive
- Average Age: 55.9 years
- Average Resting BP: 147.2 mmHg (elevated)
- Disease Rate: 60.3% (high risk)
- Recommendation: BP control + preventive therapy

## Troubleshooting

### Issue: "ModuleNotFoundError" when running
**Solution**: Ensure all packages are installed
```bash
pip install -r requirements.txt
```

### Issue: Application runs slowly
**Solution**: This is normal for the first run. Streamlit caches resources after initialization.

### Issue: Port 8501 already in use
**Solution**: Run on a different port
```bash
streamlit run streamlit_app.py --server.port 8502
```

### Issue: Predictions seem incorrect
**Solution**: Ensure patient data is in realistic ranges and all fields are properly filled.

## Clinical Validation Notes

- **Model Training Data**: 840 patients (from 918 original, after cleaning)
- **Training Set**: 672 samples (80%)
- **Test Set**: 168 samples (20%)
- **Features**: 12 clinical parameters, one-hot encoded to 21 features
- **Train-Test Split**: Stratified to maintain class distribution

## Important Clinical Disclaimers

⚠️ **CLINICAL DISCLAIMER**: This dashboard is a **decision support tool only**. All predictions must be:
1. Validated by qualified healthcare professionals
2. Not used as a replacement for clinical judgment
3. Combined with comprehensive patient evaluation
4. Reviewed in context of complete patient history

## Data Sources

- **Dataset**: UCI Heart Disease Prediction Dataset
- **Records**: 840 valid patient records (after data cleaning)
- **Source**: https://archive.ics.uci.edu/ml/datasets/heart+disease

## Project Information

- **Course**: CCS 230 - Data Mining
- **Institution**: West Visayas State University (WVSU)
- **Project**: Heart Disease Prediction - Final Project
- **Deadline**: May 18, 2026
- **Team Members**: Baladjay, Dorado, Montenegro, Pontillas

## Contact & Support

For questions about the dashboard or data:
- Review the main Jupyter notebook: `Baladjay_Dorado_Montenegro_Pontillas.ipynb`
- Check the project report: `montenegro_CCS230_Finals.pdf`
- Refer to case study: `Case_Study_Report_Final.md`

## Version History

**v1.0** (May 16, 2026)
- Initial release
- Full model integration
- All 4 analysis tabs
- Clinical interpretation framework

---

**Last Updated**: May 16, 2026
**Status**: ✅ Production Ready
