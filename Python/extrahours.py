# Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use raw_input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly. 

try:
    hrs = raw_input("Enter Hours:")
    h = float(hrs)
    rate = raw_input("Enter Pay:")
    r = float(rate)
except:
    print "Error, please enter a numeric input."
    quit()

if h > 40:
    extra_hours = h - 40
    extra_hour_rate = r * 1.5
    extra_hours_pay = extra_hours * extra_hour_rate
    totalpay = ( 40 * r ) + extra_hours_pay

else:
    totalpay = ( h * r )

print totalpay