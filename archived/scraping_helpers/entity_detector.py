import spacy
# python -m spacy download en_core_web_sm

def recognizeEntities(text, limit=10):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        if ent.text is not None:
            entities.append([ent.text, ent.label_])
    return entities[0:limit]

# print(recognizeEntities("Apple is looking at buying UK startup for $1 billion", limit=2))