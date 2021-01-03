from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from string import punctuation
class preprocess():
    def __init__(self):
        self.word_tokenize = word_tokenize
        self.stemmer = SnowballStemmer(language='english')
        self.lemmatizer = WordNetLemmatizer()
        self.stopwords = stopwords.words('english')
    def process(self, inp, stem = False, lemma = False):
        tokenized = [x for x in word_tokenize(inp) if x not in punctuation and x not in self.stopwords]
        if stem:
            return [self.stemmer.stem(x) for x in tokenized]
        if lemma:
            return [self.lemmatizer.lemmatize(x) for x in tokenized]
