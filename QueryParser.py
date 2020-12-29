from Preprocess import preprocess

class QueryParser:
    def __init__(self, st = None):
        self.processedQuery = ''
        self.stopwords = st if st != None else 
        self.processor = preprocess(st)
    def parse(self, query):
        self.processedQuery = self.processor(query)
        tfidfVect = []
        return self.processedQuery