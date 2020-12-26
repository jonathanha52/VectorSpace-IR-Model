from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from string import punctuation
class preprocess():
    def __init__(self,
                st = sent_tokenize,
                wt = word_tokenize,
                sw = stopwords,
                stm = PorterStemmer
                ):
        self.sent_tokenize = st
        self.word_tokenize = wt
        self.stopwords = stopwords
        self.stemmer = stm
    def process(self, inp):
        tokenized = [x for x in word_tokenize(inp) if x not in punctuation or x not in self.stopwords]
        stemmed = [self.stemmer(x) for x in tokenized]
        return stemmed
