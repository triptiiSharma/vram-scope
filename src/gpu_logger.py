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

    try:
        utilization = pynvml.nvmlDeviceGetUtilizationRates(device)
        gpu_utilisation = utilization.gpu
        memory_utilisation = utilization.memory
    except:
        gpu_utilisation = 0
        memory_utilisation = 0

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

duration_input = input("How long to monitor? (seconds): ")
duration = int(duration_input)

interval_input = input("Sampling interval? (seconds): ")
interval = float(interval_input)

num_samples = int(duration / interval)

print(f"\nMonitoring for {duration} seconds, sampling every {interval} second(s)...")
print(f"Will collect {num_samples} measurements\n")

measurements = []

for i in range(num_samples):
    data = collect_gpu_data()
    measurements.append(data)

    if i < num_samples - 1:
        time.sleep(interval)
    print(f"Collected measurement {i+1}/{num_samples}")


print("\nAll measurements:")
for measurement in measurements:
    print(measurement)

timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
filename = f"data/gpu_logs_{timestamp}.csv"

fieldnames = list(measurements[0].keys())

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    writer.writerows(measurements)

print(f"\nSaved {len(measurements)} measurements to {filename}")