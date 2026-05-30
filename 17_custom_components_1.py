import spacy as sa 
from spacy.language import Language
from spacy.tokens import Doc 

nlp = sa.load('en_core_web_sm')

#add new property into doc object
Doc.set_extension("courses",default=[])
courses = [
    "python",
    "data science",
    "machine learning",
    "web development",
    "cyber security",
]

@Language.component("course_finder")
def course_finder(doc):
    #empty list 
    found_courses = []
    text = doc.text.lower()
    for item in courses:
        if item in text:
            found_courses.append(item)
    
    doc._.courses = found_courses
    return doc 

nlp.add_pipe("course_finder",last=True)

doc = nlp("I am interested in learning few courses like python, data science, machine learning ")

print(doc._.courses)
