"""
Write a function that counts how many times the string "fizz" appears in a list.

Write a function called fizz_count that takes a list x as input. 

Create a variable count to hold the ongoing count. Initialize it to zero. for each item in x:, if that item is equal to the string "fizz" then increment the count variable. 

After the loop, please return the count variable.
"""

def fizz_count(x) :
	count = 0
	for item in x :
		if item == "fizz" :
			count += 1
	return count

x = []

print fizz_count(x)