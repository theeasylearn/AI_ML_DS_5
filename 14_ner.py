import spacy as sa 

nlp = sa.load('en_core_web_sm')

text = "Apple is buying United Kingdom Based startup for $ 1.2 Billion in June 2026. Tim Cook is very positive about this deal. Elon musk belives it will increase sales of IPhone computer in Olympics 2028"

doc = nlp(text)

for entity in doc.ents:
    print(f"Text {entity.text:<25} Label {entity.label_:<30}")

