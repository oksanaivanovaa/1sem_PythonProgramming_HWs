def unique(e):
    return sorted(set(e))


def transposeDict(d):
    d1 = {}
    for k in d.keys():
        d1[d[k]] = k
    return d1


def mex(e):
    res = len(e) + 1
    for x in range(1, len(e)+1):
        if x not in set(e):
            res = x
            break
    return res


def frequencyDict(s):
    d = {}
    for el in set(s):
       d[el] = list(s).count(el)
    return d
