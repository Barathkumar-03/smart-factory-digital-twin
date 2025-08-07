# 🏭 AI-Based Smart Factory Digital Twin with Realtime Fault Prediction & Visualization

## 📌 Overview
This project simulates a **Smart Factory Digital Twin** using Python, with real-time sensor data, AI-based fault prediction, and an interactive dashboard. It is a **100% software simulation** with no hardware required — perfect for demonstrating **Industry 4.0** and **IoT + AI integration** skills.

The system:
- Simulates data for **3 virtual machines** (temperature, vibration, RPM, pressure)
- Uses a **Random Forest Classifier** for real-time fault prediction
- Displays live machine status on a **Streamlit dashboard**
- Shows trends with real-time updating charts
- Can optionally log faults to cloud databases like Firebase

---

## 🎯 Features
- 🔄 Real-time sensor data simulation  
- 🧠 AI-powered fault detection  
- 📊 Live updating dashboard with charts and status  
- 💾 Save and load trained models  
- ☁️ Cloud logging support (optional Firebase integration)

---

## 🛠 Tech Stack
- **Python**
- **Pandas** – Data processing
- **Scikit-learn** – Machine Learning
- **Joblib** – Model persistence
- **Streamlit** – Dashboard & visualization
- **Matplotlib / Plotly** – Charts & graphs
- *(Optional)* **Firebase** – Cloud storage for alerts

---

## 📂 Project Structure
```text
smart-factory-digital-twin/
├── data/                          # Generated dataset for training
│   └── fault_dataset.csv
├── model/                         # Trained ML model
│   └── fault_predictor.pkl
├── images/                        # Project screenshots
│   └── dashboard_screenshot.png
├── sensor_simulator.py            # Live data simulation
├── data_generator.py              # Dataset creation
├── train_model.py                 # Model training
├── live_predictor.py              # Live fault prediction
├── dashboard_app.py               # Streamlit dashboard
└── Smart_Factory_Digital_Twin_Project_Report.pdf
