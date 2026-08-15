import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load Dataset
df = pd.read_csv("gym_membership.csv")

print("Dataset Loaded Successfully!")
print(df.head())

# Encode categorical columns
encoder = LabelEncoder()

categorical_columns = [
    "Gender",
    "Goal",
    "Experience",
    "Trainer",
    "Swimming",
    "Membership"
]

for column in categorical_columns:
    df[column] = encoder.fit_transform(df[column])

# Features
X = df.drop("Membership", axis=1)

# Target
y = df["Membership"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy : {accuracy*100:.2f}%")

# Save Model
joblib.dump(model, "model.pkl")

print("\nModel Saved Successfully!")