from CorpusPreprocess import CorpusPreprocess
from CorpusIndexing import CorpusIndexing
from QueryParser import QueryParser
from QuerySearcher import QuerySearcher
import time
import os
#import matplotlib.pyplot as plt
from evaluation import APScore
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

if __name__ == '__main__':
    path =  'Cranfield'
    dirTest = os.path.join('TEST','query.txt')
    dirGoundtruth = os.path.join('TEST', 'RES')
    VSIr = VectorSpaceIR()
    
    start = time.time()
    VSIr.indexing(path, stem= True)
    end = time.time()
    indexingElapsed = end - start
    print(f'Indexing Elapsed Time: {indexingElapsed}')

    AP = []
    VSIr.openIndex(path)
    start = time.time()
    with open(dirTest) as f:
        for line in f.readlines():
            qID, query = line.split('\t')
            with open(os.path.join(dirGoundtruth, qID+'.txt')) as g:
                groundtruth = []
                for line in g.readlines():
                    groundtruth.append(line.split()[1])
            res = VSIr.search(query, stem = True)
            #print(res)
            if len(res) == 0:
                AP.append(0)
                continue
            AP.append(APScore([x[0] for x in res],groundtruth))
    end = time.time()
    retrievalElasped = end - start
    mAP = sum(AP)/len(AP)
    print(f'mAP score: {mAP}')
    print(f'Retrival elasped time: {retrievalElasped}')
    #plt.plot(AP)
    