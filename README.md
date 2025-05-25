
# 🚀 Startup Profit Prediction using Multiple Regression Models

This project aims to predict the **profit** of startup companies using various regression models based on features like R&D Spend, Administration, Marketing Spend, and Location (State). We evaluate multiple regression techniques and select the best-performing model based on accuracy and performance metrics.

---

## 🧠 Problem Statement

Startup profitability is influenced by various types of spending and strategic decisions. Using machine learning, we aim to model these factors to predict profit outcomes. The goal is to identify which regression model performs best for this task.

---

## 🗂 Project Structure

```startup-profit-prediction/
├── code/                               # Jupyter Notebook & HTML version
│ ├── project_code.ipynb
│ └── code.html
├── data/                              # Dataset
│ └── 50_Startups.csv
├── notebooks/                          # Experimental notebooks (optional)
│ └── README.md
├── scripts/                            # Python scripts for modular code
│ ├── preprocessing.py
│ └── model.py
├── docs/                               # Project overview & documentation
│ └── overview.md
├── PROJCT_report.pdf                    # Project report (PDF)
├── README.md                             # You're reading this file 📘
├── requirements.txt                       # Python dependencies
├── .gitignore                              # Ignored files
├── LICENSE                                # Open source license
└── CONTRIBUTING.md                         # Contribution guide
```

---

## 📊 Dataset Overview

- **Name**: 50_Startups.csv  
- **Features**:
  - R&D Spend
  - Administration
  - Marketing Spend
  - State (categorical)
- **Target**: Profit

---

## 🧪 Models Used and Evaluated

We implemented and compared the following regression models:

- 🔵 **Gradient Boosting Regression**
- 🟢 **Polynomial Regression**
- 🔴 **Linear Regressionn**
- 🟠 **Support Vector Regression**
- ⚫ **Decision Tree Regression**
- 🟣 **Random Forest Regression**

Each model was trained, tested, and evaluated using R² score and RMSE metrics.

---

## 🏆 Final Model Selection

After evaluating all models, we selected the **[Insert Best Model Here, e.g., Linear Regression]** as the final model based on:

- Highest R² Score on Test Data
- Lowest Root Mean Squared Error
- Robustness to overfitting

---

## 🛠️ Technologies Used

- Python 3.x
- Jupyter Notebook
- Pandas, NumPy
- Matplotlib, Seaborn
- scikit-learn
- statsmodels

---

## ⚙️ How to Run the Project

1. Clone the repository:

  git clone https://github.com/your-username/startup-profit-prediction.git
  cd startup-profit-prediction

2. Install the required packages

  pip install -r requirements.txt

3. Launch the notebook:

  jupyter notebook code/project_code.ipynb

## 📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

## 🤝 Contributing
We welcome contributions! Please check the CONTRIBUTING.md for guidelines.

## 🙏 Acknowledgements
Dataset: 50_Startups

Tools: Python, Jupyter, Scikit-learn, Statsmodels

Developed as part of a Data Science Lab Project


