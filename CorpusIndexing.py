import math
import numpy
import json
import os
from Preprocess import preprocess
class CorpusIndexing:
    def __init__(self):
        self.doc = {}
        self.posting = {}
    def indexing(self, path):
        with open(os.path.join(path,'processed.json')) as f:
            self.doc = json.load(f)
        for idx in self.doc:
            for term in self.doc[idx]:
                if term not in self.posting:
                    self.posting[term] = {}
                if idx not in self.posting[term]:
                    self.posting[term][idx] = 0
                self.posting[term][idx] += 1
        with open(os.path.join(path,'posting.json'), 'w+') as f:
            json.dump(self.posting, f)
    
        