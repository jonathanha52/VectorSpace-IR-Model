import math
import numpy
import json
import os
from Preprocess import preprocess
class CorpusIndexing:
    def __init__(self):
        self.doc = {}
        self.index = {'doc count':0, 'term count':0,'posting':{}}
    def indexing(self, path):
        with open(os.path.join(path,'processed.json')) as f:
            self.doc = json.load(f)
        for idx in self.doc:
            self.index['doc count'] += 1
            for term in self.doc[idx]:
                if term not in self.index:
                    self.index['posting'][term] = {}
                    self.index['term count'] += 1
                if idx not in self.index['posting'][term]:
                    self.index['posting'][term][idx] = 0
                self.index['posting'][term][idx] += 1
        with open(os.path.join(path,'index.json'), 'w+') as f:
            json.dump(self.index, f)
    
        