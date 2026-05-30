import nltk
from nltk.tokenize import word_tokenize

paragraph = "the quick brown fox jump over the lazy dog"
words = word_tokenize(paragraph)
print(nltk.pos_tag(words))