import pynvml

print("=" * 50)
print("VRAM-SCOPE - GPU Information")
print("=" * 50)

try:
    # Initialize NVIDIA Management Library
    pynvml.nvmlInit()
    print("\nSuccessfully connected to GPU!")
    
    # Get GPU device (0 = first GPU)
    device = pynvml.nvmlDeviceGetHandleByIndex(0)
    
    # Get GPU name
    gpu_name = pynvml.nvmlDeviceGetName(device)
    print(f"GPU Found: {gpu_name}\n")
    
    # Get memory information
    memory = pynvml.nvmlDeviceGetMemoryInfo(device)
    memory_total_gb = memory.total / (1024**3)
    memory_used_gb = memory.used / (1024**3)
    memory_free_gb = memory.free / (1024**3)
    
    print(f"Memory Information:")
    print(f"  Total: {memory_total_gb:.2f} GB")
    print(f"  Used:  {memory_used_gb:.2f} GB")
    print(f"  Free:  {memory_free_gb:.2f} GB")
    
    # Get GPU utilization
    utilization = pynvml.nvmlDeviceGetUtilizationRates(device)
    print(f"\nGPU Utilization: {utilization.gpu}%")
    print(f"Memory Utilization: {utilization.memory}%")
    
    # Get GPU temperature
    temperature = pynvml.nvmlDeviceGetTemperature(device, pynvml.NVML_TEMPERATURE_GPU)
    print(f"GPU Temperature: {temperature}°C")
    
    print("\n" + "=" * 50)
    print("SUCCESS!")
    print("=" * 50)
    
except Exception as e:
    print(f"Error: {e}")
