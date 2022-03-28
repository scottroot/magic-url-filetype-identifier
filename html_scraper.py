# pip install bs4
import requests
import json
from bs4 import BeautifulSoup
from scraping_helpers.entity_detector import recognizeEntities
from scraping_helpers.language_detector import identifyLanguage
from scraping_helpers.language_translate import translateLanguage
from scraping_helpers.frequency_finder import topWords

def scrapeWebpage (uri):
	url = "https://arweave.net/" + uri

	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")
	soup_doc = [i.text for i in soup.find_all('p')]
	if len(soup_doc) < 1:
		soup_doc = soup.text
	# soup_doc = "\n".join(soup_doc)
	if str(soup_doc)[0] == "{":
		# print(soup_doc)
		return json.loads(soup_doc)
	else:
		language = identifyLanguage(soup_doc)
		translated = translateLanguage(soup_doc)["text_english"]
		entities = recognizeEntities(soup_doc, limit=25) # [['Apple', 'ORG'], ['UK', 'GPE'], ['$1 billion', 'MONEY']]
		top_words = topWords(translated, length=25)
		return {"language":language, "entities":entities, "top_words":top_words}