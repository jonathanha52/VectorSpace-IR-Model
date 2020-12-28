def APScore(res, gt):
    retrived = len(res)
    sumP = 0
    Relevent = 0
    for i in retrived:
        if res[i] not in gt:
            continue
        Relevent += 1
        sumP += round(Relevent/i,2)
    AP = round(sumP/retrived,2)
    return AP

