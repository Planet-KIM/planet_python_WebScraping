from nltk import Text
from nltk import word_tokenize

from nltk.book import text6
from nltk import FreqDist

fdist = FreqDist(text6)
fdist.most_common(10)

#tokens = word_tokenize('Here is some not very interesting text')
#text = Text(tokens)