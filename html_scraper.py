# !/venv/Script python
import spacy
# from spacy.language import Language
# from spacy_language_detection import LanguageDetector
# import en_core_web_sm
# from bs4 import BeautifulSoup
import requests
# from googletrans import Translator
import re


def get_webpage(uri_string):
    print("requesting webpage for {}".format(uri_string))
    url = "https://arweave.net/" + uri_string
    response = requests.get(url)
    print(" -- webpage response received\n -- status code {}".format(str(response.status_code)))
    page_text = response.text#re.sub(r"[\r|\t|\n]+", "", response.text).replace("  "," ").replace("  "," ")
    return page_text

def get_entities(page_text, limit=25):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(str(page_text)[0:min(len(page_text), 1500)])
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

# def _language(nlp, name):
#     return LanguageDetector(seed=42)  # We use the seed 42

# def get_language(text_string):
#     print(" -- starting language")
#     nlp = spacy.load("en_core_web_sm")
#     Language.factory("language_detector", func=_language)
#     nlp.add_pipe('language_detector', last=True)
#     doc = nlp(text_string)
#     language = doc._.language
#     return language["language"]

# def get_translation(page_text):
#     print("starting translator")
#     translator = Translator()
#     print("translator loaded")
#     translation = translator.translate(page_text, src="auto", dest="en")
#     print("returning translation")
#     return translation


def scrape_url(uri):
    page_text = get_webpage(uri_string=uri)
    page_string = re.sub(r"[“”‘’]+", "'", page_text)
    # page_text = str(re.sub("[.+]|(.+)|\n|\t", " ", page_text)).replace(r"\#","")
    # page_text = "".join(char for char in page_text if char.isalnum() or char == " ")
    # page_text = re.sub(" [^A-Za-z0-9]+", "", str(page_text))
    # lang = get_language(text_string=page_string)
    # tran = get_translation(page_text=page_text)
    # print("saved translation to var 'tran'")
    print(" -- starting get_entities()")
    ent = get_entities(page_text=page_string, limit=25)
    # page_text = r'{}'.format(page_text).replace("\\\\n", "").replace("\\\\\"","'")
    # return {"named_entities": ent, "source_language": lang, "source_text": page_string}#, "english_text": tran_text}
    return {"named_entities": ent, "source_text": page_string}#, "english_text": tran_text}


# x = scrape_url("EnJ2fc9CY846xNi4grtKQhg6TRifG_oib2hhj4LrrGU")
# print(x)

# if __name__ == '__main__':
#     WebScraper()