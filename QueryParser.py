from Preprocess import preprocess

class QueryParser:
    def __init__(self, st = None):
        self.processedQuery = ''
        self.stopwords = st if st != None else st
        self.processor = preprocess(st)
        self.distinctTerm = set()
    def parse(self, query):
        self.processedQuery = self.processor.process(query)
        self.distinctTerm = set(self.processedQuery)
        return self.processedQuery, self.distinctTerm