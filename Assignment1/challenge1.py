ipAddress = raw_input("Please enter your IP Address:\t")

segment = 1
segmentLength = 0

for character in ipAddress:			# Character now takes over ipAddress's text
	if character == '.':			# If character includes a "." then the following will print.
		print("Segment {0} contains {1} characters.".format(segment,segmentLength))	# segment starts at 1 and segmentLength starts at number 0 
		segment += 1	# As the loop continues segment will continuously be added 1
		segmentLength = 0 # Will tell us the number of characters in character.
	else:
		segmentLength +=1

if character != '.':		# Important. If the character does not end with a dot then we ask python to print the characters
	print("Segment {0} contains {1} characters.".format(segment,segmentLength))
