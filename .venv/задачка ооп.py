

import requests
import json

r = requests.post('https://baconipsum.com/api/?type=meat-and-filler')
r = json.loads(r.content)
print(r[0])