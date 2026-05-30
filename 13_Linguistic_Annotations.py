import spacy as sa 

nlp = sa.load('en_core_web_sm')

paragraph = """The Indian Premier League is a famous cricket tournament played in the Twenty20 format. It features top Indian and international players representing different city-based teams. IPL is loved for its exciting matches, entertainment, and huge fan following across the world."""

doc = nlp(paragraph)
print(f"{'text':<12} {'leema':<12} {'pos':<12} {'Fine position':<12} {'Dependency':<12} {'Entity':<12} {'is_stop':<8}")
print("_"*100)
for token in doc:
    print(f"{token.text:<12} {token.lemma_:<12} {token.pos_:<12} {token.tag_:<12} {token.dep_:<12} {token.ent_type:<12} {token.is_stop}")
