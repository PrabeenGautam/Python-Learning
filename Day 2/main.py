print("Welcome to the tip calculator")
bill = input("What was your total bill? $")
total_number = input("How many people to split the bill? ")
percentage = input("What % tip would you like to give? 10, 12, or 15? ")

total_money = float(bill) + (int(percentage) / 100) * float(bill)
each_bill = total_money / int(total_number)

print("Each person should pay: " + str(round(each_bill, 2)))