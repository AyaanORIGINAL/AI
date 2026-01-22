def support_model(marks):
    if marks >= 60:
        return "No support needed"
    else:
        return "Support needed"
    
students = [
    {"id": 1, "marks": 85, "actual_support": "No"},
    {"id": 2, "marks": 65, "actual_support": "Yes"},
    {"id": 3, "marks": 45, "actual_support": "Yes"},
    {"id": 4, "marks": 70, "actual_support": "Yes"},
    {"id": 5, "marks": 55, "actual_support": "Yes"},
]

print("Safety check for support model")
safety_violations = False
failures = []
for student in students:
    prediction = support_model(student["marks"])

    if student["actual_support"] == "Yes" and prediction == "No support needed":
        safety_violations = True
        failures.append(student["id"])
        print(f"Safety violation for student ID {student['id']}: Actual support needed but predicted no support needed.")
    else: 
        print(f"Student ID {student['id']}: Prediction correct.")

print("\nSummary of safety check:")
if safety_violations:
    print(f"Safety violations found for student IDs: {failures}")
    print(f"Model failed to identify support needs for {len(failures)} students.")
else:
    print("No safety violations found. Model predictions are safe.")

total_students = len(students)
total_safe = total_students - len(failures)
print(f"\n Accuracy summary:")
accuracy = (total_safe / total_students) * 100
print(f"Accuracy: {accuracy:.2f}%")