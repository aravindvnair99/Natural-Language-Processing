import nltk

from nltk.stem.porter import PorterStemmer

PORTER_stemmer = PorterStemmer()
WORD_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"

# First we do word tokenization

NLTK_tokens = nltk.word_tokenize(word_data)

# Next find the roots of the word

for w in nltk_tokens:
    print("Actual: %s\t\tStem: %s" % (w, PORTER_stemmer.stem(w)))
