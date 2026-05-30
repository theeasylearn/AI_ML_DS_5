import nltk 

corpora = ['brown'] #source for NLTK
nltk.download(corpora)
from nltk.corpus import brown
print(brown.categories())

hobbies = brown.words(categories='hobbies')
print(len(hobbies))
print(hobbies[:100])
print(brown.tagged_words()[:50])
