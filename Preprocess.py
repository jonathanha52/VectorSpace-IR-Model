from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from string import punctuation
class preprocess():
    def __init__(self, st = None):
        self.word_tokenize = word_tokenize
        self.stemmer = PorterStemmer()
        self.stopwords = st if st != None else stopwords.words('english')
    def process(self, inp):
        tokenized = [x for x in word_tokenize(inp) if x not in punctuation and x not in self.stopwords]
        stemmed = [self.stemmer.stem(x) for x in tokenized]
        return stemmed
