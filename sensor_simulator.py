import random
import time
import pandas as pd

# List of virtual machines
MACHINES = ["Machine-1", "Machine-2", "Machine-3"]

def generate_sensor_data(machine_id):
    return {
        "machine_id": machine_id,
        "temperature": round(random.uniform(45, 95), 2),  # degrees Celsius
        "vibration": round(random.uniform(0.1, 1.5), 2),  # g-force
        "rpm": random.randint(900, 1500),                 # rotations per minute
        "pressure": round(random.uniform(2.0, 5.5), 2),   # bar
        "timestamp": pd.Timestamp.now()
    }

def simulate_stream(interval=2):
    print("📡 Simulating live factory sensor data...\n")
    while True:
        for machine in MACHINES:
            data = generate_sensor_data(machine)
            print(data)
        print("-" * 50)
        time.sleep(interval)

if __name__ == "__main__":
    simulate_stream()
