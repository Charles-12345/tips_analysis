# Tips Prediction Using Linear Regression

## Overview

This project demonstrates a simple machine learning workflow using Python to predict restaurant tip amounts based on customer and dining characteristics. A Linear Regression model is built using the **Tips** dataset from the Seaborn repository.

The project includes:

- Data loading and inspection
- Data preprocessing
- Linear Regression model training
- Model evaluation using RMSE and R²
- Feature importance analysis
- Visualization of feature influence

---

## Dataset

The dataset is loaded directly from the Seaborn GitHub repository:

https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv

### Dataset Variables

| Variable | Description |
|----------|-------------|
| total_bill | Total bill amount |
| tip | Tip amount (Target Variable) |
| sex | Customer gender |
| smoker | Smoker status |
| day | Day of the week |
| time | Lunch or Dinner |
| size | Number of people in the party |

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- PyCharm IDE

---

## Requirements

Install the required libraries using:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

Or install from the requirements file:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
tips-analysis/
│
├── analysis.py
├── README.md
├── Notes.md
├── requirements.txt
└── visualization.png
```

---

## How to Run

1. Clone or download this repository.
2. Open the project in PyCharm (or your preferred Python IDE).
3. Install the required libraries.
4. Run:

```bash
python analysis.py
```

The script will:

- Load the dataset
- Inspect the data
- Encode categorical variables
- Train a Linear Regression model
- Evaluate the model
- Display feature importance
- Save a visualization as `visualization.png`

---

## Machine Learning Workflow

The analysis follows these steps:

1. Load the dataset.
2. Inspect the data structure.
3. Check for missing values.
4. Encode categorical variables using one-hot encoding.
5. Split the dataset into training and testing sets (80% / 20%).
6. Train a Linear Regression model.
7. Predict tip values.
8. Evaluate the model using RMSE and R².
9. Visualize feature coefficients.

---

## Model Evaluation

The model performance is measured using:

- **RMSE (Root Mean Squared Error)** – Measures prediction error.
- **R² Score** – Measures how well the model explains the variation in tip amounts.

---

## Findings

The analysis indicates that **Total Bill** is the most influential variable in predicting the tip amount.

This is expected because customers typically leave tips based on a percentage of the total bill. Variables such as party size, smoker status, day of the week, and meal time contribute to the prediction but have comparatively smaller effects.

A bar chart (`visualization.png`) is generated to illustrate the relative influence of each feature.

---

## Files Included

- `analysis.py` – Main Python script
- `README.md` – Project documentation
- `Notes.md` – Summary of findings
- `requirements.txt` – Required Python packages
- `visualization.png` – Feature importance visualization

---

## Author

**Charles Daniel Apollo**

Data Management & Monitoring & Evaluation Professional  
Prospective Data Scientist

Email: **charlesdanieldoka@gmail.com**

---

## Acknowledgements

This project uses the publicly available **Tips** dataset provided by the Seaborn library.

Thank you for reviewing my submission. I appreciate the opportunity to complete this assessment and look forward to discussing my approach and findings.
