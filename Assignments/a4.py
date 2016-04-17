largest = None
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
	continue
print "Done!"
print "Maximum is " , largest
#without user = int(user) on line 12, accepts as string, makes 67 > 600
