# CCS 230 Final Project: Heart Disease Prediction

## 📋 Project Overview

This is a comprehensive data mining and machine learning project that includes:
1. **Exploratory Data Analysis (EDA)** - Understand data distributions and patterns
2. **Data Cleaning** - Remove invalid/duplicate records
3. **Association Rule Mining** - Discover symptom combinations
4. **Classification Models** - Decision Tree & Random Forest predictors
5. **Case Study Report** - Professional report for hospital executives

---

## 📁 Project Files

```
Final project/
├── heart.csv                           # Main dataset (918 patients, 12 features)
├── Montenegro_CCS230_Finals.ipynb      # MAIN NOTEBOOK - Contains all analysis & models
├── Case_Study_Report_Template.md       # Template for professional report
└── README.md                           # This file
```

---

## 🚀 How to Use This Project

### Step 1: Run the Jupyter Notebook
```bash
jupyter notebook Montenegro_CCS230_Finals.ipynb
```

The notebook is structured with 10 sections:
1. Import libraries
2. Load & explore dataset
3. **EDA & Visualization** - Charts, histograms, correlation heatmaps
4. **Data Cleaning** - Remove invalid records
5. **One-Hot Encoding** - Convert categorical variables
6. **Association Rule Mining** - Find symptom patterns
7. **Decision Tree Model** - Build & train classifier
8. **Random Forest Model** - Build & train classifier
9. **Model Evaluation** - Compare performance metrics
10. **Confusion Matrix Analysis** - Analyze Recall (CRITICAL for medical diagnosis)

### Step 2: Execute All Cells
Run the notebook cells sequentially to:
- Generate visualizations (EDA charts)
- Calculate statistics
- Train both models
- Evaluate performance metrics
- Display confusion matrices

### Step 3: Write the Case Study Report
Use the template `Case_Study_Report_Template.md`:
1. Fill in your findings from the notebook
2. Insert chart/visualization images
3. Complete sections with model metrics
4. Focus on Recall and why it matters for medical diagnosis
5. Export to PDF for submission

---

## 📊 Key Sections Explained

### Section 3: Exploratory Data Analysis (EDA)
**What to Look For:**
- Age distribution by disease status
- Categorical feature relationships
- Correlation heatmap (which features most strongly predict disease?)
- Gender and chest pain type patterns

**Chart to Include in Report:** Correlation heatmap + Age distribution

---

### Section 6: Association Rule Mining
**What You'll Find:**
- Symptom combinations that predict disease
- Rules like: "If Patient is Asymptomatic AND has high Oldpeak, then Heart Disease (Confidence: 85%)"

**Report Focus:**
- Top 3-5 most confident rules
- Explain clinical relevance
- Show which symptom combinations are most dangerous

---

### Section 7 & 8: Classification Models

#### Decision Tree Model:
- Simple, interpretable rules
- Shows feature importance
- Can be explained to non-technical stakeholders

#### Random Forest Model:
- Ensemble of 100 decision trees
- Generally more accurate
- Reduces overfitting

**Report Focus:**
- Which model has highest accuracy?
- Which has highest precision?
- **Which has highest RECALL?** ⭐ (THIS IS CRITICAL)

---

### Section 10: Confusion Matrix Analysis ⚠️ MOST IMPORTANT

**Why This Matters:**
In medical diagnosis, **missing a disease** (False Negative) is worse than a false alarm:
- False Negative: Patient HAS disease but model says NO ❌ Patient doesn't get treatment
- False Positive: Patient doesn't have disease but model says YES ⚠️ Can be verified with more tests

**RECALL Formula:**
```
Recall = True Positives / (True Positives + False Negatives)
       = Number of diseased correctly identified / Total with disease
```

**For Your Report:**
- "Out of 100 patients WITH heart disease, our model correctly identifies X patients (X% Recall)"
- "Out of 100 patients WITHOUT disease, our model correctly rules them out (Y% Specificity)"
- "Critical insight: The model with higher recall misses fewer patients"

---

## 📈 Visualizations Generated

The notebook creates these visualizations for your report:

1. **Target Distribution** - Pie chart of disease vs no disease
2. **Age Distribution** - Histogram and box plot by disease status
3. **Categorical Features** - Bar charts showing relationships
4. **Correlation Heatmap** - Feature relationships
5. **Feature Importance** - Decision Tree vs Random Forest
6. **Confusion Matrices** - Side-by-side comparison
7. **Model Comparison** - Metrics comparison bar charts
8. **Recall Analysis** - Why one model is better

**To Export Charts for Report:**
- Right-click on chart → Save image
- Or use: `plt.savefig('chart_name.png')`

---

## 📝 Writing Your Case Study Report

### Structure (Use Template):
1. **Executive Summary** (1-2 pages)
   - What you found
   - Main recommendation
   - Why it matters

