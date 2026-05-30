import spacy
from pathlib import Path

# Try multiple possible locations
model_path = Path("my_course_extractor")

if not model_path.exists():
    model_path = Path("./output/model-best")

if not model_path.exists():
    raise FileNotFoundError("Model not found. Please run training first!")

nlp = spacy.load(str(model_path))

print(f"Model loaded successfully from: {model_path}\n")

def extract_courses(text):
    doc = nlp(text)
    courses = [ent.text for ent in doc.ents if ent.label_ == "COURSE"]
    return courses


# Test
texts = [
    "Learn Python, Data Science and Web Development at The Easylearn Academy.",
    "Our new DevOps and Kubernetes bootcamp is now enrolling.",
    "I want to learn JavaScript and React.",
    "No courses mentioned here."
]

for text in texts:
    courses = extract_courses(text)
    print(f"Text: {text}")
    print(f"Courses: {courses}\n")