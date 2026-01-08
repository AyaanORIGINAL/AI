test_set = [25, 60, 45 , 80 , 100]
def get_real_answer(n):
    return n > 50

correct = 0
total = len(test_set)
print("Starting Exam")
for n in test_set:
    prediction = [n > 50]
    actual = get_real_answer(n)

    if prediction == [actual]:
        correct += 1
        
score_percent = (correct / total) * 100
print(f"Final Score: {correct} / {total}({score_percent}%)")
