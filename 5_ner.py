import nltk
from nltk.tokenize import word_tokenize

paragraph = "Apple was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne in the garage of Jobs childhood home in Los Altos, California"
words = word_tokenize(paragraph)
tags = nltk.pos_tag(words)
print(nltk.ne_chunk(tags))