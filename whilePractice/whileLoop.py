# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1


# Prompting the user to chose a direction using a whie loop and if statements
direction = ["south", "east", "west", "north"]
chosenExit = ""
while chosenExit not in direction:
    chosenExit = (raw_input("Please chose a direction: \t"))
    if chosenExit == "quit":
        print("Game Over!")
        break
    elif chosenExit != direction:
        print("This is not a direction!")
else:
    print("Aren't you glad you got out!")


import random

# Requesting the user to guess a number and seeing if the entered number equals the random number
highest = 10
integer = random.randint(1,highest)

print("please guess a number")
guess = int(raw_input(""))

if guess != integer:
    if guess < highest:
        print("Please guess higher")
    else:
        print("Please guess lower.")
    guess = int(raw_input(""))
    if  guess == integer:
        print("You've guess correctly")
    else:
        print("Sorry you did not guess correctly")
else:
    print("Congratulations. You got it the first time")


# Same concept as the method above although this time the user has an unlimited amount of guesses rather than just 2

higher = 10
answer = random.randint(1,higher)
option = 0
while option !=  answer:
    option = int(raw_input("Please guess a number: \t"))
    if option < answer:
        print("Please guess higher")
    elif option > answer:
        print("Please guess lower!")
    else:
        print("Great job! Got it right!")
