from CorpusPreprocess import CorpusPreprocess
from CorpusIndexing import CorpusIndexing
from QueryParser import QueryParser
from QuerySearcher import QuerySearcher
import time
import os

#Wrapping modules into a single class for better interfacing
class VectorSpaceIR:
    def __init__(self):
        self.CP = CorpusPreprocess()
        self.CI = CorpusIndexing()
        self.QP = QueryParser()
        self.QS = QuerySearcher()
    def indexing(self, path, lemma = False, stem = False):
        #This method handle preprocessing a corpus and indexing it
        self.CP.preprocess(path, lemma, stem)
        self.CI.indexing(path)
    def openIndex(self, path):
        #Chooing location for indexing
        #This needs to be used before search step
        self.QS.open(path)
    def search(self, inp, stem = False, lemma = False):
        #Takes a string input, preprocess and perform search on designated location
        #from the openIndex method
        processedQuery = self.QP.parse(inp, stem, lemma)
        res = self.QS.search(processedQuery)
        return res
    