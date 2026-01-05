failures = 0

for day in range(1, 8):
    print(f"Day {day}:")

    weather = input("Weather (sunny/rainy): ").strip().lower()
    exam = input("Exam today? (yes/no): ").strip().lower()
    
    if exam == "yes":
        decision = "Cancel activities due to exam."
    elif weather == "sunny" and failures < 2:
        decision = "Outdoor activities"
    else:
        decision = "Indoor activities"
    print(f"Decision: {decision}")

    result = input("Was the decision good? (yes/no): ").strip().lower()
    if result == "no":
        failures += 1
        print("Noted failure.\n")
    
print(f"Total failures over the week: {failures}")