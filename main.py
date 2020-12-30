from CorpusAnalyzer import CorpusAnalyzer
from CorpusIndexing import CorpusIndexing
from QueryParser import QueryParser
from QuerySearcher import QuerySearcher

class VectorSpaceIR:
    def __init__(self, stopwords = None):
        self.CA = CorpusAnalyzer(stopwords)
        self.CI = CorpusIndexing()
        self.QP = QueryParser(stopwords)
        self.QS = QuerySearcher()
    def indexWrite(self, path):
        self.CA.analyze(path)
        self.CI.indexing(path)
    def openIndex(self, path):
        self.QS.open(path)
    def search(self, string):
        processedQuery, distinctTerm = self.QP.parse(string)
        #print(processedQuery, distinctTerm)
        res = self.QS.search(processedQuery, distinctTerm)
        return res

if __name__ == '__main__':
    path =  'Cranfield'
    VSIr = VectorSpaceIR()
    #VSIr.indexWrite(path)
    VSIr.openIndex(path)
    doc = VSIr.search('experimental investigation')
    print(doc)