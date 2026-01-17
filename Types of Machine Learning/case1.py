marks = [92, 95, 33, 30]
grp1 = []
grp2 = []
for m in marks:
    if m > 50:
        grp1.append(m)
    else:
        grp2.append(m)
print("Logic error, Meaningless grouping")
print(f"Group 1: {grp1} (pass? fail? unknown)")
print(f"Group 2: {grp2} (just different from grp 3)")

reward = 0
guess = "A"
print("\n LOGIC ERROR Inefficient Learning")
if guess == "A":
    reward += 1
print(f"Reward: {reward}")
print("System learnt nothing about *why* A was correct.")