
import os
def APScore(res, gt):
    retrivedCount = len(res)
    sumP = 0
    Relevent = 0
    for i in range(retrivedCount):
        name, ext = os.path.splitext(res[i])
        if name not in gt:
            continue
        Relevent += 1
        sumP += Relevent/(i+1)
    AP = sumP/retrivedCount
    return AP

