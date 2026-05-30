import spacy as sa 
nlp = sa.load("en_core_web_sm")

print("Name of piplines ",nlp.pipe_names)

for name,components in nlp.pipeline:
    print(f"Name {name:<30} Components {components}")
