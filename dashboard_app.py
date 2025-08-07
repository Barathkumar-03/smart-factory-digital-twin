import streamlit as st
import pandas as pd
import random
import joblib
import time
from collections import deque

# Load the model
model = joblib.load("model/fault_predictor.pkl")

MACHINES = ["Machine-1", "Machine-2", "Machine-3"]

# Store last 20 sensor readings for graphs
sensor_history = {
    m: {
        "temperature": deque(maxlen=20),
        "vibration": deque(maxlen=20),
        "fault": deque(maxlen=20)
    }
    for m in MACHINES
}

def generate_sensor_data():
    return {
        "temperature": round(random.uniform(45, 100), 2),
        "vibration": round(random.uniform(0.1, 2.0), 2),
        "rpm": random.randint(800, 1600),
        "pressure": round(random.uniform(2.0, 6.0), 2)
    }

def predict_fault(data):
    features = [[data["temperature"], data["vibration"], data["rpm"], data["pressure"]]]
    return model.predict(features)[0]

# Streamlit layout
st.set_page_config(page_title="Smart Factory Digital Twin", layout="wide")
st.title("🏭 Smart Factory Digital Twin – Fault Monitoring System")

main_area = st.empty()

# Columns for charts
cols = st.columns(len(MACHINES))

while True:
    rows = []

    for i, machine in enumerate(MACHINES):
        data = generate_sensor_data()
        prediction = predict_fault(data)
        status = "⚠️ FAULT" if prediction == 1 else "✅ Normal"

        # Add current values to history for graphs
        sensor_history[machine]["temperature"].append(data["temperature"])
        sensor_history[machine]["vibration"].append(data["vibration"])
        sensor_history[machine]["fault"].append(prediction)

        # Table row
        rows.append({
            "Machine": machine,
            "Temperature (°C)": data["temperature"],
            "Vibration (g)": data["vibration"],
            "RPM": data["rpm"],
            "Pressure (bar)": data["pressure"],
            "Status": status
        })

        # Graphs
        with cols[i]:
            st.subheader(f"📊 {machine}")
            st.line_chart(pd.DataFrame({
                "Temperature": list(sensor_history[machine]["temperature"]),
                "Vibration": list(sensor_history[machine]["vibration"])
            }))
            st.write("Last Status:", status)

    # Live table of all machines
    df = pd.DataFrame(rows)
    main_area.table(df)

    time.sleep(3)
