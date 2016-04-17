largest = None
smallest = None
while True:
	user = (raw_input("Enter Number, (enter 'done' to exit):"))
	if user == "done":
			break
	try: 
		int(user)	
	except:
		print "Value is not accepted, try again"
		continue
	user = int(user)
	if largest == None:
		largest = user
	elif user > largest:
		largest = user
	elif smallest == None:
		smallest = user
	elif user < smallest:
		smallest = user
	else:
		continue
	continue
print "Done!"
print "Maximum is " , largest
print "Minimum is" , smallest
#without user = int(user) on line 11, accepts as string, makes 67 > 600
