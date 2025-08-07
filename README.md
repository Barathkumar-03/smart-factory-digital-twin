# 🏭 AI-Based Smart Factory Digital Twin with Realtime Fault Prediction & Visualization

## 📌 Overview
This project simulates a **Smart Factory Digital Twin** using Python, with real-time sensor data, AI-based fault prediction, and an interactive dashboard.  
It is a **100% software simulation** with no hardware required — perfect for demonstrating **Industry 4.0** and **IoT + AI integration** skills.

The system:
- Simulates data for **3 virtual machines** (temperature, vibration, RPM, pressure)
- Uses a **Random Forest Classifier** for real-time fault prediction
- Displays live machine status on a **Streamlit dashboard**
- Shows trends with real-time updating charts


---

## 🎯 Features
- 🔄 **Real-time sensor data simulation**
- 🧠 **AI-powered fault detection**
- 📊 **Live updating dashboard** with charts and machine status
- 💾 **Save & load trained models** for reuse

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
├── live_predictor.py               # Live fault prediction
├── dashboard_app.py                # Streamlit dashboard
├── Smart_Factory_Digital_Twin_Project_Report.pdf # Project report
└── README.md                       # Documentation

---

## 🚀 How to Run the Project

1️⃣ Install Dependencies\
pip install -r requirements.txt

2️⃣ Generate Dataset
python data_generator.py

3️⃣ Train the Model
python train_model.py

4️⃣ Run Live Predictions in Terminal
python live_predictor.py

5️⃣ Launch the Dashboard
streamlit run dashboard_app.py

---

## 📸 Dashboard Preview
Here’s the live monitoring dashboard showing real-time machine status:

![Dashboard Preview](images/dashboard_screenshot.png)

---

## 📝 Project Highlights
No Hardware Required – Fully software-based simulation

Machine Learning Model – Predicts faults with high accuracy

Live Data Streaming – Simulates sensor readings in real-time

Interactive Dashboard – Visualizes machine status & performance metrics

Customizable Thresholds – Easily adjust parameters for different factory setups

