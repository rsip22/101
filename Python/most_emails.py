"""
Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 

The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 

After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name, "r")
words = list()
counts = dict()

for line in handle:
	if not line.startswith("From ") : continue
	sender = line.split()
	words.append(sender[1])
	counts[sender[1]] = counts.get(sender[1],0) + 1
	
most_emails = None
bigcount = None

for line,count in counts.items():
	if bigcount is None or count > bigcount :
		most_emails = line
		bigcount = count

print most_emails, bigcount