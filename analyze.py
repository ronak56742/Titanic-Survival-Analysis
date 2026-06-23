import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# LOAD DATA

df = pd.read_csv("Titanic-Dataset.csv")

# DATA UNDERSTANDING

print("Dataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# DATA CLEANING

df['Age'] = df['Age'].fillna(df['Age'].median())

df['Embarked'] = df['Embarked'].fillna(
    df['Embarked'].mode()[0]
)

df = df.drop('Cabin', axis=1)

# FEATURE ENGINEERING

df['FamilySize'] = (
    df['SibSp']
    + df['Parch']
    + 1
)

df['AgeGroup'] = pd.cut(
    df['Age'],
    bins=[0, 12, 18, 35, 60, 100],
    labels=[
        'Child',
        'Teen',
        'Young Adult',
        'Adult',
        'Senior'
    ]
)

# Save cleaned dataset
df.to_csv(
    "Titanic_Cleaned.csv",
    index=False
)

# Create visuals folder
os.makedirs("visuals", exist_ok=True)


# UNIVARIATE ANALYSIS

# Survival Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Survived', data=df)
plt.title("Survival Distribution")
plt.savefig("visuals/survival_distribution.png")
plt.show()

# Gender Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Sex', data=df)
plt.title("Gender Distribution")
plt.savefig("visuals/gender_distribution.png")
plt.show()

# Passenger Class Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Pclass', data=df)
plt.title("Passenger Class Distribution")
plt.savefig("visuals/class_distribution.png")
plt.show()

# Age Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=20, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.savefig("visuals/age_distribution.png")
plt.show()

# BIVARIATE ANALYSIS

# Gender vs Survival
plt.figure(figsize=(6,4))
sns.countplot(
    x='Sex',
    hue='Survived',
    data=df
)
plt.title("Gender vs Survival")
plt.savefig("visuals/gender_vs_survival.png")
plt.show()

# Class vs Survival
plt.figure(figsize=(6,4))
sns.countplot(
    x='Pclass',
    hue='Survived',
    data=df
)
plt.title("Passenger Class vs Survival")
plt.savefig("visuals/class_vs_survival.png")
plt.show()

# Age Group vs Survival
plt.figure(figsize=(8,5))
sns.countplot(
    x='AgeGroup',
    hue='Survived',
    data=df
)
plt.title("Age Group vs Survival")
plt.savefig("visuals/agegroup_vs_survival.png")
plt.show()

# Embarked vs Survival
plt.figure(figsize=(6,4))
sns.countplot(
    x='Embarked',
    hue='Survived',
    data=df
)
plt.title("Embarked vs Survival")
plt.savefig("visuals/embarked_vs_survival.png")
plt.show()

# ADVANCED ANALYSIS

# Family Size vs Survival
plt.figure(figsize=(10,5))
sns.countplot(
    x='FamilySize',
    hue='Survived',
    data=df
)
plt.title("Family Size vs Survival")
plt.savefig("visuals/familysize_vs_survival.png")
plt.show()

# Fare vs Survival
plt.figure(figsize=(8,5))
sns.boxplot(
    x='Survived',
    y='Fare',
    data=df
)
plt.title("Fare vs Survival")
plt.savefig("visuals/fare_vs_survival.png")
plt.show()

# Correlation Matrix
corr = df[
    [
        'Survived',
        'Pclass',
        'Age',
        'Fare',
        'SibSp',
        'Parch',
        'FamilySize'
    ]
].corr()

# Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm'
)
plt.title("Correlation Heatmap")
plt.savefig("visuals/correlation_heatmap.png")
plt.show()

print("\nProject Analysis Completed Successfully!")