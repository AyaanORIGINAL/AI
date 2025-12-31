data = ["Name, Age", "Ali,6", "Kuddus,7", "Zayan,8", "Dexter,9", "Joe,10"]
vip_list = [line.split(",")[0] 
for line in data[1:]
if int(line.split(",")[1]) >7]
print("VIP List:", vip_list)