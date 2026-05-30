import spacy

# Load YOUR trained model
nlp = spacy.load("./output/model-best")

# Test sentences (new, never seen during training)
test_sentences = [
    "Enroll in our JavaScript and TypeScript course now.",
    "The SQL Fundamentals class starts next Monday.",
    "We teach Flutter, Dart and Firebase development.",
]

for text in test_sentences:
    doc = nlp(text)

    print(f"\nText: {text}")

    if doc.ents:
        for ent in doc.ents:
            print(f"Found: '{ent.text}' → Label: {ent.label_}")
    else:
        print("No entities found")

