hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter hourly rate:").replace("$","")
r = float(rate)
if h <= 40:
	print "Your pay is: $" , h*r
else:
	print "Your pay is: $" , (h*r) + ((h-40)*(r*1.5))-((h-40)*r)

	