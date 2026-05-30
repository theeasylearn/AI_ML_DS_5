import spacy as sa
from spacy.matcher import Matcher

text = "Apple is buying United Kingdom Based startup for $ 1.2 Billion in June 2026. Tim Cook is very positive about this deal. Elon musk belives it will increase sales of IPhone computer in Olympics 2028"

nlp = sa.load('en_core_web_sm')
doc = nlp(text)
matcher = Matcher(nlp.vocab)

pattern = [
    {'LOWER':'apple'},
    {'POS':'AUX','op':'*'},
    {'LEMMA':'buy'}
]

matcher.add('my_rules',[pattern])

matches = matcher(doc)

for match_id,start,end in matches:
    word = doc[start:end]
    print(f"{word} position {start} {end}")