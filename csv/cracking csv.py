with open("class_data.csv", "r") as file:
    lines = file.readlines()

header = lines[0].strip().split(",")
raw_data = lines[1:]

cleaned_data = []
for line in raw_data:
    values = line.strip().split(",")
    row_dict = dict(zip(header, values))
    cleaned_data.append(row_dict)

print(f"Column Detected: {header}")
print(f"First {len(cleaned_data)} rows of data:")
for row in cleaned_data:
    print(row)