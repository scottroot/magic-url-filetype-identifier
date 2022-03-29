from bs4 import BeautifulSoup
import requests
import json
from collections import Counter
from string import punctuation
from heapq import nlargest
from googletrans import Translator
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.language import Language
from spacy_language_detection import LanguageDetector
import en_core_web_sm
import re


class WebScraper():

    def __init__(self, uri):
        self.uri = uri
        self.nlp = en_core_web_sm.load()

    def get_entities(self, limit=25):
        doc = self.nlp(self.soup)
        entities = []
        for ent in doc.ents:
            if ent.text is not None:
                entities.append([ent.text.strip(), ent.label_.strip()])
        return entities[0:limit]

    def _language(self, nlp, name):
        return LanguageDetector(seed=42)  # We use the seed 42

    def get_language(self):
        Language.factory("language_detector", func=self._language)
        self.nlp.add_pipe('language_detector', last=True)
        doc = self.nlp(self.soup)
        language = doc._.language
        return language["language"]

    def get_translation(self):
        translator = Translator()
        translation = translator.translate(self.soup, src="auto", dest="en")
        return translation.text

    def get_webpage(self):
        url = "https://arweave.net/" + self.uri
        response = requests.get(url)
        # r = response.text.strip()#replace("\n","").replace("  "," ")
        soup = BeautifulSoup(response.content, "html.parser").text
        self.soup = re.sub(r"[\r|\t|\n]+", "", soup).replace("  "," ").replace("  "," ")

    def run(self):
        self.get_webpage()
        ent = self.get_entities()
        lang = self.get_language()
        if lang.lower() != "en":
            tran = self.get_translation()
        else:
            tran = ""
        return {"named_entities": ent, "source_language": lang, "source_text": self.soup, "english_text": tran}


# x = WebScraper("C9I8KiECwbjnYxMYoyRC3MqtuQI0RKze59aoNiyXKEI")
# print(x.run())