import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib  # For saving the model

# Step 1: Load dataset
df = pd.read_csv("data/fault_dataset.csv")
print("✅ Dataset loaded. Sample:")
print(df.head())

# Step 2: Define features and label
X = df[["temperature", "vibration", "rpm", "pressure"]]
y = df["fault"]

# Step 3: Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Test the model
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("\n📈 Accuracy of the model:", round(acc * 100, 2), "%")
print("\n📋 Classification Report:\n", classification_report(y_test, y_pred))

# Step 6: Save the trained model
joblib.dump(model, "model/fault_predictor.pkl")
print("💾 Model saved to model/fault_predictor.pkl")
