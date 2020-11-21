import math
import numpy
import json
class TfidfVectorSpace:
    def __init__(self, docMap = None):
        self.idfVec = {}
        self.tfidfVec = {}
        self.docMap = {}
        self.countDoc = 0
        self.termMap = {}
        self.parseId(docMap)
    def fit(self, corpus):
        self.countDoc = len(corpus)
        for doc in corpus:
            temp = set(doc)
            for term in temp:
                self.termMap.add(term)
                if term not in self.idfVec:
                    self.idfVec[term] = 1
                else:
                    self.idfVec[term] += 1
        for doc in corpus:
            countTerm = len(doc)
            self.tfidfVec[docid] = []
            for key in self.termMap:
                self.tfidfVec[docid].append((doc.count(key)/countTerm) * (math.log(self.countDoc/(1+self.idfVec[key]),2)))
            docid += 1
    def parseId(self, docMap):
        if docMap != None:
            try:
                with open(docMap) as f:
                    self.docID = json.load(f)
            except:
                print(f"Can't open {docMap}")
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
        