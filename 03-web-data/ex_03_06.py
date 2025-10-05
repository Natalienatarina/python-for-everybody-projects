import urllib.request

url = input('Enter location: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_2301441.json'


print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()

import json
info = json.loads(data)

total = 0

for item in info["comments"]:
    total += int(item["count"])

print('count', len(data))
print('sum', total)    