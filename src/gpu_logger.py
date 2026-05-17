import pynvml
import time
from datetime import datetime
import csv

pynvml.nvmlInit()

def collect_gpu_data():
    device = pynvml.nvmlDeviceGetHandleByIndex(0)

    name = pynvml.nvmlDeviceGetName(device)

    memory = pynvml.nvmlDeviceGetMemoryInfo(device)
    memory_total_gb = memory.total / (1024**3)
    memory_used_gb = memory.used / (1024**3)
    memory_free_gb = memory.free / (1024**3)

    utilization = pynvml.nvmlDeviceGetUtilizationRates(device)
    gpu_utilisation = utilization.gpu
    memory_utilisation = utilization.memory

    temperature = pynvml.nvmlDeviceGetTemperature(device, pynvml.NVML_TEMPERATURE_GPU)

    gpu_data = {
        "Timestamp": datetime.now(),
        "Device Name": name,
        "Total Memory": memory_total_gb,
        "Used Memory": memory_used_gb,
        "Free Memory": memory_free_gb,
        "GPU Utilisation": gpu_utilisation,
        "Memory Utilisation": memory_utilisation,
        "Temperature": temperature
    }

    return gpu_data

measurements = []

for i in range(5):
    data = collect_gpu_data()
    measurements.append(data)

    if i < 4:
        time.sleep(3)
    print(f"Collected measurement {i+1}/5")


print("\nAll measurements:")
for measurement in measurements:
    print(measurement)

filename = "data/gpu_logs.csv"

fieldnames = list(measurements[0].keys())

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    writer.writerows(measurements)

print(f"\nSaved {len(measurements)} measurements to {filename}")