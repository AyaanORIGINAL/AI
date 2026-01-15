class BiometricScanner:
    def __init__(self, threshold=0.00):
        self.threshold = threshold
        self.logs = []

    def scan_face(self, person_id, confidence):
        status = "Allowed" if confidence >= self.threshold else "Denied"

        log_entry = {
        "person_id": person_id,
        "confidence": confidence,
        "status": status
    }
    
        self.logs.append(log_entry)
        return log_entry

SecurityLevel = 0.85
scanner = BiometricScanner(SecurityLevel)
attempts = [
    {"person_id": "Zayan_Emp", "confidence": 0.92},
    {"person_id": "Unknown_1", "confidence": 0.60},
    {"person_id": "Joe_CEO", "confidence": 0.82},
    {"person_id": "Unknown_2", "confidence": 0.45},
]
print(f"Security System Active (Threshold: {SecurityLevel*100}%)\n")
for attempt in attempts:
    result = scanner.scan_face(attempt["person_id"], attempt["confidence"])

    if result["status"] == "Allowed":
        print(f"Access Granted to {result['person_id']} (Confidence: {round(result['confidence']*100, 2)}%)")
    else:
        print(f"Access Denied to {result['person_id']} (Confidence: {round(result['confidence']*100, 2)}%)")

print("Incident report:")
ceo_entry = next(x for x in scanner.logs if x["person_id"] == "Joe_CEO")
if ceo_entry["status"] == "Denied":
    print("False negative detected for CEO!")
else:
    print("All clear. No incidents detected.")
    