import random
import time
import pandas as pd
import joblib

# Load the trained ML model
model = joblib.load("model/fault_predictor.pkl")
print("✅ Fault prediction model loaded!")

# List of machines
MACHINES = ["Machine-1", "Machine-2", "Machine-3"]

def generate_sensor_data(machine_id):
    return {
        "machine_id": machine_id,
        "temperature": round(random.uniform(45, 100), 2),
        "vibration": round(random.uniform(0.1, 2.0), 2),
        "rpm": random.randint(800, 1600),
        "pressure": round(random.uniform(2.0, 6.0), 2),
        "timestamp": pd.Timestamp.now()
    }

def predict_fault(sensor):
    features = [[
        sensor["temperature"],
        sensor["vibration"],
        sensor["rpm"],
        sensor["pressure"]
    ]]
    prediction = model.predict(features)[0]
    return prediction

def simulate_prediction(interval=2):
    print("\n📡 Real-time Fault Prediction Running...\n")
    while True:
        for machine in MACHINES:
            sensor_data = generate_sensor_data(machine)
            fault = predict_fault(sensor_data)

            status = "⚠️ FAULT DETECTED" if fault == 1 else "✅ Normal"
            print(f"[{sensor_data['timestamp']}] {sensor_data['machine_id']} → Temp: {sensor_data['temperature']}°C, Vib: {sensor_data['vibration']}g, RPM: {sensor_data['rpm']}, Pressure: {sensor_data['pressure']} bar → Status: {status}")
        print("-" * 120)
