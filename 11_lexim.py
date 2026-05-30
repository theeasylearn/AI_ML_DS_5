import spacy as sa 

nlp = sa.load('en_core_web_sm')

paragraph = """The Indian Premier League, popularly known as IPL, is one of the biggest and most exciting cricket tournaments in the world. It was started in 2008 by the Board of Control for Cricket in India. The league follows the Twenty20 format, where teams play fast-paced matches filled with action and entertainment. Many famous international and Indian cricketers participate in the tournament. Teams represent different Indian cities and compete for the championship trophy. IPL is loved for its thrilling matches, huge fan following, cheerleaders, music, and grand opening ceremonies. It has also helped young players showcase their talent and build successful cricket careers."""
doc = nlp(paragraph)

lexim = doc[0]

for word in doc:
    print(f"{word.text:<20} {word.lower_:<20} {word.is_stop:<10} {word.is_oov:<10}")
