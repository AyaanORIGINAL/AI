from collections import Counter, namedtuple
Record = namedtuple('Record', ['marks', 'actual'])

def predict_outcome(marks):
    return 'pass' if marks >= 60 else 'fail'

test_grp = {
    Record(58, 'fail'), Record(61, 'pass'),
    Record(59, 'pass'), Record(62, 'pass'),
    Record(60, 'fail'), Record(59, 'fail'),

}

audit_log = Counter()
print("Running audit cycle")
for student in test_grp:
    prediction = predict_outcome(student.marks)
    if prediction == student.actual:
        status = "Prediction Correct"
    else:
        status = "Model error"


    audit_key = f"{status}: Predicted {prediction}, Actual {student.actual}"
    audit_log[audit_key] += 1
for outcome, count in audit_log.items():
    print(f"[{count}] {outcome}")