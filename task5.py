def permutations(n):

    def gen_n(n, pref=[]):
        if len(pref) == n:
            return [tuple(pref)]
        else:
            s = set(pref)
            answ = []
            for i in range(1, n + 1):
                if i not in s:
                    answ += gen_n(n, pref+[i])
            return answ

    return gen_n(n)


def correctbracketsequences(n):

    def gen_n(n, pref='', bal=0):
        if len(pref) == 2 * n and bal == 0:
            yield pref
        else:
            for i in (1, -1):
                new_bal = bal + i
                if i == 1:
                    new_pref = pref + '('
                else:
                    new_pref = pref + ')'
                if (len(new_pref) <= 2 * n) and (new_bal >= 0) and \
                        (new_bal <= n):
                    yield from gen_n(n, new_pref, new_bal)

    return list(gen_n(n))


def combinationswithrepeats(n, k):

    def gen_comb(n, k, pref=[]):
        if len(pref) == k:
            yield tuple(pref)
        else:
            for i in range(1, n + 1):
                if len(pref) > 0:
                    if pref[-1] <= i:
                        yield from gen_comb(n, k, pref + [i])
                else:
                    yield from gen_comb(n, k, pref + [i])

    return(list(gen_comb(n, k)))


def unorderedpartitions(n):

    def gen_par(n, pref=[]):
        if sum(pref) == n:
            yield tuple(pref)
        else:
            if len(pref) > 0:
                en = pref[-1]
            else:
                en = 1
            for i in range(en, n-en+2):
                if sum(pref)+i <= n:
                    yield from gen_par(n, pref + [i])

    return list(gen_par(n))


if __name__ == "__main__":
    assert permutations(1) == [(1,)]
    assert permutations(2) == [(1, 2), (2, 1)]
    assert permutations(3) == [(1, 2, 3), (1, 3, 2), (2, 1, 3),
                               (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    print("permutations - OK")

    assert correctbracketsequences(1) == ['()']
    assert correctbracketsequences(2) == ['(())', '()()']
    assert correctbracketsequences(3) == ['((()))', '(()())', '(())()',
                                          '()(())', '()()()']
    print("correctbracketsequences - OK")

    assert combinationswithrepeats(1, 1) == [(1,)]
    assert combinationswithrepeats(2, 2) == [(1, 1), (1, 2), (2, 2)]
    assert combinationswithrepeats(3, 2) == [(1, 1), (1, 2), (1, 3), (2, 2),
                                             (2, 3), (3, 3)]
    print("combinationswithrepeats - OK")

    assert unorderedpartitions(1) == [(1,)]
    assert unorderedpartitions(3) == [(1, 1, 1), (1, 2), (3,)]
    assert unorderedpartitions(5) == [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 3),
                                      (1, 2, 2), (1, 4), (2, 3), (5,)]
    print("unorderedpartitions - OK")
