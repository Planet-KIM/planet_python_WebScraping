import json
from urllib.request import urlopen

def getCountry(ipAddress):
    url = 'http://api.ipstack.com/' + ipAddress
    url += '?access_key=ACCESS_KEY&amp;format=1'
    response = urlopen(url).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get('country_code')

print(getCountry('50.78.253.58'))