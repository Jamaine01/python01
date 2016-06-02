
import urllib 
from BeautifulSoup import *

count = 7
url = 'http://python-data.dr-chuck.net/known_by_Ross.html'

while count > 0:
	url_parsed = BeautifulSoup(urllib.urlopen(url).read())

	tags = url_parsed('a')

	links = list()

	for tag in tags:
		links.append(tag.get('href', None))
	
	url = links[17]
	count -= 1


print 'Final Name: ', url
	


