# pip install spacy
# pip install spacy-language-detection
# !python -m spacy download en_core_web_lg
import spacy
from spacy.language import Language
from spacy_language_detection import LanguageDetector




def get_lang_detector(nlp, name):
    return LanguageDetector(seed=42)  # We use the seed 42

def identifyLanguage (text):
    nlp_model = spacy.load("en_core_web_sm")
    Language.factory("language_detector", func=get_lang_detector)
    nlp_model.add_pipe('language_detector', last=True)

    # Document level language detection
    doc = nlp_model(text)
    language = doc._.language
    return language["language"]

    # # Sentence level language detection
    # # text = "This is English text. Er lebt mit seinen Eltern und seiner Schwester in Berlin. Yo me divierto todos los días en el parque. Je m'appelle Angélica Summer, j'ai 12 ans et je suis canadienne."
    # doc = nlp_model(soup.text)
    # for i, sent in enumerate(doc.sents):
    #     print(sent, sent._.language)