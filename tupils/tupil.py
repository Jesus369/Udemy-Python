# Tupils which are similar to list. Tupils is an immutable object - They can't be changed easily changed like how a list can be.
# Another note is that lists are meant to hold items of the same type only.
# Where as tupils are intended to hold hetrogenius items. Explanation is that once an album is release, it's contents can not change.

welcome = "Welcome to my Nightmate", "Alice Cooper", 1971
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)        # Will print ["Ride the Lighting", "Metallica", 1984]
print(metallica[0])     # Will prit Ride the Lightning [0] represents the first string in "metallica".
print(metallica[1])
print metallica[2]
# Above is shown you calling the strings individually & below we print them all out together with a "for loop"
for i in metallica:
    print(i)
# metallica[0] = "Master of puppets" <-- This will NOT change the string to Master of puppets.
imelda = imelda[0], "Imelda May", imelda[2] # Go in order. When imelda[1], being the one you want to rename comes along. Instead of imelda[1], write the new name.
print(imelda)           #prints "More Mayhem", "Imelda May", "2011".

print("=" * 40)

# Unpackaging the tupil. We pair each string to a variable based the order they're assigned to.
data = "Meteora", "Linkin Park", 2001, ((1, "Forward"), (2, "Don't Stay"), (3, "Faint"), (4, "Breaking the Habit")) # Creating a master tupil with individual tupils.
title, artist, date, track = data
print(title)
print(artist)
print(date)
print(track)            # Calling the parent tupil will print all individual tupils inside of it.

for song in track:
    track, title = song # Setting variables for the songs in track
    print("\t Track Number {}: {}".format(track,title))

print("=" * 40)

for song in track:      # With a parent tupil we can't go through the children individually, so we use a "for loop".
    print(song)

print("=" * 40)

# Individual tupils with multiple characters within divided by commas. These tupils are then assigned a variable.
data2 = "Meteora", "Linkin Park", 2001, (1, "Forward"), (2, "Don't Stay")
album2, artist2, date2, track1, track2 = data2
print(album2)
print(artist2)
print(date2)
print(track1)
print(track2)
