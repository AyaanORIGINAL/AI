scoreboard = [6, 4, "Error", 1, "6", 0, -5, "Wide", 10]
valid_runs = []
total_score = 0

for item in scoreboard:
    if isinstance(item, int):
        if item >= 0:
            valid_runs.append(item)
    elif isinstance(item, str) and item.isdigit():
      
        valid_runs.append(int(item))
    

total_score = sum(valid_runs)
print("Valid Runs:", valid_runs)
print("Final Score:", total_score)
