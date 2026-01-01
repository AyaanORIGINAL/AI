import random
cricket_prob = 50
user_actions = ["y", "n", "y", "y"]
print("training the algorithm")
for action in user_actions:
    if action == "y":
        cricket_prob += 15
        print(f"User liked, probability increased to {cricket_prob}%")
    else:
        cricket_prob -= 15
        print(f"User disliked, probability decreased to {cricket_prob}%")

print("\n Final Feed Generation")
for i in range(10):
    if random.randint(1, 100) <= cricket_prob:
        print(f"video {i+1}: Bangladesh vs India Cricket Highlights")
    else:
        print(f"video {i+1}: Bangladesh national anthem 🎵")
        
