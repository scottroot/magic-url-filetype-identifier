# from uri_request import whatTheFile
# import subprocess
import requests


# print(whatTheFile("-UUtpZh3_A0VBnnU9fP0yon-xFV26d5uarXE-xMHMqY"))

# x = subprocess.check_output(['python', 'uri_request.py', '-UUtpZh3_A0VBnnU9fP0yon-xFV26d5uarXE-xMHMqY'])
# print(x.decode('UTF-8'))



uri = "https://arweave.net/" + "-UUtpZh3_A0VBnnU9fP0yon-xFV26d5uarXE-xMHMqY"
data = requests.get(uri)
dtext = data.content
# m = Magic()
print("test")

def test(dtext):
	from magic import Magic
	m = Magic()
	print(
		m.from_buffer(dtext)
		)
test(dtext)
# import puremagic

# filename = "test/resources/images/test.gif"

# ext = puremagic.from_file(filename)
# # '.gif'

# puremagic.magic_file(filename)
