import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from collections import Counter
from string import punctuation
from heapq import nlargest

def topWords(text, length=5):

    nlp = spacy.load("en_core_web_lg")
    stopwords = list(STOP_WORDS)
    punc = list(punctuation) + ['\n']
    pos_tag = ['PROPN', 'VERB'] # 'ADJ', 'NOUN',
    text = text.replace("\n", " ")
    doc = nlp(text)
    tokens=[token.text for token in doc]

    word_frequencies={}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punc and word.pos_ in pos_tag:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1
    # print(word_frequencies)

    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency
    return list(word_frequencies.keys())[0:length]
    #
    # sentence_tokens = [sent for sent in doc.sents]

    # sentence_scores = {}
    # for sent in sentence_tokens:
    #     for word in sent:
    #         if word.text.lower() in word_frequencies.keys():
    #             if sent not in sentence_scores.keys():
    #                 sentence_scores[sent] = word_frequencies[word.text.lower()]
    #             else:
    #                 sentence_scores[sent] += word_frequencies[word.text.lower()]
    # # print(sentence_scores)

    # select_length = round(len(sentence_tokens) * length)
    # summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    # # print(len(sentence_tokens)*0.3)

    # final_summary = [word.text for word in summary]
    # summary = ''.join(final_summary)
    # return summary

# print(topWords("""This is just one of the ways to get text summarization by use of most frequently used words and then calculating most important sentences.
# There can be various other ways like use of library nltk to do it by using lexical analysis, part of speech tagger and n-grams. We will talk more about it in my next blog.
# """))