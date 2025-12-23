raw_data = [85, "N/A", 90, -5, "100", 75, "Error"]
clean_data = []
for item in raw_data:
    if str(item).isdigit():
        value = int(item)
        clean_data.append(value)
    elif isinstance(item, int) and item > 0:
        clean_data.append(item)
print("Original:", raw_data)
print("Cleaned:", clean_data)