
import os
def APScore(res, gt):
    PrecisionatRecall = {}
    pInter = []
    retrivedCount = len(res)
    sumP = 0
    Relevent = 0
    for i in range(retrivedCount):
        name, ext = os.path.splitext(res[i])
        if name not in gt:
            continue
        Relevent += 1
        PrecisionatRecall[Relevent/len(gt)] = Relevent/(i+1)
    recall = 0.0
    while recall <= 1.0:
        pInter.append(getMaxP(recall, PrecisionatRecall))
        recall += 0.1
    return sum(pInter)/len(pInter)

def getMaxP(r, par):
    pMax = 0
    for i in par:
        if i >= r and par[i] > pMax:
            pMax = par[i]
    return pMax