import requests
from requests.auth import HTTPBasicAuth
from requests.auth import AuthBase

auth = HTTPBasicAuth('ryan', 'password')
url = 'http://pythonscraping.com/pages/auth/login.php'
r = requests.post(url=url, auth=auth)
print(r.text)