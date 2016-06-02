import urllib
from BeautifulSoup import *
import xml.etree.ElementTree as ET

url =  'http://python-data.dr-chuck.net/comments_242234.xml'

uhand = urllib.urlopen(url).read()

info = ET.fromstring(uhand)

comments = info.findall('comments/comment')
total = 0

for comment in comments:
		total = total + int(comment.find('count').text)
print total



#print uhand