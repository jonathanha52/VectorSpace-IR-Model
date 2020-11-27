from TfidfVectorSpace import TfidfVectorSpace
import os
import json

#Helper function
def printlist(arg):
    print('{:<12}{:<12}'.format('Score', 'Doc ID'))
    for i in arg:
        print('{:<12}{:<12}'.format(i[0],i[1]))

#Data structure
root = os.getcwd()
print(f'Working at: {root}')
corpus_dir = 'Cranfield'
corpus = []
docid_map = {}
stoplist = stopwords.words('english')
ps = PorterStemmer()
corpus_list = {}
listfile = os.listdir(os.path.join(root,corpus_dir))

#Corpus processing
vectorSpace = TfidfVectorSpace(mapping_dir)
print('Processing corpus...')
for f in listfile:
    #print(f'Processing {f}')
    with open(os.path.join(root,corpus_dir,f)) as doc:
        doc_content = doc.read()
        if len(doc_content) != 0:
            sents = sent_tokenize(doc_content)
            words = []
            for s in sents:
                words = words + word_tokenize(s)
            tokenized = [item for item in words if item not in stoplist]
            stemmed = [ps.stem(item) for item in tokenized]
            corpus_list[f] = stemmed 
print('Done.')
print('Building vector space...')
vectorSpace.fit(corpus_list)
print('Done.')

#Query processing
inputQuery = input('Enter query string: ')
inputToken = word_tokenize(inputQuery)
inputToken = [item for item in inputToken if item not in stoplist]
inputStemmed = [ps.stem(item) for item in inputToken]
vectorizedInput = vectorSpace.vectorize(inputStemmed)
rank = vectorSpace.ranking(vectorizedInput)
printlist(rank)
#print(vectorizedInput)
#print(inputStemmed)

