# 🚢 Titanic Survival Analysis

## Project Overview

This project analyzes the Titanic passenger dataset to identify the factors that influenced passenger survival. Using Python, Pandas, Matplotlib, and Seaborn, the dataset was cleaned, transformed, and explored to uncover meaningful patterns and insights.

The project follows a complete Data Analytics workflow including data understanding, data cleaning, feature engineering, exploratory data analysis (EDA), visualization, and insight generation.

---

## Business Problem

The objective of this analysis is to determine which factors had the greatest impact on passenger survival during the Titanic disaster.

Key questions explored:

* What was the overall survival rate?
* Did gender influence survival?
* Did passenger class affect survival?
* Did age affect survival chances?
* Did fare amount influence survival?
* Did family size impact survival outcomes?
* Did embarkation port affect survival rates?

---

## Dataset Information

**Dataset:** Titanic Dataset

**Source:** Kaggle Titanic Dataset

**Records:** 891 passengers

**Features:**

* PassengerId
* Survived
* Pclass
* Name
* Sex
* Age
* SibSp
* Parch
* Ticket
* Fare
* Cabin
* Embarked

### Target Variable

**Survived**

* 0 = Did Not Survive
* 1 = Survived

---

## Data Cleaning

Several preprocessing steps were performed to improve data quality:

### Missing Values

| Column   | Missing Values |
| -------- | -------------- |
| Age      | 177            |
| Cabin    | 687            |
| Embarked | 2              |

### Cleaning Steps

* Filled missing Age values using the median.
* Filled missing Embarked values using the mode.
* Removed Cabin column due to excessive missing values.
* Verified duplicate records.
* Created a cleaned dataset for analysis.

### Feature Engineering

Created new features:

#### FamilySize

FamilySize = SibSp + Parch + 1

This feature represents the total number of family members traveling together.

#### AgeGroup

Passengers were categorized into:

* Child
* Teen
* Young Adult
* Adult
* Senior

---

## Analysis

### Univariate Analysis

Analyzed individual variables:

* Survival Distribution
* Gender Distribution
* Passenger Class Distribution
* Age Distribution

### Bivariate Analysis

Analyzed relationships between variables:

* Gender vs Survival
* Passenger Class vs Survival
* Age Group vs Survival
* Embarked vs Survival

### Advanced Analysis

* Family Size vs Survival
* Fare vs Survival
* Correlation Analysis
* Heatmap Visualization

---

## Visualizations

The following visualizations were created:

### Univariate Analysis

* Survival Distribution
  <img width="631" height="435" alt="image" src="https://github.com/user-attachments/assets/f6db2ebb-bfa2-4989-821b-73bfcca8d521" />

* Gender Distribution
  <img width="623" height="432" alt="image" src="https://github.com/user-attachments/assets/47f66bcc-9480-43ec-a8c7-4ac5e159d853" />

* Passenger Class Distribution
  <img width="627" height="430" alt="image" src="https://github.com/user-attachments/assets/65668a59-5c37-4228-a449-917cc3522f4e" />

* Age Distribution
  <img width="618" height="391" alt="image" src="https://github.com/user-attachments/assets/9f6fca67-3ae1-4f40-8fe8-9c9afff2cfec" />

### Bivariate Analysis

* Gender vs Survival
  <img width="617" height="422" alt="image" src="https://github.com/user-attachments/assets/15283992-954b-4926-9547-ce0f4e873ce8" />

* Passenger Class vs Survival
  <img width="625" height="423" alt="image" src="https://github.com/user-attachments/assets/7e9b1d70-f405-46df-82e4-07daab92179b" />

* Age Group vs Survival
  <img width="622" height="388" alt="image" src="https://github.com/user-attachments/assets/dc4b680c-c599-4f4a-9e9c-a7c0eca84221" />

* Embarked vs Survival
  <img width="635" height="422" alt="image" src="https://github.com/user-attachments/assets/00c437cb-4b40-448d-a677-18d7cc582998" />

### Advanced Analysis

* Family Size vs Survival
  <img width="617" height="312" alt="image" src="https://github.com/user-attachments/assets/82b48206-b086-4da6-9c2d-d970554500e0" />

* Fare vs Survival
  <img width="610" height="387" alt="image" src="https://github.com/user-attachments/assets/5716c812-bf41-4e3c-8173-6845fd0c4208" />

* Correlation Heatmap
  <img width="562" height="467" alt="image" src="https://github.com/user-attachments/assets/06f1ba83-f3e5-4a0d-93f2-249b1e6a8ee9" />

---

## Key Insights

### 1. Survival Rate

More passengers died than survived during the Titanic disaster.

### 2. Gender Impact

Female passengers had significantly higher survival rates compared to male passengers.

### 3. Passenger Class Impact

First-class passengers experienced the highest survival rates, while third-class passengers had the lowest.

### 4. Age Impact

Children and younger passengers generally had better survival chances than older passengers.

### 5. Fare Impact

Passengers who paid higher ticket fares were more likely to survive.

### 6. Family Size Impact

Passengers traveling alone or with small families had better survival outcomes than those traveling in very large family groups.

### 7. Embarkation Port

Survival rates varied among embarkation ports, indicating differences in passenger demographics and travel classes.

### 8. Correlation Findings

* Fare showed a positive relationship with survival.
* Passenger class showed a strong relationship with survival.
* Age had a relatively weak correlation with survival.
* Family size showed a moderate influence on survival outcomes.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## Project Structure

Titanic-Survival-Analysis/

├── Titanic-Dataset.csv

├── Titanic_Cleaned.csv

├── analyze.py

├── README.md

└── visuals/

    ├── survival_distribution.png

    ├── gender_distribution.png

    ├── class_distribution.png

    ├── age_distribution.png

    ├── gender_vs_survival.png

    ├── class_vs_survival.png

    ├── agegroup_vs_survival.png

    ├── embarked_vs_survival.png

    ├── familysize_vs_survival.png

    ├── fare_vs_survival.png

    └── correlation_heatmap.png

---

## Conclusion

This analysis demonstrates how data analytics techniques can be used to uncover meaningful insights from historical datasets. The results indicate that passenger class, gender, fare amount, and family size played important roles in determining survival outcomes during the Titanic disaster.

The project showcases practical skills in data cleaning, feature engineering, exploratory data analysis, data visualization, and insight generation using Python.
