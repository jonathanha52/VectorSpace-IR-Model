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
        self.corpusName = ''
        self.countDoc = 0
    def indexCorpus(self, dirToCorpus):
        try:
            self.__loadMapId(dirToCorpus)
        except Exception as e:
            print(e)
            try:
                self.__mapId(dirToCorpus)
            except Exception as e:
                print(e)
                return
        corpus = self.__processCorpus(dirToCorpus)
        self.__idfVectorize(corpus)
        for doc in corpus:
            countTerm = len(doc)
            docid = self.docMap[doc]
            self.tfidfVec[docid] = []
            for key in self.termMap:
                self.tfidfVec[docid].append((doc.count(key)/countTerm) * (math.log(self.countDoc/(1+self.idfVec[key]),2)))
            docid += 1
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
    def __mapId(self, dirToCorpus):
        try:
            listfile = os.listdir(dirToCorpus)
        except:
            print('Directory don\'t exist!')
            return
        if len(listfile) == 0:
            raise ValueError(f'{dirToCorpus} is empty!')
        current_docid = 0
        for f in listfile:
            self.docMap[current_docid] = f
            self.docMap[f] = current_docid
            current_docid += 1
        n = input(f'Do you want to write doc id mapping to {corpusName}.json? y/n')
        if n.lower() == 'y':
            with open(corpusId, 'w+') as f:
                json.dump(self.docMap, f)
    def __loadMapId(self, dirToCorpus):
        try:
            self.corpusName = os.path.split(dirToCorpus)[1]
            corpusIdFile =  os.path.join(os.path.split(dirToCorpus)[0],self.corpusName+'.json')
            with open(corpusId) as f:
                self.docMap = json.load(f)
        except:
            print('Existing id map not found!\nMapping new doc id')
    def __processCorpus(self, dirToCorpus):
        listfile = os.listdir(dirToCorpus)
        preprocessor = preprocess()
        processedDoc = []
        for f in listfile:
            with open(os.path.join(dirToCorpus, f)) as doc:
                docContent = doc.read()
            processedDoc.append(preprocessor.process(docContent))
        return processedDoc
    def __idfVectorize(self, corpus):
        for c in corpus:
            for term in c:
                if term not in self.idfVec:
                    self.idfVec[term] = 0
                self.idfVec[term] += 1
    def __cosineSimilarity(self, a, b):
        arrA = numpy.array(a)
        arrB = numpy.array(b)

        return numpy.dot(a, b) / (numpy.linalg.norm(a) - numpy.linalg.norm(b))
    
        