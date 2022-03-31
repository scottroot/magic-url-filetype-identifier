import spacy
# python -m spacy download en_core_web_sm

def get_entities(page_text, limit=25):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(str(page_text)[0:min(len(page_text), 1500)])
    ents = dict()
    ent_label = list()
    ent_text = list()
    for ent in doc.ents:
        print(ent.label_)
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

print(get_entities("Apple is looking at buying UK startup for $1 billion", limit=10))

