
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (make sure train.csv is in the same folder)
df = pd.read_csv("train.csv")

# --------------------
# DATA CLEANING
# --------------------

# Check missing values
print(df.isnull().sum())

# Fill missing Age with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill missing Embarked with most frequent value
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])


df.drop(columns=['Cabin'], inplace=True)



# 1. Survival by Gender
df.groupby('Sex')['Survived'].mean().plot(kind='bar')
plt.title("Survival Rate by Gender")
plt.ylabel("Survival Rate")
plt.show()

# 2. Survival by Passenger Class
df.groupby('Pclass')['Survived'].mean().plot(kind='bar')
plt.title("Survival Rate by Passenger Class")
plt.ylabel("Survival Rate")
plt.show()

# 3. Age Distribution
plt.hist(df['Age'], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# 4. Fare vs Survival
df.boxplot(column='Fare', by='Survived')
plt.title("Fare vs Survival")
plt.suptitle("")
plt.show()

# 5. Correlation between numeric variables
print(df.corr(numeric_only=True))
