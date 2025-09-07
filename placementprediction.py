import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Load dataset with correct path
df = pd.read_csv(r"C:\Users\princ\OneDrive\Desktop\ML\PYTHON PROGRAMS\placement.csv")


print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())


# Features and Target
X = df[['cgpa', 'iq']]
y = df['placement']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# Example prediction
sample = model.predict([[7.0, 120]])  # CGPA=7.0, IQ=120
print("Prediction (1=Placed, 0=Not Placed):", sample[0])
