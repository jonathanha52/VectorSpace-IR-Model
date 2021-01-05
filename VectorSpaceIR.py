from CorpusPreprocess import CorpusPreprocess
from CorpusIndexing import CorpusIndexing
from QueryParser import QueryParser
from QuerySearcher import QuerySearcher
import time
import os
class VectorSpaceIR:
    def __init__(self):
        self.CP = CorpusPreprocess()
        self.CI = CorpusIndexing()
        self.QP = QueryParser()
        self.QS = QuerySearcher()
    def indexing(self, path, lemma = False, stem = False):
        self.CP.preprocess(path, lemma, stem)
        self.CI.indexing(path)
    def openIndex(self, path):
        self.QS.open(path)
    def search(self, string, stem = False, lemma = False):
        processedQuery = self.QP.parse(string, stem, lemma)
        #print(processedQuery, distinctTerm)
        res = self.QS.search(processedQuery)
        return res
    #print(count)
    #plt.plot(AP)
    