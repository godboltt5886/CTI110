# CTI 110
#P3LAB2 - Grades and Games
#Godboltt
#10/29/24


def main():
    print("Craps Game")
    print("roll from 1 to 6")
    die1 = int(input("First Die:"))
    die2 = int(input("Second Die:"))

    total = die1 + die2
    print("Roll:" , die1, "+", die2, "is",total)

    # did we win or lose?
    # 7 or 11 -> win, 2 or 12 -> lose, rest -> to be continued
    if total == 7:
        print("You win!")
    elif total == 11:
        print("You win!")
    elif total == 2:
        print("You lose.")
    elif total == 12:
        print ("You lose.")
    else:
        print("point was", total)
        print("to be continued...")


# start progam
main()
    
