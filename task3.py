import itertools
from functools import reduce


def squares(a):
    for it in a:
        yield int(it) ** 2


def repeatntimes(elems, n):
    for i in range(n):
        yield from elems


def evens(x):
    if x % 2 == 1:
        x += 1
    while True:
        yield x
        x += 2


def digitsumdiv(p):
    for it in itertools.count(p):
        k = 0
        it1 = it
        while it1 > 0:
            k += it1 % 10
            it1 = it1 // 10
        if k % p == 0:
            yield it


def extractnumbers(s):
    return filter(lambda c: c.isdigit(), s)


def changecase(s):
    return map(lambda x: x.swapcase() if x.isalpha() else x, s)


def productif(elems, conds):
    return reduce(lambda x, y: x * y,
                  map(lambda x: x[0] if x[1] else 1, zip(elems, conds)), 1)


if __name__ == "__main__":
    it = digitsumdiv(5)
    for i in range(6):
        print(next(it))

    print(list(repeatntimes(list(squares([1,2,3])),2)))
    print(list(repeatntimes(squares([1, 2, 3]), 2)))
    print(next(squares([1, 2, 3])))
