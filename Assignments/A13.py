import urllib
from BeautifulSoup import *
import re

url = urllib.urlopen('http://python-data.dr-chuck.net/comments_242237.html').read()

soup = BeautifulSoup(url)

tags = soup.findAll("span", { "class":"comments" })

nums = list()

for tag in tags:
	num = int(tag.text)
	nums.append(num)


print 'Sum', sum(nums), '\nCount', len(tags)







