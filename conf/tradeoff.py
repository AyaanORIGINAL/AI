def model_inclusive(score):
    return "Selected" if score >= 60 else "Not Selected"

def model_selected(score):
    return "Selected" if score >= 85 else "Not Selected"

applicants = [
    {"id": 1, "score": 90, "merit": True},
    {"id": 2, "score": 80, "merit": False},
    {"id": 3, "score": 78, "merit": True},
    {"id": 4, "score": 60, "merit": False},
    {"id": 5, "score": 50, "merit": False},
]
print(f"{'ID':<4} {'Score':<6} {'Merit':<8} {'Inclusive Model':<16} {'Selected Model':<20}")
for applicant in applicants:
    res_a = model_inclusive(applicant["score"])
    res_b = model_selected(applicant["score"])

    cost_a = "Waste" if (res_a == "Selected" and not applicant["merit"]==True) else ""
    cost_b = "Exclusion" if (res_b == "Not Selected" and applicant["merit"]==True) else ""

    print(f"{applicant['id']:<2} {applicant['score']:<5} {str(applicant['merit']):<6} | {res_a:<8} {cost_a: <8}| {res_b:<10} {cost_b:<10}")