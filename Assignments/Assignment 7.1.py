import re

fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
	line = line.rstrip()
	if 'computers' in line:
		print line