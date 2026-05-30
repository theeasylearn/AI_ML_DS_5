import spacy as sa 
from spacy.language import Language
from spacy.tokens import Doc 

nlp = sa.load('en_core_web_sm')

#add new property into doc object
Doc.set_extension("emails",default=False)

@Language.component("hasEmail")
def hasEmail(doc):
    text = doc.text.lower()
    if "@" in text:
        import re
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc.text)
        doc._.emails = emails 
    return doc 
    
nlp.add_pipe("hasEmail",last=True)

doc = nlp("Hello my name is ankit patel. previously we were talking about job offer. could you please send your resume on theeasylearn@gmail.com")

print(doc._.emails)
