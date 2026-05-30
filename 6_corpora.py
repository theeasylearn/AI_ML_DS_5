import nltk 

corpora = ['gutenberg'] #source for NLTK
nltk.download(corpora)
from nltk.corpus import gutenberg
print(gutenberg.fileids())
book_1 = gutenberg.words('austen-emma.txt')
print(len(book_1))
print(book_1[:50]) 

book_2 = gutenberg.words('shakespeare-hamlet.txt')
print(len(book_2))
print(book_1[100:150]) 
