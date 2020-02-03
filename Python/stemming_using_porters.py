import nltk

from nltk.stem.porter import PorterStemmer

PORTER_STEMMER = PorterStemmer()
WORD_DATA = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"

# First we do word tokenization

NLTK_TOKENS = nltk.word_tokenize(WORD_DATA)

# Next find the roots of the word

for w in NLTK_TOKENS:
    print("Actual: %s\t\tStem: %s" % (w, PORTER_STEMMER.stem(w)))
