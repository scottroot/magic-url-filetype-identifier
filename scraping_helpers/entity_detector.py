import spacy

nlp = spacy.load("en_core_web_lg")
# doc = nlp("Apple is looking at buying UK startup for $1 billion")

def recognizeEntities(text, limit=10):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        # print(ent.text, ent.start_char, ent.end_char, ent.label_)
        if ent.text is not None:
            entities.append([ent.text, ent.label_])
        # print(ent.text, ent.label_)
    return entities[0:limit]

# print(recognizeEntities("Apple is looking at buying UK startup for $1 billion", limit=2))