import magic
from urllib.parse import unquote
import requests
import sys

def whatTheFile (uri):
    uri = unquote(str(uri))
    uri = "https://arweave.net/" + uri
    data = requests.get(uri)
    dtext = data.text
    # m = magic.Magic()
    # found = m.from_buffer(data.content)
    return magic.from_buffer(data.content)
# print(whatTheFile("bfWnri0wv_Hw-qFldml8OtBmJl-SoCwVJtuaN90sxTk"))

try:
    uri = sys.argv[1]
    print(whatTheFile(uri))
except:
    pass