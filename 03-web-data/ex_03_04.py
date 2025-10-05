from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('ENTER - ')
position = 18
count = 7

#print('Retrieving:', url)

#for i in range(n) means repeat the block n times, with i as the current loop index from 0 to n-1.
for i in range(count):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    if len(tags) < position:
        print('Error')
        break
#Use -1 becoz py count from 0
    tag = tags[position -1]
    url = tag.get('href', None)
    print('Retrieving', url)
print('Last name in result:', tag.text)