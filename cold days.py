temps = [13,14,15,18,20,22,18,16,19]
cold_days = []

for temp in temps:
    if temp <=15:
        cold_days.append(temp)

normal_days = [temp for temp in temps if temp >15]
print("Cold Days:", cold_days)
print("Normal Days:", normal_days)
print("Number of Cold Days:", len(cold_days))