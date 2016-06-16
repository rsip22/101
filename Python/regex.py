"""
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression and then converting the extracted strings to integers and summing up the integers. 
Actual data: http://python-data.dr-chuck.net/regex_sum_234794.txt (There are 73 values and the sum ends with 662)

"""

import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "regex_sum_234794.txt"
handle = open(name, "r")

sumall = []

for line in handle:
	numbers = re.findall('[0-9]+', line)
	if len(numbers) < 1 : continue
	for item in numbers :
		sumall.append(int(item))

print sum(sumall)