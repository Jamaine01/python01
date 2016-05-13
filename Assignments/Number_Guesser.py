import time
from random import randint

while True:
	usr = int(raw_input('Enter Secret Number (0-100)!: '))
	try:
		usr < 101 and usr > -1
	except:
		print 'Please enter valid value. Try again.'
		continue

	print 'Guessing Number...'
	time.sleep(3)
	num_1 = randint(0,100)
	permanent_high = -1
	permanent_low = -1
	count = 1

	print num_1 ,'\n' ,'Is this number correct?'
	break

while True:
	if permanent_high - permanent_low == 2:
		print 'Your number is', randint(permanent_low + 1, permanent_high - 1), '!', '\n', 'Number of tries:', count
		break
	else:
		usr_ans = raw_input('Yes or No?:').lower()
		try:
			usr_ans == 'yes' or 'no'
		except:
			print 'Not a valid answer. Try again.'
			continue
		if usr_ans == 'yes':
			break
		elif usr_ans == 'no':
			count = count + 1
			hint = raw_input('Is your number higher or lower?:')
			try:
				hint == 'higher' or 'lower'
			except:
				print 'Not a valid answer. Try again.'
				continue
			if hint == 'higher':
				if permanent_low == -1:
					permanent_low = num_1
					print 'Guessing Number...'
					time.sleep(1)
					if permanent_high == -1:
						num_1 = randint(permanent_low + 1, 100)
						print num_1, '\n', 'Is this number correct?'
					else:
						num_1 = randint(permanent_low + 1, permanent_high - 1)
						print num_1, '\n', 'Is this number correct?'
					continue
				elif permanent_high != -1:
					permanent_low = num_1
					num_1 = randint(permanent_low + 1, permanent_high - 1)
					print num_1, '\n', 'Is this number correct?'
					continue
				else:
					permanent_low = num_1
					print 'Guessing Number...'
					time.sleep(1)
					num_1 = randint(permanent_low + 1, 100)
					print num_1, '\n', 'Is this number correct?'
					continue
			elif hint == 'lower':
				if permanent_high == -1:
					permanent_high = num_1
					print 'Guessing Number...'
					time.sleep(1)
					if permanent_low == -1:
						num_1 = randint(0, permanent_high - 1)
						print num_1, '\n', 'Is this number correct?'
					else:
						num_1 = randint(permanent_low + 1, permanent_high - 1)
						print num_1, '\n', 'Is this number correct?'
					continue
				elif permanent_low != -1:
					permanent_high = num_1
					num_1 = randint(permanent_low + 1, permanent_high - 1)
					print num_1, '\n', 'Is this number correct?'
					continue
				else:
					permanent_high = num_1
					print 'Guessing Number...'
					time.sleep(1)
					num_1 = randint(0, permanent_high - 1)
					print num_1, '\n', 'Is this number correct?'
					continue
print 'I have successfully guessed your number!', '\n', 'Number of tries:', count





