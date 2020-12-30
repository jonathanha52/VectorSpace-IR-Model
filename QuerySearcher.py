import json
import os
import numpy
import math
class QuerySearcher:
    def __init__(self):
        self.index = {}
        self.retrived = []
        self.id = {}
        self.path = ''
    def open(self, path):
        '''
        path: directory of corpus
        '''
        self.path = path
        with open(os.path.join(path, 'index.json')) as f:
            self.index = json.load(f)
        with open(os.path.join(path, 'id.json')) as f:
            self.id = json.load(f)
    def search(self, query, distinctTerm):
        '''
        query: query parsed by query parser
        '''
        doclist = set()
        ranked = []
        print(distinctTerm)
        for q in distinctTerm:
            try:
                for doc in list(self.index['posting'][q].keys()):
                    doclist.add(doc)
            except:
                pass
        print(doclist)
        queryFeat = []
        for t in distinctTerm:
            try:
                tf = query.count(t)
                idf = 1 + math.log(self.index['doc count']/len(self.index['posting'][q]))
                queryFeat.append(tf*idf)
            except:
                queryFeat.append(0)
        print(queryFeat)
        for doc in doclist:
            featVector = []
            for q in distinctTerm:
                try:
                    tf = self.index['posting'][q][doc]
                    idf = 1 + math.log(self.index['doc count']/len(self.index['posting'][q]))
                    featVector.append(tf*idf)
                except:
                    featVector.append(0)
            score = self.__l2score(queryFeat, featVector)
            docName = os.path.splitext(self.id[doc])[0]
            ranked.append((docName, score))
            ranked.sort()
        return ranked
    def __l2score(self, a, b):
        return numpy.linalg.norm(a-b)
        
        