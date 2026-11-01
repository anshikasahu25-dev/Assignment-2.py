
# Monthly Savings

money = float(input("Enter pocket money: "))
canteen = float(input("Canteen expense: "))
transport = float(input("Transport expense: "))
shopping = float(input("Shopping expense: "))

total = canteen + transport + shopping
saving = money - total

safe = saving >= 0

print("Total Expense:", total)
print("Saving:", saving)
print("Budget Safe:", safe)
