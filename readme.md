# 🏠 Task 01: House Price Prediction using Linear Regression

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-FF8C00?style=for-the-badge)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4%2B-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-28A745?style=for-the-badge)

</div>

<div align="center">

# 📈 Predicting House Prices with Linear Regression

</div>

A machine learning project that predicts residential house prices using a multiple linear regression model based on features such as square footage, number of bedrooms, and total bathrooms.

> Before execution, install the required dependencies locally. This repository does not include the virtual environment folder, so create and activate your own environment before running the project.

---

## 📌 Overview

This project implements a machine learning solution for estimating property values from structured housing data. It is designed to learn patterns from historical sales data and predict the sale price of a house based on essential property attributes.

The workflow includes:
- loading the dataset
- selecting relevant features
- engineering a combined bathroom metric
- training a linear regression model
- evaluating the model with metrics such as R² and RMSE
- generating submission-ready predictions
- visualizing actual versus predicted prices

This project was developed as Task 01 of the SkillCraft Technology Machine Learning Internship.

---

## 🛠️ Technologies Used

- Python 3
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- CSV dataset processing
- Jupyter / Python script execution

---

## 📂 Project Structure

```text
SCT_ML_1/
├── .gitignore                
├── .venv/                      # Local virtual environment(created from steps below)
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── linear_regression.py        # Main ML script
├── actual_vs_predicted.png     # created as ouput
├── submission_task1.csv        
├── data/
   ├── train.csv              
   ├── test.csv               
   ├── sample_submission.csv  
   └── data_description.txt   

```

## 💻 How to Run

### Prerequisites
- Python 3.10 or later
- pip package manager

### Step 1: Create a virtual environment

```bash
python -m venv .venv
```

### Step 2: Activate the environment

Windows (PowerShell):
```powershell
.\.venv\Scripts\Activate.ps1
```

Windows (Command Prompt):
```cmd
.venv\Scripts\activate.bat
```


### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the project

```bash
python linear_regression.py
```

### Step 5: View outputs
The script generates:
- `submission_task1.csv`
- `actual_vs_predicted.png`



---

---

## 🎯 Learning Outcomes

- Understand the workflow of a regression-based machine learning project
- Learn how to clean and prepare structured housing data
- Apply feature engineering for more meaningful prediction inputs
- Train and evaluate a Linear Regression model
- Interpret evaluation metrics like R² Score and RMSE
- Save predictions in a Kaggle-style CSV format
- Visualize the relationship between actual and predicted prices

---

## 📸 Project Preview

This project focuses on predicting household prices using features like:
- Living area in square feet
- Number of bedrooms
- Number of bathrooms
- Sale price as the target variable

A sample visualization, `actual_vs_predicted.png`, shows how closely the model's predictions match the actual prices.

---


## 👨‍💻 Author

**Author:** Devarakonda Vignesh Varsha  
**Project Type:** Machine Learning Internship Task

---

## 📌 Internship Details

- **Internship:** SkillCraft Technology
- **Domain:** Machine Learning
- **Task:** Task 01 - House Price Prediction
- **Objective:** Build a Linear Regression model to predict house prices using relevant property features

---

<div align="center">

⭐ This project demonstrates a practical machine learning workflow for tabular data and highlights the value of regression models in real-world price prediction tasks.

</div>
