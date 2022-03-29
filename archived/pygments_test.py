import inspect
import urllib
import magic
from urllib.request import urlopen
from urllib.parse import unquote
import requests

def get_file (uri):
    uri = unquote(str(uri))
    uri = "https://arweave.net/" + uri
    data = requests.get(uri)
    dtext = data.text
    return dtext

def whatTheFile(text: str):
    from pygments.lexers import guess_lexer
    lexer = guess_lexer(text)
    mimetype = lexer.mimetypes[0] if lexer.mimetypes else None
    print(mimetype)

def magicFile(url):
    # m = magic.Magic()
    request = urllib.request.Request("https://arweave.net/"+url)
    response = urlopen(request)
    mime_type = magic.from_buffer(response.read(128))
    print(mime_type)

url = "-UUtpZh3_A0VBnnU9fP0yon-xFV26d5uarXE-xMHMqY"
file = get_file(url)
whatTheFile(file)
magicFile(url)

# if __name__ == "__main__":
#     # Set the text to the actual defintion of _test(...) above
#     text = inspect.getsource(_test)
#     print('Text:')
#     print(text)
#     print()
#     print('Result:')
#     _test(text)