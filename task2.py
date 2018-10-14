def listToString(a):
    s = "["
    for el in a:
        s += str(el)+", "
    if len(a) != 0:
        s = s[:-2]
    return s + "]"


def addBorder(a):
    l = len(a[0])
    for i in range(len(a)):
        a[i] = "|" + a[i] + "|"
    b = "+"
    for i in range(l):
        b += "-"
    b += "+"
    return [b] + a + [b]


def shorting(e):
    s = ''
    e_new = []
    for word in e:
        if len(word) > 10:
            word = word[0] + str(len(word[1:-1])) + word[-1]
        e_new.append(word)
    return e_new


def competition(e, k):
    res = 0
    if e[k] != 0:
        res = k+1
        for i in range(k+1, len(e)):
            if e[i] == e[k]:
                res += 1
            else:
                break
    else:
        for i in range(k-1, -1, -1):
            if e[i] != 0:
                res = i+1
                break
    return res


def goodPairs(a, b):
    s = []
    for i in set(a):
        for j in set(b):
            if (i+j) != 0:
                if (i*j) % (i+j) == 0:
                    s.append(i**2 + j**2)
    return sorted(set(s))

print(goodPairs([16, 25, 45, 30], [30, 16, 34, 45, 30]))

def makeShell(n):
    res = []
    for i in range(n):
        res += [[0] * (i + 1)]
    for i in range(n - 1, 0, -1):
        res += [[0] * i]
    return res


if __name__ == "__main__":

    assert listToString([]) == "[]", "listToString error"
    assert listToString([1, 2, 3]) == "[1, 2, 3]", "listToString error"
    assert listToString([-5]) == "[-5]", "listToString error"
    print("listToString - OK")

    assert addBorder(['abc',
                      'def']) == ['+---+',
                                  '|abc|',
                                  '|def|',
                                  '+---+'], \
        "addBorder error"
    print("addBorder - OK")

    assert shorting(['word', 'localization', 'internationalization',
                     'pneumonoultramicroscopicsilicovolcanoconiosis']) == \
           ['word', 'l10n', 'i18n', 'p43s'], "shorting error"
    print("shorting - OK")

    assert competition([5, 4, 3, 2, 1], 2) == 3, \
        "competition error"
    assert competition([0, 0, 0, 0], 0) == 0, \
        "competition error"
    assert competition([10, 9, 8, 7, 7, 7, 5, 5], 4) == 6, \
        "competition error"
    assert competition([9, 7, 4, 1, 1], 3) == 5, \
        "competition error"
    print("competition - OK")

    assert goodPairs([4, 5, 6, 7, 8], [8, 9, 10, 11, 12]) == [128, 160, 180], \
        "goodPairs error"
    assert goodPairs([2], [2]) == [8], \
        "goodPairs error"
    assert goodPairs([7, 8, 9], [5, 3, 2]) == [], \
        "goodPairs error"
    print("goodPairs - OK")

    assert makeShell(1) == [[0]], "makeShell error"
    assert makeShell(2) == [[0], [0, 0], [0]], "makeShell error"
    assert makeShell(3) == [[0], [0, 0], [0, 0, 0], [0, 0], [0]], \
        "makeShell error"
    print("makeShell - OK")
