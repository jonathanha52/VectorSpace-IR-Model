from Preprocess import preprocess

class QueryParser:
    def __init__(self):
        self.processedQuery = ''
        self.processor = preprocess()
        self.distinctTerm = set()
    def parse(self, query, lemma = False, stem = False):
        #Simple takes the query and preprocess it
        #Can't explain it any simpler than that
        self.processedQuery = self.processor.process(query, lemma, stem)
        return self.processedQuery