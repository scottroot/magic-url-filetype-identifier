import requests
import json

r = requests.get("https://python-magic-filetype.herokuapp.com/api")
print(r.text)