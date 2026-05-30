from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ['ran','running','swimming','swimmer','reading','playing','player','cricketing','cricketer','balling','baller']

for item in words:
    print(ps.stem(item))