# for i in range(0,21):		# The range in "i" is 0 - 21.
# 	print("i is now {0}.".format(i))


# number = "9,234,543,767,243"
# for i in range(0, len(number)): 					# Ranges from 0 to the end of the full length of "number".
# 	print(number[i])			 			# Square bracket prints out each character in the "i" which is the full length of number. Otherwise "number"  will continue to print equal to the amount of characters it has.


number = "9,234,543,767,243"
new_number = ''								# An empty string which will contain a comment later
for i in range(0, len(number)):						# Explaining "i" represents the range, starting from 0 to the full length of number
	if number[i] in "123456789":					# If each character is in [i] is in "123456789"
		new_number = new_number + number[i] 			# "new number" will equal itself plus the numbers within the span of number[i]
converted_number = int(new_number)					# convert_number will equal int(new_number). converted to int because it was once a string
print("{0}".format(converted_number))

for state in ["helpful", "excited", "demandful", "hard worker"]:	# for state in the "array" meaning that state has now taken over the properties of the array
	print("This parrot is {0}".format(state))			# Will loop through each string in the array until it reaches the end


for length in range(0,100,5):		# The third value will count through in 5's from 0(starting) till 95(end).
	print("We are counting in 5's\t {0}".format(length))


# Multiplication table
for i in range(1,13):							# "i" will represent the range between 1 - 12.
	for j in range(1,13):						# "j" will represent the range between 1 - 12.
		print("{0} * {1} is {2}".format(i, j, i*j))		# Print will be as formatted
	print("=" * 40)							# Including a space between each mult table


shopping_list = ["milk", "eggs", "bread", "chicken", "pasta", "rice"]	# Our list
for item in shopping_list:						# "Item" is now taking each string in shopping list
#	print("You need to buy {0}".format(item))    			# Or....
	print("You need to buy " + item)

print("=" * 40
	)
item_list = ["pencils", "paper", "pens", "markers", "highlighters"]
for unecessary in item_list:						# "unecessary" takes on the strings within the array.
	if unecessary == "paper":					# if "unecessary" happens to come across "paper" as it's looping
		continue						# Then "paper" will be overlooked and will continue on after "paper"
# 		break							# If "break" then the for loop will end as soon as it hits "paper"
	print("Buy " + unecessary)
