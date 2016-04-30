# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.

largest = None
smallest = None
while True:
	num = raw_input("Enter a number: ")
	if num == "done": 
		break
	else:
		try:
			num = int(num)
		except:
			print "Invalid input"
			continue
	
		if largest is None:
			largest = num
		elif num > largest:
			largest = num
	
		if smallest is None:
			smallest = num
		elif num < smallest:
			smallest = num

print "Maximum is", largest
print "Minimum is", smallest