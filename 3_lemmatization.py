from nltk.stem import WordNetLemmatizer

lem = WordNetLemmatizer()

print(lem.lemmatize('better',pos='a'))
print(lem.lemmatize('weakest',pos='a'))
print(lem.lemmatize('nearer',pos='a'))
print(lem.lemmatize('running',pos='v'))