rules = {
    ("emergency", 1, "All activities must stop immediately."),
    ("exam", 2, "Outdoor activities are restricted during exams."),
    ("rain", 3, "Outdoor activities are discouraged during heavy rain."),
    ("holiday", 4, "Outdoor activities are encouraged on holidays."),
    ("weekend", 5, "Outdoor activities are encouraged on weekends."),
    ("good_weather", 6, "Outdoor activities are encouraged in good weather."),
}

state = {
     "emergency": False,
     "exam": True,
    "rain": False,
    "holiday": True,
    "weekend": True,
    "good_weather": True,
}
active_rules = []

for rule, priority, message in rules:
    if state[rule]:
        active_rules.append((priority, message))
if active_rules:
    active_rules.sort()
    print("Decision: " + active_rules[-1][1])
else:
    print("Decision: No specific rules active, proceed as normal.")