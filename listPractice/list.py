shopping_list = ["milk", "eggs", "bread", "chicken", "pasta", "rice"]	# Our list
for item in shopping_list:												# "Item" is now taking each string in shopping list
#	print("You need to buy {0}".format(item))     # Or....
	print("You need to buy " + item)

print("-" * 40)#--------------------------------------------------------------------------------------------------------------

item_list = ["pencils", "paper", "pens", "markers", "highlighters"]
for unecessary in item_list:				# "unecessary" takes on the strings within the array.
	if unecessary == "paper":			# if "unecessary" happens to come across "paper" as it's looping.
		continue				# Then "paper" will be overlooked and will continue on after "paper".
# 		break					# If "break" then the for loop will end as soon as it hits "paper".
	print("Buy " + unecessary)


print("-" * 40)#--------------------------------------------------------------------------------------------------------------

notDoing = ["pinin", "eating", "exercising", "meditating"]
for verb in notDoing:
	print("My parrot is not " + verb)

print("-" * 40)#--------------------------------------------------------------------------------------------------------------

set1 = [34, 54, 2, 5]
set2 = [3, 45, 100, 7]
complete = set1 + set2
complete.sort()						# Will sort the numbers within "complete" in numerical order.
print(complete)
print(sorted(complete)) 				# Sorts the numbers in order.

print("-" * 40)#--------------------------------------------------------------------------------------------------------------

ipAddress = raw_input("Please enter an IPAddress: \t")
print(ipAddress.count(".")) 				# Will count the number of sequences each time.

print("-" * 40)#--------------------------------------------------------------------------------------------------------------

myCar = ["cleaned", "washed", "vacuumed", "scented"]
myCar.append("in the shop") 				# Adds "in the shop" to the list of arrays using the "append" function.
for toDo in myCar:
	print("My car needs to be " + toDo)

print("-" * 40)#--------------------------------------------------------------------------------------------------------------

list1 = [1, 43, 7, 32, 56]
rev_list1 = list1					# rev_list1 now has the properties of list1
rev_list1.sort(reverse=True)				# rev_list1 will have it's numbers sorted, although now with the reverse=True we are assorting them from greated to lowest
print(list1)						#list1 and rev_list1 are the same so list1 will print out what rev_list1 has

print("-" * 40)#--------------------------------------------------------------------------------------------------------------

numbs1 = [2, 3, 4, 546, 456, 45]
numbs2 = [324, 32, 5, 8, 8, 23]
for numb_set in [numbs1, numbs2]:			# Prints out numbs1 and numbs2 as a whole set
	print numb_set
	for individuals in numb_set:			# Prints out numbs1 and numbs1 and its individual listing numbers
		print(individuals)

print("-" * 40)#--------------------------------------------------------------------------------------------------------------

menu = []
menu.append(["spam", "egg", "bacon"])
menu.append(["spam", "bacon", "egg"])
menu.append(["bacon", "egg", "cheese"])
menu.append(["spam", "cheese", "spam", "bacon"])
menu.append(["spam", "spam", "egg", "bacon"])
menu.append(["spam", "bacon", "spam", "egg"])
menu.append(["egg", "cheese", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "spam", "bacon", "spam", "spam"])

for meal in menu:
	if not "spam" in meal:				# Searches for a list without "spam" in it
		print(meal)
		for ingredient in meal:
			print(ingredient)

print("-" * 40)#--------------------------------------------------------------------------------------------------------------

week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
my_iterator = iter(week)				# my_iterator is now "week" although the iter function starts listing the array of week individually
for i in range(0, len(week)):
	next_day = next(my_iterator)			# goes through the array of my_iterator printing them out one after another, hence the "next" function
	print(next_day)
