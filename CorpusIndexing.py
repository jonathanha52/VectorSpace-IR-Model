import math
import numpy
import json
import os
from Preprocess import preprocess
class CorpusIndexing:
    def __init__(self):
        self.doc = {}
        self.index = {}
        self.docCount = 0
        self.norm = []
    def indexing(self, path):
        #From path, the class looks for processed.json file
        #and load into self.doc for indexing step
        #which is an output of the preprocessing step.
        #This will raise an exception if the preprocess step isn't done
        with open(os.path.join(path,'processed.json')) as f:
            self.doc = json.load(f)
        #From now on is the indexing part, including:
        #1. Creating posting list
        #2. Normalize

        #Creating posting list process
        #Each term is counted and multiply by idf of each term
        for idx in self.doc:
            self.docCount += 1
            for term in self.doc[idx]:
                if term not in self.index:
                    self.index[term] = {}
                    self.index[term]['posting'] = {}
                    self.index[term]['idf'] = 0
                if idx not in self.index[term]['posting']:
                    self.index[term]['posting'][idx] = 0
                self.index[term]['posting'][idx] += 1
        for term in self.index:
            self.index[term]['idf'] = math.log2(self.docCount / len(self.index[term]['posting']))
            for doc in self.index[term]['posting']:
                self.index[term]['posting'][doc] *= self.index[term]['idf']
        
        #Calculating norm for each document
        self.norm = [0]*self.docCount
        for i in range(self.docCount):
            for term in self.index:
                try:
                    self.norm[i] += self.index[term]['posting'][str(i)]**2
                except:
                    pass
            self.norm[i] = math.sqrt(self.norm[i])
        #Divide each tfidf weight for corresponding norm
        for i, n in enumerate(self.norm):
            for term in self.index:
                try:
                    self.index[term]['posting'][str(i)] = self.index[term]['posting'][str(i)]/n
                except:
                    pass
        
        #Export indexing
        with open(os.path.join(path,'index.json'), 'w+') as f:
            json.dump(self.index, f)
    
        