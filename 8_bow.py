from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
documents = [
    "The cat sat on the mat",
    "The dog sat on the log",
    "The cat chased the mouse",
    "The dog chased the cat"
]
bag_of_words = cv.fit_transform(documents)
print(cv.vocabulary_)
print(bag_of_words.toarray())
