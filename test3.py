import time
import os
from VSSystem import VSSystem
from evaluation import APScore

STEM = True
LEMMA = False
STOP = False
'''
Testing created for testing indexing and querying using Snowball stemmer
'''
if __name__ == '__main__':
    path =  'Cranfield'
    dirTest = os.path.join('TEST','query.txt')
    dirGoundtruth = os.path.join('TEST', 'RES')
    VSIr = VSSystem()
    
    print('Stemming + Keeping stopword testing')
    start = time.time()
    VSIr.indexing(path, stem = STEM, lemma=LEMMA, st=STOP)
    end = time.time()
    indexingElapsed = end - start
    print(f'Indexing Elapsed Time: {indexingElapsed}')
    print('-----*-----')
    
    AP = []
    count = 0
    VSIr.openIndex(path)
    start = time.time()
    with open(dirTest) as f:
        for line in f.readlines():
            qID, query = line.split('\t')
            with open(os.path.join(dirGoundtruth, qID+'.txt')) as g:
                groundtruth = []
                for line in g.readlines():
                    groundtruth.append(line.split()[1])
            res = VSIr.search(query, stem = STEM, lemma=LEMMA, st=STOP)
            #print(res)
            if len(res) == 0:
                AP.append(0)
                count += 1
                continue
            AP.append(APScore([x[0] for x in res],groundtruth))
    end = time.time()
    retrievalElasped = end - start
    mAP = sum(AP)/len(AP)
    print(f'mAP score: {mAP}')
    print(f'Retrival elasped time: {retrievalElasped}')