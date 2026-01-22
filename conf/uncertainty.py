def cautious_model (marks):
    if marks >=65:
        return "Pass"
    elif marks <=50:
        return "Fail"
    else:
        return "Uncertain"
    
marks = [50, 58 , 60 , 62 , 70]
actual = ["Fail", "Fail", "Pass", "Pass", "Pass"]
print("Confidence check")
for m, a in zip(marks, actual):
    print(f"Marks: {m} | Prediction: {cautious_model(m)} | Actual: {a}")