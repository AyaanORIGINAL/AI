import random
data_set = [x for x in range(10,210,10)]
random.shuffle(data_set)
split_index = int(len(data_set) * 0.8)

train_set = data_set[:split_index] 
test_set = data_set[split_index:]

print(f"Total Data points : {len(data_set)}")
print("-" * 30)
print(f"Training Set {len(train_set)} items")
print(f"-> {train_set}")
print(f"\n Testing Set {len(test_set)} items")
print(f"-> {test_set}")