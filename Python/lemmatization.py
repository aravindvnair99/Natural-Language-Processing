import nltk

from nltk.stem import WordNetLemmatizer

w = WordNetLemmatizer()


def findpos(x):

    t = 'n'

    if x.startswith("V"):

        t = "v"

    elif x.startswith("J"):

        t = "a"

    elif x.startswith("R"):

        t = "r"

    elif x.startswith("N"):

        t = "n"

    return(t)


WORD_DATA = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"

# First Word tokenization

TOKENS = nltk.word_tokenize(WORD_DATA)

POS = nltk.pos_tag(TOKENS)

print("\nParts of speech are:\n\n", POS, "\n")

LEMMA = []

for i in range(len(POS)):

    x = findpos(POS[i][1])

    LEMMA.append(w.lemmatize(POS[i][0], x))

print(LEMMA)
