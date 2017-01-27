from sys import argv

fromHere, toHere = argv

print "Starting with fromHere file: %r" % fromHere
print "now opening fromHere and setting to variable"

openedFile = fromHere.open()

print "This is opened fromHere file: %r" % openedFile
print "Now making variable to hold new file we are writing to"

writingHere.open("w")
print "Now writing openedFile to writingHere"
writingHere.
