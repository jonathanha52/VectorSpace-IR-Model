import json
import os
from numpy import dot
from numpy.linalg import norm
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
    def search(self, query):
        #query: query parsed by query parser
        queryWeight = {}
        doclist = set()
        ranked = []
        #Remove all term not existed in corpus
        filtered = list(filter(lambda x: x in self.index, query))
        distinctTerm = set(filtered)
        #Get relevent document
        for term in distinctTerm:
            #Get relevent doc
            for doc in list(self.index[term]['posting'].keys()):
                doclist.add(doc)
            #Term weighting
            queryWeight[term] = filtered.count(term) * self.index[term]['idf']
        #Term normalizing
        queryNorm = 0
        for term in queryWeight:
            queryNorm += queryWeight[term]**2
        queryNorm = math.sqrt(queryNorm)
        for term in queryWeight:
            queryWeight[term] /= queryNorm
        #Get ranked document
        for doc in doclist:
            score = 0
            for term in distinctTerm:
                try:
                    score += self.index[term]['posting'][doc] * queryWeight[term]
                except:
                    pass
            ranked.append((self.id[doc],score))
        ranked.sort(key = lambda x:x[1], reverse = True)
        return ranked
    def __cosine(self, a, b):
        return (dot(a)*dot(b))/(norm(a)*norm(b))
        
        