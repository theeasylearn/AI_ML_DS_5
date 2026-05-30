import spacy
from spacy.tokens import DocBin
import json

# Use pre-trained English model as base (much better)
nlp = spacy.load("en_core_web_sm")

doc_bin = DocBin()

with open("training_data.json", "r") as f:
    data = json.load(f)

for example in data:
    text = example["text"]
    entities = example["entities"]
    
    doc = nlp.make_doc(text)
    spans = []
    
    for start, end, label in entities:
        span = doc.char_span(start, end, label=label)
        if span is not None:
            spans.append(span)
        else:
            print(f"Warning: Bad span → {text[start:end]}")
    
    doc.ents = spans
    doc_bin.add(doc)

doc_bin.to_disk("train.spacy")
doc_bin.to_disk("dev.spacy")

print("Data converted successfully using en_core_web_sm")