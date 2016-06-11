counts = dict()
print "Enter a line of text: "
line = raw_input()

words = line.lower().split()

print "Counting..."
for word in words :
	counts[word] = counts.get(word,0) + 1

print "Counts ", counts