backpack = ["water", "food", "bandage", "torch", "map"]
new_item = input("Enter an item you found: ")
print("You found a", new_item)

if len(backpack) >=5:
    remove_item = input("Your backpack is full. Which item would you like to remove? " )
    backpack.remove(remove_item)
backpack.append(new_item)
print("Current inventory:", backpack)