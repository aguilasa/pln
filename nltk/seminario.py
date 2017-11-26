import nltk
from nltk.corpus import treebank

texto = 'Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.'
frases = texto.split('.')
print(frases)
frases = nltk.tokenize.sent_tokenize(texto)
print(frases)
tokens = nltk.word_tokenize(texto)
print(tokens)
classes = nltk.pos_tag(tokens)
print(classes)
entidades = nltk.chunk.ne_chunk(classes)
print(entidades)

t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()