import requests

req = requests.get('https://petstore.swagger.io/v2/pet/1')
print(req.json())
assert req.status_code ==200
assert req.json()['id'] ==1
assert req.elapsed.total_seconds()<=3


