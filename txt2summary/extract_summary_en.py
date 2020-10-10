# encoding: utf-8

# refrence: https://github.com/DerwenAI/pytextrank

import logging
import pytextrank
import spacy
import sys, os

# load a spaCy model, depending on language, scale, etc.

EXPERIMENT_DIR = '../experiment/chapter_0'
nlp = spacy.load("en_core_web_sm")
# nlp = spacy.load("es_core_news_sm")

# logging is optional: to debug, set the `logger` parameter
# when initializing the TextRank object

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger("PyTR")

# add PyTextRank into the spaCy pipeline

tr = pytextrank.TextRank(logger=None)
nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

# parse the document

with open("dat/mih.txt", "r") as f:
    text = f.read()

doc = nlp(text)

# examine the top-ranked phrases in the document

# for phrase in doc._.phrases:
#     print("{:.4f} {:5d}  {}".format(phrase.rank, phrase.count, phrase.text))
#     print(phrase.chunks)


# generate a GraphViz doc to visualize the lemma graph

tr.write_dot(path="lemma_graph.dot")

print("\n----\n")

# switch to a longer text document...
text_name = '-nGbufx6Ecc.en'
with open(os.path.join(EXPERIMENT_DIR, text_name + '.txt'), "r") as f:
    text = f.read()
    print(text)

doc = nlp(text)

with open(os.path.join(EXPERIMENT_DIR, text_name + '.keywords.txt'), 'w') as fout:
    for phrase in doc._.phrases[:20]:
        fout.writelines(str(phrase))
        fout.writelines('\n')
        print(phrase)

print("\n----\n")

# summarize the document based on the top 15 phrases,
# yielding the top 5 sentences...
with open(os.path.join(EXPERIMENT_DIR, text_name + '.summary.txt'), 'w') as fout:
    for sent in doc._.textrank.summary(limit_phrases=15, limit_sentences=5):
        fout.writelines(str(sent))
        fout.writelines('\n')
        print(sent)

print("\n----\n")
