import random

test_data = [random.randint(50, 150) for _ in range(20)]
total_questions = len(test_data)

def get_correct_ans(n):
    return "High" if n > 100 else "Low"

ai_score = 0
for num in test_data:
    prediction = "High" if num > 110 else "Low"
    if prediction == get_correct_ans(num):
        ai_score += 1

random_score = 0
for num in test_data:
    guess = random.choice(["High", "Low"])
    if guess == get_correct_ans(num):
        random_score += 1

ai_acc = (ai_score / total_questions) * 100
random_acc = (random_score / total_questions) * 100

print(f"Random Guessing Accuracy: {random_acc}%")
print(f"AI Predictor Accuracy: {ai_acc}%")

if ai_acc > random_acc:
    print("Success: AI outperformed random guessing!")
else:
    print("Failure: AI did not outperform random guessing.")