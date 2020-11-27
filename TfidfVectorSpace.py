import math
import numpy
import json
import os
from Preprocess import preprocess

class TfidfVectorSpace:
    def __init__(self):
        self.idfVec = {}
        self.tfidfVec = {}
        self.docMap = {}
        self.termMap = {}
        self.corpus_name = ''
        self.countDoc = 0

    def loadCorpus(self, dirToCorpus):
        self.__mapId(dirToCorpus)
        self.__processCorpus(dirToCorpus)
        
        listfile = os.listdir(dirToCorpus)
        self.countDoc = len(listfile)
        for doc in listfile:
            temp = set(doc)
            for term in temp:
                self.termMap.add(term)
                if term not in self.idfVec:
                    self.idfVec[term] = 1
                else:
                    self.idfVec[term] += 1
        for doc in corpus:
            countTerm = len(doc)
            docid = self.docMap[doc]
            self.tfidfVec[docid] = []
            for key in self.termMap:
                self.tfidfVec[docid].append((doc.count(key)/countTerm) * (math.log(self.countDoc/(1+self.idfVec[key]),2)))
            docid += 1

    def __mapId(self, dirToCorpus):
        try:
            corpus_name = os.path.split(dirToCorpus)[1] + '.json'
            corpusId =  os.getcwd() + os.path.split(dirToCorpus)[1] + '.json'
            with open(corpus_name) as f:
                self.docMap = json.load(f)
        except:
            print('Existing id map not found!\nMapping new doc id')
        try:
            listfile = os.listdir(dirToCorpus)
        except:
            print('Directory not exist!')
        if len(listfile) == 0:
            print('Empty corpus!')
            return
        current_docid = 0
        for f in listfile:
            self.docMap[current_docid] = f
            self.docMap[f] = current_docid
            current_docid += 1
        n = input(f'Do you want to write doc id mapping to {corpus_name}.json? y/n')
        if n.lower() == 'y':
            with open(corpusId, 'w+') as f:
                json.dump(self.docMap, f)
    def __processCorpus(self, dirToCorpus):
        for 
    
    def vectorize(self, doc):
        tfidfVec = []
        queryLength = len(doc)
        for key in self.termMap:
            tfidfVec.append((doc.count(key)/queryLength)* (math.log(1/(1+self.idfVec[key]),2)))
        return tfidfVec
    def ranking(self, vectorized, top=10, dec=3):
        ranked = []
        a = numpy.array(vectorized)
        for doc in self.tfidfVec:
            b = numpy.array(self.tfidfVec[doc])
            score = round(numpy.linalg.norm(a-b),dec)
            ranked.append((score,doc))
        ranked.sort(key = lambda x:x[0])
        return ranked[0:top]
        