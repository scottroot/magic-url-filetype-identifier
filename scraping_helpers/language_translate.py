# pip install googletrans==3.1.0a0
from googletrans import Translator

def translateLanguage(text, src="auto", dest='en'):
	translator = Translator()
	translation = translator.translate(text, src=src, dest=dest)
	return {"text_origin":translation.src, "text_english":translation.text}

# print(translateLanguage("hola mi amigo"))
