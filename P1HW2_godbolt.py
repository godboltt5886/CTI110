# CTI 110
# P1HW2
# T Godbolt
# 10/8/24


"""
3.Ask user to enter their budget
4.Ask user to enter travel destination
5.Ask user for amount they will spend on gas
6.Ask user for amount they will spend on accomodation
7.Ask user for amount they will spend on food
8.Add expenses
9.Subtract expenses from budget
10.Display results
"""

# Ask user to enter their budget
budget = float(input("Whats is your travel budget? $ "))
# Where are they going
destination = input("Where are you going? ")
# How much will they spend on gas
gas_expense = float(input("How much will you spend on gas? "))
# How much will they spend on accomodation
accommodation_expense = float(input("How much will you spend on accomodation? "))
# How much will they spend on food
food_expense = float(input("How much will you spend on food? "))
# Add expenses
total_expenses = gas_expense + accommodation_expense + food_expense
remaining_balance = budget - total_expenses

print("- Travel Expenses -")
print(f"Location: (Nashville)")
print(f"Initial Budget: ${budget:.2f}")
print(f"Fuel: ${gas_expense:.2f}")
print(f"Accommodation: ${accommodation_expense:.2f}")
print(f"Food: ${food_expense:.2f}")
print(f"Remaining Balance: ${remaining_balance:.2f}")