import nltk
nltk.download('punkt_tab')
paragraph = """Once upon a time, a little boy named Tim found an old lantern in his grandfather's attic.  When he lit it, a friendly ghost appeared and whispered, "Let's go on an adventure!"  They flew over sleeping rooftops and glowing rivers under the moonlight.  The ghost showed Tim the secret wonders hidden in everyday things.  By dawn, Tim returned home with a heart full of magic and a new best friend."""
from nltk.tokenize import word_tokenize,sent_tokenize

lines = sent_tokenize(paragraph)
print(lines)

words = word_tokenize(paragraph)
print(words)


