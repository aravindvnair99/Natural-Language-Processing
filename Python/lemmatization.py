import nltk

from nltk.stem import WordNetLemmatizer

W = WordNetLemmatizer()


def findpos(POS):

    STARTS_WITH = 'n'

    if POS.startswith("V"):

        STARTS_WITH = "v"

    elif POS.startswith("J"):

        STARTS_WITH = "a"

    elif POS.startswith("R"):

        STARTS_WITH = "r"

    elif POS.startswith("N"):

        STARTS_WITH = "n"

    return(STARTS_WITH)


WORD_DATA = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"

# First do word tokenization

TOKENS = nltk.word_tokenize(WORD_DATA)

POS = nltk.pos_tag(TOKENS)

print("\nParts of speech are:\n\n", POS, "\n")

LEMMA = []

for i in range(len(POS)):

    x = findpos(POS[i][1])

    LEMMA.append(W.lemmatize(POS[i][0], x))

print(LEMMA)
