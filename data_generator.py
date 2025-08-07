import random
import pandas as pd

# Define how many samples you want to generate
NUM_SAMPLES = 1000

def generate_sample(machine_id):
    temp = round(random.uniform(45, 100), 2)
    vib = round(random.uniform(0.1, 2.0), 2)
    rpm = random.randint(800, 1600)
    pres = round(random.uniform(1.5, 6.0), 2)
    
    # Rule-based fault: High temp AND high vibration = likely fault
    fault = 1 if (temp > 85 and vib > 1.2) else 0

    return {
        "machine_id": machine_id,
        "temperature": temp,
        "vibration": vib,
        "rpm": rpm,
        "pressure": pres,
        "fault": fault
    }

def generate_dataset():
    data = []
    for i in range(NUM_SAMPLES):
        machine = random.choice(["Machine-1", "Machine-2", "Machine-3"])
        data.append(generate_sample(machine))

    df = pd.DataFrame(data)
    df.to_csv("data/fault_dataset.csv", index=False)
    print("✅ Dataset generated and saved to data/fault_dataset.csv")

if __name__ == "__main__":
    generate_dataset()
