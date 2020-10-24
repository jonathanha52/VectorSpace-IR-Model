import math
import numpy
class TfidfVectorSpace:
    def __init__(self):
        self.idfVec = {}
        self.totalDoc = 0
        self.tfidfVec = {}
        self.countDoc = 0
        self.termSet = set()
    def fit(self, corpus):
        docid = 0
        self.countDoc = len(corpus)
        for doc in corpus:
            temp = set(doc)
            for term in temp:
                self.termSet.add(term)
                if term not in self.idfVec:
                    self.idfVec[term] = 1
                else:
                    self.idfVec[term] += 1
        for doc in corpus:
            countTerm = len(doc)
            self.tfidfVec[docid] = []
            for key in self.termSet:
                self.tfidfVec[docid].append((doc.count(key)/countTerm) * (math.log(self.countDoc/(1+self.idfVec[key]),2)))
            docid += 1
    def vectorize(self, doc):
        tfidfVec = []
        queryLength = len(doc)
        for key in self.termSet:
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
        