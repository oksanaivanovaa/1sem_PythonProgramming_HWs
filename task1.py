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

if __name__ == "__main__":

    assert unique([1, 2, 1, 3]) == [1, 2, 3], "unique doesn't work"
    assert unique({5, 1, 3}) == [1, 3, 5], "unique doesn't work"
    assert unique('adsfasdf') == ['a', 'd', 'f', 's'], "unique doesn't work"
    print("unique func. - OK")

    assert transposeDict({}) == {}, "transposeDict doesn't work"
    assert transposeDict({1: 'a', 2: 'b'}) == {'a': 1, 'b': 2}, "transposeDict doesn't work"
    assert transposeDict({1: 1}) == {1: 1}, "transposeDict doesn't work"
    print("transposeDict func. - OK")

    assert mex([1, 2, 3]) == 4, "mex doesn't work"
    assert mex(['asdf', 123]) == 1, "mex doesn't work"
    assert mex([0, 0, 1, 0]) == 2, "mex doesn't work"
    print("mex func. - OK")

    assert frequencyDict('') == {}, "frequencyDict doesn't work"
    assert frequencyDict('abacaba') == {'a': 4, 'b': 2, 'c': 1}, "frequencyDict doesn't work"
    print("frequencyDict func. - OK")
