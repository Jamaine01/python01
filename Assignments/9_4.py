fname = raw_input('Enter file name: ')

try:
	open(fname)
except:
	print 'File does not exist'

lst_emails = []
dct_emails = dict()
fh = open(fname)

for line in fh:
	line = line.rstrip()
	if line.startswith('From '):
		lst_words = line.split()
		lst_emails.append(lst_words[1])
for email in lst_emails:
	dct_emails[email] = dct_emails.get(email, 0) + 1

emails_tup = dct_emails.items()
emails_val_1st = []

for email, count in emails_tup:
	emails_val_1st.append((count, email))

emails_val_1st.sort(reverse=True)

print emails_val_1st[0]
