fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh: 
	# reads line by line
	if line == 0 : continue
	wordlist = line.split()
	# print wordlist
	
	for word in wordlist :
		if word in lst : continue
		else:
			lst.append(word)

lst.sort()

print lst