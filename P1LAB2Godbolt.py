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

num_fries = int(input("How many fries? ") )
print("OK, that's", num_fries, "french fries.")

burger_total = num_burgers * burger_cost
print("$", burger_total)
fry_total = num_fries * fry_cost 
meal_total = burger_total + fry_total




print("-" * 20)
print(num_burgers, format(burger_total,".2f") )
print(num_fries, format(fry_total, ".2f") )
print("-" * 20)
print("Total\t\t$", format(meal_total, ".2f") )