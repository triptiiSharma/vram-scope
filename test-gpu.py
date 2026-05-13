# Day 1: First GPU Access Test
# This script checks if we can read GPU information

import pynvml

print("=" * 50)
print("VRAM-SCOPE - Day 1 Setup Test")
print("=" * 50)

try:
    # Initialize NVIDIA Management Library
    pynvml.nvmlInit()
    print("\n✓ Successfully connected to GPU!")
    
    # Get GPU device (0 = first GPU)
    device = pynvml.nvmlDeviceGetHandleByIndex(0)
    
    # Get GPU name
    gpu_name = pynvml.nvmlDeviceGetName(device)
    print(f"\n✓ GPU Found: {gpu_name}")
    
    # Get memory information
    memory = pynvml.nvmlDeviceGetMemoryInfo(device)
    memory_total_gb = memory.total / (1024**3)
    memory_used_gb = memory.used / (1024**3)
    memory_free_gb = memory.free / (1024**3)
    
    print(f"\n✓ Memory Information:")
    print(f"  Total: {memory_total_gb:.2f} GB")
    print(f"  Used:  {memory_used_gb:.2f} GB")
    print(f"  Free:  {memory_free_gb:.2f} GB")
    
    # Get GPU utilization
    utilization = pynvml.nvmlDeviceGetUtilizationRates(device)
    print(f"\n✓ GPU Utilization: {utilization.gpu}%")
    print(f"✓ Memory Utilization: {utilization.memory}%")
    
    # Get GPU temperature
    temperature = pynvml.nvmlDeviceGetTemperature(device, pynvml.NVML_TEMPERATURE_GPU)
    print(f"\n✓ GPU Temperature: {temperature}°C")
    
    print("\n" + "=" * 50)
    print("SUCCESS! Everything is working perfectly!")
    print("=" * 50)
    print("\n💡 Next: We'll use these same functions to log data over time")
    
except Exception as e:
    print(f"\n✗ Error: {e}")
    print("\nTroubleshooting:")
    print("1. Make sure you have an NVIDIA GPU")
    print("2. Check NVIDIA drivers: run 'nvidia-smi' in cmd")
    print("3. Verify pynvml is installed: pip list | findstr pynvml")