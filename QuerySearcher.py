import json
import os
class QuerySearcher:
    def __init__(self):
        self.posting = {}
        self.retrived = []
    def open(self, path):
        '''
        path: directory of corpus
        '''
        with open(os.path.join(path, 'index.json')) as f:
            self.posting = json.load(f)
    def search(self, path, query):
        '''
        query: query parsed by query parser
        '''
        doclist = set()
        ranked = []
        for q in query:
            try:
                doclist.add(self.posting['posting'][q])
            except:
                pass
        
        