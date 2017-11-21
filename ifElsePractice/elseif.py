# Old enough to vote?
name = raw_input("What is your name?")
age = int(raw_input("How old are you?"))
if age >= 18:
	print("You can vote!")
else:
	print("Try again next time!")

print("\n\n")

# Can you guess my name?
print("Can you guess my age?")
guess = int(raw_input(""))
if guess < 24:
	print("Sorry guess higher")
	guess = int(raw_input(""))

	if guess == 24:
		print("Great job lab!")
	else:
		print("Better luck next time!")
elif guess > 24:
	print("Guess lower!")
	guess = int(raw_input(""))

	if guess == 24:
		print("Great job lad!")
	else:
		print("Better luck next time!")
else:
	print("Got it right the first time!")


print("\n\n")
# Run to the grocery store
response = "yes"

print("""Evan: Can you go and buy some apples for my salad!?
Steph: How many do you need?
Evan: 4 should be enough
*Drives to the grocery store*
Steph: Crap! How many apples did he say I needed to buy again?""")
demand = int(raw_input("Enter a number \t"))

# If user input is greater than 4 the following code will run.
if demand > 4:
	print("*Drives home* Uh oh! too many! I think it was suppose to be 4.")
	correct = raw_input("Was Jesus suppose to buy 4?")
	if  correct.lower() == response.lower():
		print("Well too much of something never killed anyone!")
	elif correct.lower() != response.lower():
		print("You're crazy! Shouldn't be asking you anyways!")
#But if the user input is less than 4 then this code will run. 
elif demand  < 4:
	print("*Drives home* Uh oh! too little! I think it was suppose to be 4 right?")
	correct = raw_input("Did jesus have to buy 4?")
	if correct.lower() == response.lower():
		print("i'm in for it when i get home!!")
	elif correct.lower() != response.lower():
		print("Quit your jibber jabbering!")
# Otherwise if it is neither less than or greater than 4 and the user guess 4 the first time the following code will run.
else:
	print("Good thing I've got a great memory!")
		












