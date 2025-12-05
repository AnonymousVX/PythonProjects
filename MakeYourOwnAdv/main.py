name = input("What is your name: ")
print("Welcome", name, "to this adventure!")
answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way do you want to go? ")
if answer == "left":
    answer = input("You've come to a river, you can walk around it or swim across it. Type walk to walk around or swim to swim around")
    if answer == "walk":
        print("You walked across and the elephants crushed you.")
    elif answer == "swim":
        print("You swam across and were eaten by an alligator")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You come across a wobbly bridge, do you want to cross through it? (cross/back)")
    if answer == "cross":
        print("You crossed through it, you won the knighthood by the king")
    elif answer == "back":
        print("You backed down and the villagers threw stones at you.")
    else:
        print("Not a valid option. you lose.")
else:
    print("Not a valid option. you lose")