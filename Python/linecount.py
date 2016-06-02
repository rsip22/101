fhand = open('mbox-short.txt', 'r')
count = 0

for line in fhand:
	count = count + 1

print 'Line count: ', count