import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Step 1: Generate synthetic data
np.random.seed(42)
n_samples = 300

data = {
    'speed': np.random.uniform(20, 100, n_samples),
    'terrain_type': np.random.choice([0, 1, 2], n_samples),  # 0=flat, 1=uphill, 2=downhill
    'braking_events': np.random.randint(0, 10, n_samples),
    'acceleration': np.random.uniform(0.5, 4.0, n_samples),
    'ambient_temp': np.random.uniform(10, 45, n_samples)
}

df = pd.DataFrame(data)

# Step 2: Simulate battery usage (target)
df['battery_usage'] = (
    0.015 * df['speed'] +
    0.3 * df['terrain_type'] +
    0.2 * df['braking_events'] +
    0.5 * df['acceleration'] -
    0.01 * df['ambient_temp'] +
    np.random.normal(0, 0.2, n_samples)  # noise
)

# Step 3: Train a linear regression model
X = df[['speed', 'terrain_type', 'braking_events', 'acceleration', 'ambient_temp']]
y = df['battery_usage']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Save the model
joblib.dump(model, "battery_model.pkl")
print("✅ Model trained and saved as 'battery_model.pkl'")
