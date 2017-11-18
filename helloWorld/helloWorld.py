print("Hello World")
print(1 + 2)
print(7 - 2)
age = "24"
month = "May"
year = "1993"
firstName = "Jesus"
lastName = "Flores"
print(firstName + " " +lastName)
print("This person is reffered to as " + firstName + " " + lastName + " and he was born on " + month + " " + year + " which makes him " + age + " years old!")


#User Interface
greeting = "Hello"
name = raw_input("What's your name?")
print(greeting + " " + name)

#splitSting
# "\n" Will cause a break and create a new line for any text included after it
splitString = "This line will be \nDivided into many lines \nAs you see here. \nThe backslash-n function \nWill perform this."
print(splitString)

#anotherSplitString
# Triple quotes will make it easier to divide strings into seperate lines.
print("""This stentence will
be devided into two seperate lines""")

#tabString
# "\t" will cause an indent between text
tabString = "1\t2\t3\t4\t5\t6"
print(tabString)
