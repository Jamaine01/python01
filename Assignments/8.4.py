fname = raw_input('Enter file name: ')
fh = open(fname)
_list = list()
for line in fh:
	line = line.split()
	for word in line:
		word = word.lower()
		if word not in _list:
			_list.append(word)

_list = sorted(_list)

print _list
