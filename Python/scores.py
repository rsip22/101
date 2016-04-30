score = raw_input("Enter Score: ")
inp = float(score)

if inp >= 0.9:
    print "A"
elif inp >= 0.8:
    print "B"
elif inp >= 0.7:
    print "C"
elif inp >= 0.6:
    print "D"
elif inp < 0.6:
    print "F"
else:
    print "This value is out of range."
    quit()