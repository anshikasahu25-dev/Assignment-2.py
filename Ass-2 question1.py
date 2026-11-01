item1 = float(input("Enter your first item price :"));
item2 = float(input("Enter your second item price:"));

total = item1 + item2
discount = total *15/100
final_bill = total- discount +99

print("total:", total )
print("discount :", discount)
print("delievery fee:99")
print("final_bill :", final_bill)
