import spacy as sa 

nlp = sa.load('en_core_web_sm')

paragraph = """The Indian Premier League is a famous cricket tournament played in the Twenty20 format. It features top Indian and international players representing different city-based teams. IPL is loved for its exciting matches, entertainment, and huge fan following across the world."""

doc = nlp(paragraph)

for line in doc.sents:
    print(line.text)
