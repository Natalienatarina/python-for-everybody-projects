import urllib.request, urllib.parse
import json, ssl

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('===failure to retrieve===')
        print(data)
        continue

    plus_code = js['features'][0]['properties'].get('plus_code')
    if not plus_code:
        print('===No plus code found===')

    print('plus_code', plus_code)