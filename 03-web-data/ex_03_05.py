import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')


print('Retrieving: ', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

counts = tree.findall('.//count')
total = 0
for count in counts:
    total += int(count.text)
    print(count.text)

print('Count: ', len(counts))
print('Sum: ', total)
