import csv
import pandas as pd

file1 = input("Enter first CSV filename: ")
file2 = input("Enter second CSV filename: ")

read_file1 = pd.read_csv(file1)
read_file2 = pd.read_csv(file2)

avg1 = read_file1["Used Memory"].mean()
avg2 = read_file2["Used Memory"].mean()
difference = avg2 - avg1

print(f"Average used memory of file 1: {avg1:.3f} GB")
print(f"Average used memory of file 2: {avg2:.3f} GB")
print(f"Difference: {difference:.3f} GB")

util1 = read_file1["GPU Utilisation"].mean()
util2 = read_file2["GPU Utilisation"].mean()
util_diff = util2 - util1

print(f"\nAverage GPU utilization of file 1: {util1:.1f}%")
print(f"Average GPU utilization of file 2: {util2:.1f}%")
print(f"Difference: {util_diff:.1f}%")

temp1 = read_file1["Temperature"].mean()
temp2 = read_file2["Temperature"].mean()
temp_diff = temp2 - temp1

print(f"\nAverage temperature of file 1: {temp1:.1f}°C")
print(f"Average temperature of file 2: {temp2:.1f}°C")
print(f"Difference: {temp_diff:.1f}°C")

