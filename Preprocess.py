from nltk import sent_tokenize, pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import SnowballStemmer, WordNetLemmatizer, PorterStemmer
from string import punctuation
class preprocess():
    def __init__(self):
        self.word_tokenize = word_tokenize
        self.stemmer = SnowballStemmer(language='english')
        self.lemmatizer = WordNetLemmatizer()
        self.stopwords = stopwords.words('english')
    def process(self, inp, stem = False, lemma = False, st = True):
        tokenized = [x for x in word_tokenize(inp) if x not in punctuation]
        #st is true then stopwords will be removed
        #added for testing
        if st:
            tokenized = [x for x in tokenized if x not in self.stopwords]
        #stem and lemma should be mutually exclusive, which 2 parameter should not have the same value
        if stem:
            return [self.stemmer.stem(x) for x in tokenized]
        if lemma:
            tagged = pos_tag(tokenized)
            return [self.lemmatizer.lemmatize(x[0], self.getPOSTag(x[1])) for x in tagged]
    
    #Get approriate tag for lemmatizer
    def getPOSTag(self, treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN