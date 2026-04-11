# 🧹 Customer Data Preprocessing

A beginner-friendly Python project that walks through the essential steps of cleaning, encoding, and scaling a raw customer dataset before feeding it into a machine learning model.

---

## 📌 Problem Statement

Raw datasets are messy — they contain missing values, duplicate records, inconsistent categories, and numerical features on vastly different scales. This project tackles all of those issues step by step.

---

## 📂 Dataset

A synthetic customer dataset with the following columns:

| Column | Type | Description |
|---|---|---|
| `customer_id` | Integer | Unique customer identifier |
| `age` | Float | Customer age (has missing values) |
| `city` | String | City of residence (has missing values) |
| `gender` | String | Male / Female |
| `annual_income` | Integer | Yearly income in INR |

---

## 🗂️ Project Structure

```
customer-preprocessing/
│
├── preprocessing.py       # Main script with all 3 tasks
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

---

## ✅ Tasks

### Task 1 — Clean the Data
- Impute missing values in `age` with the **median**
- Impute missing values in `city` with the **mode** (most frequent value)
- Remove **duplicate rows**

**Why?**
- Median is robust to outliers for numerical columns
- Mode makes sense for categorical columns
- Duplicate rows can bias the model during training

---

### Task 2 — Encode Categorical Columns
- **One-Hot Encoding** on `city` → creates binary columns like `city_Mumbai`, `city_Delhi`
- **Label Encoding** on `gender` → converts `Male/Female` to `1/0`

**Why?**
Machine learning models work with numbers, not text. Encoding converts categories into a numerical format the model can understand.

---

### Task 3 — Scale Numerical Features

Scale `age` and `annual_income` using:

| Scaler | Formula | Output Range | Best For |
|---|---|---|---|
| **MinMaxScaler** | `(x - min) / (max - min)` | 0 to 1 | KNN, Neural Networks |
| **StandardScaler** | `(x - mean) / std` | ~-3 to +3 | Linear models, SVM |

**When to prefer which?**
- Use **MinMaxScaler** when your data has no extreme outliers and the algorithm expects bounded inputs (e.g., neural networks).
- Use **StandardScaler** when your data has outliers or you're using distance-sensitive algorithms like SVM or Logistic Regression — it centers data around zero with unit variance.

---

## 🛠️ Libraries Used

| Library | Purpose |
|---|---|
| `pandas` | Data manipulation and cleaning |
| `numpy` | Numerical operations |
| `sklearn.preprocessing` | Encoding and scaling tools |

---

## ⚙️ Setup & Run

### 1. Install dependencies
```bash
pip install pandas numpy scikit-learn
```

### 2. Run the script
```bash
python preprocessing.py
```

---

## 📖 Key Concepts Explained

### 🔹 What is `sklearn`?
Scikit-Learn (`sklearn`) is a Python machine learning library that provides ready-made tools for preprocessing, model training, and evaluation. In this project, we use its `preprocessing` module.

### 🔹 Why scale data?
If `age` ranges from 25–40 and `annual_income` ranges from 40,000–1,20,000, algorithms that compute distances will heavily favour income and almost ignore age. Scaling brings both features to a comparable range.

### 🔹 Why use median (not mean) for imputation?
The mean is sensitive to outliers. If one customer has an age of 200 (bad data), the mean shifts drastically. The median stays stable.

---

## 👤 Author

Created as a learning exercise in data preprocessing fundamentals.
