from sys import argv

script, fileFrom, fileTo = argv

openedFile = open(fileFrom)
print "this is storage:", openedFile
indata = openedFile.read()
print "this is indata: %s" % indata

# fileTo = open()
outFile = open(fileTo, "w")
outFile.write(indata)

print "so this is outFile now: %r" % outFile
print "and this is fileTo: %r" % fileTo

openedFile.close()
outFile.close()
