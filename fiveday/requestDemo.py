import requests


res = requests.get('https://petstore.swagger.io/v2/pet')
print(res.text)
