#CTI 110
#P1LAB2 - Receit
# Godbolt
#10/1/24

print("P1LAB2")
# For today, let's do a restaurant
#that only sells burgers and fries

#declare our variables
num_burgers = 0
num_fries= 0
burger_cost = 4.99
fry_cost = 0.99

print("Can I take your order?")
# we have to convert their input to an int
num_burgers = int(input("How many Burgers? "))

print ("You ordered" , num_burgers, "burgers")

num_fries = input("How many fries? ")
print("OK, that's", num_fries, "french fries.")

burger_total = num_burgers * burger_cost
print("$", burger_total)