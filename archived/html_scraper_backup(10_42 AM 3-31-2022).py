# !/venv/Script python
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.language import Language
from spacy_language_detection import LanguageDetector
# import en_core_web_sm
# from bs4 import BeautifulSoup
import requests
import json
from collections import Counter
from string import punctuation
from heapq import nlargest
from googletrans import Translator
import re

class WebScraper():
    print("class WebScraper started")

    def __init__(self, uri):
        self.uri = uri

    def get_entities(self, nlp_model, page_text, limit=25):
        doc = nlp_model(str(page_text)[0:min(len(page_text), 1500)])
        # entities = []
        ents = dict()
        ent_label = list()
        ent_text = list()
        for ent in doc.ents:
            if ent.text is not None:
                # entities.append([ent.text.strip(), ent.label_.strip()])
                ent_label.append(ent.label_.strip())
                ent_text.append(ent.text.strip())

        max_len = min(len(ent_label), limit)
        for i in range(max_len):
            try:
                ents[ent_label[i]] = ents[ent_label[i]] + [ent_text[i]]
            except:
                ents[ent_label[i]] = [ent_text[i]]
        return ents

    # def _language(self, nlp, name):
    #     return LanguageDetector(seed=42)  # We use the seed 42

    # def get_language(self):
    #     Language.factory("language_detector", func=self._language)
    #     self.nlp.add_pipe('language_detector', last=True)
    #     doc = self.nlp(self.soup)
    #     language = doc._.language
    #     return language["language"]

    def get_translation(self, page_text):
        translator = Translator()
        translation = translator.translate(page_text, src="auto", dest="en")
        return translation

    def get_webpage(self, uri_string):
        print("requesting webpage")
        url = "https://arweave.net/" + self.uri
        response = requests.get(url)
        print("webpage response received, status code " + str(response.status_code))
        page_text = re.sub(r"[\r|\t|\n]+", "", response.text).replace("  "," ").replace("  "," ")
        return page_text

    def run(self):
        # self.nlp = en_core_web_sm.load()
        nlp = spacy.load("en_core_web_sm")
        print("spacy core loaded")
        page_text = self.get_webpage(uri_string=self.uri)
        ent = self.get_entities(nlp_model=nlp, page_text=page_text, limit=25)
        # lang = self.get_language()
        # if lang.lower() != "en":
        #     tran = self.get_translation()
        tran = self.get_translation(page_text=page_text)
        # else:
        #     tran = ""
        return {"named_entities": ent, "source_language": tran.src, "source_text": page_text, "english_text": tran.text.strip(r"\\\n\t\#")}


# x = WebScraper("IWdMfjLQo2mFlQ3ZBBVGwAghRI419mEw-HxufRIwF2g")
# print(x.run())

# if __name__ == '__main__':
#     WebScraper()