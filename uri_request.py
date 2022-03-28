from urllib.parse import unquote
import requests
from arweave_api 

def magicId (content):
    from magic_lib import Magic
    m = Magic()
    return m.from_buffer(content)

def whatTheFile (uri):
    uri = unquote(str(uri))
    uri = "https://arweave.net/" + uri
    data = requests.get(uri)
    # dtext = data.text
    # print(dtext)
    return magicId(data.content)

# try:
#     uri = xsys.argv[1]
#     print(whatTheFile(uri))
# except:
#     print(whatTheFile('-UUtpZh3_A0VBnnU9fP0yon-xFV26d5uarXE-xMHMqY'))
#     pass

# print(whatTheFile('-UUtpZh3_A0VBnnU9fP0yon-xFV26d5uarXE-xMHMqY'))