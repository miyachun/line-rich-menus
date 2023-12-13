import requests

headers = {"Authorization":"Bearer XXX","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-XXX', headers=headers)

print(req.text)