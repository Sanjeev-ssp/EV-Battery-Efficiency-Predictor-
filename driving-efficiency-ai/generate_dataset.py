import pandas as pd
import numpy as np

np.random.seed(42)

n = 200

speed = np.random.uniform(20, 120, n)
terrain_type = np.random.randint(0, 3, n)
braking_events = np.random.poisson(4, n)
acceleration = np.random.normal(2.5, 1, n)
ambient_temp = np.random.normal(30, 5, n)

battery_usage = (
    0.002 * speed
    + 0.1 * terrain_type
    + 0.05 * braking_events
    + 0.2 * acceleration
    - 0.003 * ambient_temp
    + np.random.normal(0, 0.05, n)
)

df = pd.DataFrame({
    'speed': speed,
    'terrain_type': terrain_type,
    'braking_events': braking_events,
    'acceleration': acceleration,
    'ambient_temp': ambient_temp,
    'battery_usage': battery_usage
})

df.to_csv("driving_data.csv", index=False)
print("✅ Dataset generated and saved as 'driving_data.csv'")