2. **Introduction** (1-2 pages)
   - Problem statement
   - Dataset overview
   - Why early heart disease detection matters

3. **Data Analysis** (2-3 pages)
   - Key demographics
   - Risk factors discovered
   - Symptom combinations from association rules

4. **Models** (2-3 pages)
   - How you built the models
   - Performance metrics
   - Feature importance

5. **Confusion Matrix & Clinical Impact** (2-3 pages) ⭐ CRITICAL SECTION
   - Explain True Positives, False Positives, True Negatives, False Negatives
   - Define Recall and why it's important
   - Show confusion matrices from both models
   - Explain which model is better and why

6. **Recommendation** (1 page)
   - Which model should hospital use?
   - Why? (highest recall = fewer missed diagnoses)

7. **Implementation Plan** (1-2 pages)
   - How to deploy the model
   - What to monitor
   - Expected benefits

### Tone & Audience:
- Write for **hospital executives** (not data scientists)
- Avoid jargon, explain technical terms
- Use real-world examples (e.g., "Out of 100 patients with disease, model identifies X")
- Emphasize clinical benefits and patient safety

### Key Points to Emphasize:
- ✓ Model helps catch diseases early
- ✓ Can prevent worse health outcomes
- ✓ Recalls is high (few missed patients)
- ✓ False positives can be verified with additional testing
- ✓ Cost-benefit: Early detection saves lives

---

## 🎯 Grading Rubric Alignment

Your submission will be evaluated on:

✅ **Phase 1: EDA & Data Cleaning**
- [ ] Visualizations showing data patterns
- [ ] Data cleaning documented
- [ ] One-Hot Encoding applied

✅ **Phase 2: Association Rule Mining**
- [ ] Apriori algorithm applied
- [ ] Rules generated and explained
- [ ] Symptoms/risk factor combinations identified

✅ **Phase 2: Classification Models**
- [ ] Decision Tree model built ✓
- [ ] Second model (Random Forest) built ✓
- [ ] Both models evaluated and compared

✅ **Phase 2: Confusion Matrix & Recall**
- [ ] Confusion matrices displayed
- [ ] Recall explained and emphasized
- [ ] False Negatives analyzed

✅ **Deliverables**
- [ ] Python notebook (Montenegro_CCS230_Finals.ipynb) submitted
- [ ] Case Study Report (PDF) submitted with all sections complete

---

## 💾 How to Submit

### File 1: Python Notebook
- File: `Montenegro_CCS230_Finals.ipynb`
- Contains: All code, visualizations, analysis

### File 2: Case Study Report (PDF)
- File: `Montenegro_CCS230_Finals.pdf`
- Contains: Professional report from template
- Should be: 10-15 pages, well-formatted, includes charts

**Export to PDF:**
- Use Word: File → Export as PDF
- Or: Print to PDF from any document

---

## 🔧 Technical Details

**Python Packages Used:**
```
pandas              # Data manipulation
numpy               # Numerical computing
scikit-learn        # Machine learning
matplotlib          # Plotting
seaborn             # Statistical visualization
mlxtend             # Association Rule Mining
```

**Train-Test Split:** 80% training / 20% testing
**Random State:** 42 (for reproducibility)
**Features After Encoding:** [X] columns
**Models:** Decision Tree + Random Forest

---

## ❓ Troubleshooting

**Problem:** Missing library error
```bash
pip install scikit-learn mlxtend pandas matplotlib seaborn
```

**Problem:** heart.csv not found
- Make sure `heart.csv` is in the same folder as the notebook
- Or update the path in the notebook

**Problem:** Plots not showing in Jupyter
- Add this to the first code cell:
```python
%matplotlib inline
```

---

## 📞 Questions to Ask Yourself

As you write the report, make sure you can answer:

1. ✓ What are the key risk factors for heart disease in this dataset?
2. ✓ What symptom combinations are most predictive?
3. ✓ How accurate are the models? (accuracy, precision, recall, F1)
4. ✓ Which model is better and why?
5. ✓ How many patients with disease does each model miss? (false negatives)
6. ✓ Why is recall more important than accuracy for medical diagnosis?
7. ✓ What would I recommend to a hospital executive?

---

## 📚 Resources

- **Scikit-learn Documentation**: https://scikit-learn.org/
- **Confusion Matrix Guide**: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
- **Association Rules**: https://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/

---

## ✨ Final Tips

1. **Run the entire notebook before writing** - See all results first
2. **Screenshots all visualizations** - Export for your report
3. **Focus on Recall** - This is the grading rubric's emphasis
4. **Use real numbers** - Replace [X] in template with actual values
5. **Clinical language** - Frame findings as healthcare benefits
6. **Recommendation clear** - State exactly which model and why

---

**Good luck with your project!** 🍀

Remember: You're essentially creating a tool to help hospitals save lives through early disease detection.
