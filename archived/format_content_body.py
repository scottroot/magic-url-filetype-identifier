import json
from scraping_helpers.language_translate import translateLanguage
import re
import jsom



txt = 	"""
		{"name": "Frog "#"5093", "symbol": "FROG", "description": "8888 randomly generated Frogs stored on the Solana blockchain, made with over 130 unique traits of varying rarity. Each Cyber Frog is non-sequentially minted and provably unique.", "seller_fee_basis_points": 999, "external_url": "https://cyberfrogs.io", "image": "https://www.arweave.net/Y_1jJzemEtvtrTJuiyn68iRBIHVO2O8tzvbS49m7hWU?ext=png", "attributes": [{"trait_type": "Background", "value": "Light Green"}, {"trait_type": "Skin", "value": "Ghost"}, {"trait_type": "Eyes", "value": "Stoned"}, {"trait_type": "Outfit", "value": "Leather Jacket"}, {"trait_type": "Item", "value": "SMG"}, {"trait_type": "Headware", "value": "Orange Ski Goggles"}, {"trait_type": "Mouth", "value": "Toothpick"}], "properties": {"creators": [{"address": "frogQCpP8LpgfhhpusLvNoRw6sjmsX3Vij7MF8KtHn2", "share": "28"}, {"address": "6ojTWAjYzuWdiXrxSqmxRLzzvq5MMe1gG4L1wZ1cfpdo", "share": "10"}, {"address": "ERTxeMLoJfJnBmpStLVyqMfzG2gsHbqdrPKtf4ekBcWk", "share": "26"}, {"address": "6uzzoNMHk9S4ug9b47YszofJe3FtXpg8BxAKUHhH7nBY", "share": "22"}, {"address": "EYcrmJ2RsXrDYL9FpvgiKTfWHCYLnzjZwL3PkJ84DA6U", "share": "14"}]}}
		"""
# txt = translateLanguage(txt)
# txt2 = json.dumps(json.loads(txt), indent=4)
# print(txt2)
# print(txt["created_at"])
# x = jsom.JsomParser().loads(txt)
# print(json.dumps(x, indent=4))
# print("\n".join(re.findall(r'("[A-z0-9]+":\S[A-z0-9\:\+ ]+[\",]),', txt)))

# x = txt.replace("\"", "").replace("{","").replace("}","").replace("\\","")

# (?# url = re.findall(r".+(arweave.net/[A-z0-9_\?\=]+)\,", x))

x = re.findall(r".*", txt)

x = re.sub(r"[{|}|\[|\]]","", txt).replace("\t","").replace("\n","")
x = x.replace(" \"", "\"").replace("\" ", "\"").split(",")

x = [i.split(":") for i in x]
print(x)