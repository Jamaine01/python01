import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
	address = raw_input('Enter location: ')
	if len(address) < 1 :
		break
	elif address == 'exit':
		break
	url = serviceurl + urllib.urlencode({'sensor':'false', 'address':address})
	print 'Retrieving', url
	info = urllib.urlopen(url).read()
	print 'Retrieved', len(info),'characters'

	try:
		js = json.loads(str(info))
	except:
		js = None

	if 'status' not in js or js['status'] != 'OK':
		print '==== Failure to Retrieve ===='
		print info
		continue

	print json.dumps(js, indent=4)

	lat = js['results'][0]['geometry']['location']['lat']
	lng = js['results'][0]['geometry']['location']['lng']
	
	print 'lattitude:',lat , '\n longitude:',lng

	location = js['results'][0]['place_id']
	break

print location
