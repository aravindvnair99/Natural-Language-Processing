import nltk

from nltk.stem import WordNetLemmatizer

W = WordNetLemmatizer()


def findpos(pos):
	"""Find parts of speech"""
    starts_with = 'n'

    if pos.startswith("V"):

        starts_with = "v"

    elif pos.startswith("J"):

        starts_with = "a"

    elif pos.startswith("R"):

        starts_with = "r"

    elif pos.startswith("N"):

        starts_with = "n"

    return starts_with


WORD_DATA = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"

# First do word tokenization

TOKENS = nltk.word_tokenize(WORD_DATA)

POS = nltk.pos_tag(TOKENS)

print("\nParts of speech are:\n\n", POS, "\n")

LEMMA = []

for i in enumerate(POS):

    x = findpos(POS[i][1])

    LEMMA.append(W.lemmatize(POS[i][0], x))

print(LEMMA)
