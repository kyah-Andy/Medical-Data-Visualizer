

# 🏥 Medical Data Visualizer

This project visualizes medical examination data using **Python**, **Pandas**, **Matplotlib**, and **Seaborn**. It explores the relationship between lifestyle factors, body measurements, blood markers, and the presence of cardiovascular disease.

![Data Cleaning](https://img.shields.io/badge/Data%20Cleaning-Yes-blue)
![EDA](https://img.shields.io/badge/EDA-Exploratory%20Analysis-green)
![Visualization](https://img.shields.io/badge/Visualization-Seaborn%20%2F%20Matplotlib-orange)
---
## Preview

![Result Preview](https://github.com/kyah-Andy/Medical-Data-Visualizer/blob/main/catplot.png)

![Result Preview](https://github.com/kyah-Andy/Medical-Data-Visualizer/blob/main/heatmap.png)

---

## 📊 Dataset

The dataset (`medical_examination.csv`) contains patient records with the following features:

- Age (in days)
- Height (cm)
- Weight (kg)
- Gender
- Blood pressure (ap_hi, ap_lo)
- Cholesterol level
- Glucose level
- Lifestyle factors (smoke, alco, active)
- Target variable: cardio (presence of cardiovascular disease)

---

## 🎯 Project Goals

The goal of this project is to:

1. Analyze medical data using pandas
2. Engineer new features (e.g., BMI / overweight status)
3. Normalize categorical health indicators
4. Visualize relationships using:
   - 📌 Categorical Plot (Seaborn Catplot)
   - 📌 Correlation Heatmap (Seaborn Heatmap)

---

## 🧠 Features Implemented

### 1. Data Cleaning & Feature Engineering
- Added **overweight column** using BMI calculation
- Normalized cholesterol and glucose values:
  - `1 → 0 (good)`
  - `>1 → 1 (bad)`

---

### 2. Categorical Plot
- Uses `sns.catplot()`
- Shows counts of:
  - cholesterol
  - glucose
  - smoke
  - alco
  - active
  - overweight
- Split by cardiovascular disease (`cardio`)

---

### 3. Heatmap Visualization
- Data cleaning includes:
  - Removing invalid blood pressure values
  - Removing extreme height/weight outliers
- Correlation matrix generated using Pandas
- Heatmap created using Seaborn

---

## 📁 Project Structure
Medical_Data_Visualizer/
│── main.py  
│── medical_data_visualizer.py  
│── medical_examination.csv  
│── test_module.py  
│── README.md  



---

## ⚙️ Installation

Install required libraries:

```bash
pip install pandas matplotlib seaborn
```
## 🚀 How to Run

Run the project using:
```
python main.py
```

This will:
- Run unit tests
- Generate visualizations (catplot + heatmap)

---

## 🧪 Testing

Tests are included in test_module.py.

Run automatically via:
```
python main.py
```
If everything is correct, you should see:
```
Ran 2 tests in X.XXXs
OK
```
---
## 📈 Expected Outputs

When running successfully, you should see:
```
Ran 2 tests in X.XXXs
OK
```
---


**Categorical Plot**
- Count plots for health/lifestyle features
- Split by cardiovascular disease
**Heatmap**
- Correlation matrix of medical features
- Clear positive/negative relationships between variables

## 📌 Notes
- Ensure medical_examination.csv is in the same directory as main.py
- Do not modify test files for validation

## 👨‍💻 Author
**Andy Razon**

📜 License
This project is part of the freeCodeCamp curriculum and is intended for educational purposes.
