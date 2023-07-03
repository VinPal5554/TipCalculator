print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_percentage = (tip / 100) + 1
people = int(input("How many people to split the bill? "))

split_payment = (total_bill / people) * tip_percentage
split_payment2 = "{:.2f}".format(split_payment)
print(f"Each person should pay: {split_payment2}")