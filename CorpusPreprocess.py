
import os
import json
from nltk.corpus import stopwords
from Preprocess import preprocess

class CorpusPreprocess:
    def __init__(self):
        self.path = ''
        self.id = {}
        self.processed = {}
        self.listfile = []
    def preprocess(self, path, lemma = False, stem = False):
        self.path = path
        self.__idMapping()
        self.__process(lemma, stem)
    def __idMapping(self):
        #Assign distinct id for each document in the corpus
        self.listfile = os.listdir(self.path)
        if len(self.listfile) == 0:
            raise Exception(f'{self.path} is empty!')
        self.listfile.sort()
        current_docid = 0
        for f in self.listfile:
            name, ext = os.path.splitext(f)
            if ext == '.json':
                continue
            self.id[current_docid] = f
            self.id[f] = current_docid
            current_docid += 1
        tmp = os.path.join(self.path, 'id.json')
        with open(tmp,'w+') as f:
            json.dump(self.id, f)
            
    def __process(self, lemma = False, stem = False):
        processor = preprocess()
        for doc in self.listfile:
            name, ext = os.path.splitext(doc)
            if ext == '.json':
                continue
            with open(os.path.join(self.path,doc)) as f:
                content = f.read()
            processedContent = processor.process(content, lemma, stem)
            docId = int(self.id[doc])
            self.processed[docId] = processedContent
        with open(os.path.join(self.path, 'processed.json'), 'w+') as f:
            json.dump(self.processed, f)


            

