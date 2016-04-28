from collections import Counter

fname = raw_input('Enter file name:')
fh = open(fname)
count = 0
name_count = []

for line in fh:
	line = line.rstrip()
	if line.startswith('From'):
		names = line.split()
		print names[1]
		count = count + 1
		name_count.append(names[1])

print 'There were', count, 'lines in the file with from as the first word'

print Counter(name_count)
