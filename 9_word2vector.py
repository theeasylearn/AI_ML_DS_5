from gensim.models import Word2Vec
story = [
    ["In", "a", "deep", "green", "forest", "near", "the", "tall", "mountains", "many", "animals", "lived", "happily", "together"],
    ["A", "clear", "blue", "river", "flowed", "quietly", "through", "the", "forest", "every", "day"],
    ["Deer", "came", "to", "the", "river", "in", "the", "morning", "to", "drink", "fresh", "water"],
    ["Colorful", "birds", "sang", "sweet", "songs", "from", "the", "branches", "of", "big", "trees"],
    ["A", "clever", "fox", "and", "a", "friendly", "rabbit", "often", "played", "near", "the", "riverbank"],
    ["One", "rainy", "evening", "dark", "clouds", "covered", "the", "mountains", "and", "strong", "winds", "began", "to", "blow"],
    ["The", "river", "started", "rising", "quickly", "and", "the", "small", "animals", "became", "frightened"],
    ["The", "elephants", "worked", "together", "to", "help", "the", "animals", "cross", "to", "safe", "ground"],
    ["After", "the", "storm", "ended", "the", "birds", "flew", "over", "the", "forest", "and", "chirped", "happily", "again"],
    ["From", "that", "day", "all", "the", "animals", "understood", "that", "unity", "and", "kindness", "make", "everyone", "strong"]
]
print("Model training started.....")
model = Word2Vec(sentences=story,vector_size=100,min_count=1,sg=1,window=3,epochs=20)
print("Model training finished....")
list = model.wv.similar_by_word(word='animals',topn=5)
print(list)
list = model.wv.similar_by_word(word='river',topn=5)
print(list)
list = model.wv.similar_by_word(word='rabbit',topn=5)
print(list)
list = model.wv.most_similar(negative='river',topn=5)
print(list)


