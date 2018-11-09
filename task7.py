from functools import reduce
import math


def valuesunion(*dicts):
    s = set()
    for dict in dicts:
        s.update(set(dict.values()))
    return s


def popcount(n):
    return bin(n).count('1')


def powers(n, m):
    return {i: (i ** i) % m for i in range(1, n+1)}


def isIPv4(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


def fibonacci(n):
    return list(reduce(lambda x, n: [x[1], x[0]+x[1]], range(n), [0, 1]))[0]


def pascals():

    for count in itertools.count(0):
        line = []
        for element in range(count + 1):
            line.append(int((math.factorial(count)) /
                            ((math.factorial(element)) *
                             math.factorial(count - element))))
        yield tuple(line)
