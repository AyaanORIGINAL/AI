import random
import statistics

readings = []
print("LIDAR Sensor Scanning")

for i in range(10):
    readings.append(100 + random.randint(-2, 2))

readings.append(500)
print(f"raw data with glitch: {readings}")
avg_distance = sum(readings) / len(readings)

median_distance = statistics.median(readings)

print("-" * 20)
print(f"Average distance: {avg_distance}cm INACCURATE")
print(f"Median distance: {median_distance}cm ACCURATE")