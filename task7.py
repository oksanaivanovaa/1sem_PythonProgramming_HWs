from functools import reduce
import math
import itertools


def valuesunion(*dicts):
    s = set()
    for dict in dicts:
        s.update(set(dict.values()))
    return s


def popcount(n):
    return bin(n).count('1')


def powers(n, m):
    return {i: (i ** i) % m for i in range(1, n+1)}


def subpalindrome(s):
    pal = s[0]
    for i in range(len(s)-1):
        for j in range(len(s)-1, i, -1):
            if s[i] == s[j]:
                boool = True
                for k in range(1, (j-i+1)//2):
                    if s[i+k] != s[j-k]:
                        boool = False
                        break
                if boool:
                    if len(pal) < len(s[i:j+1]):
                        pal = s[i:j+1]
    return pal


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


def pascals():

    def pas():
        for count in itertools.count(0):
            line = []
            for element in range(count + 1):
                line.append(int((math.factorial(count)) //
                                ((math.factorial(element)) *
                                math.factorial(count - element))))
            yield tuple(line)

    return list(pas())


def fibonacci(n):
    return list(reduce(lambda x, n: [x[1], x[0]+x[1]], range(n), [0, 1]))[0]


def brackets2(n, m):

    def gen_n(n, m, pref='', bal1=0, bal2=0, count1=0, count2=0, sum_bal=0):

        def norm(pref):
            stack = []
            for el in pref:
                if not stack:
                    stack.append(el)
                else:
                    if stack[-1] == '(':
                        if el == ')':
                            stack.pop()
                        else:
                            stack.append(el)
                    elif stack[-1] == '[':
                        if el == ']':
                            stack.pop()
                        else:
                            stack.append(el)
                    else:
                        stack.append(el)
            return False if stack else True

        if len(pref) == 2 * n + 2*m and bal1 == bal2 == 0 \
                and count1 == n and count2 == m and norm(pref):
            yield pref
        else:
            for i in ('(', ')', '[', ']'):
                new_bal1 = bal1
                new_bal2 = bal2
                new_count1 = count1
                new_count2 = count2
                if len(pref) >= n + m:
                    new_sum_bal = sum_bal - (new_bal1 - new_bal2)
                else:
                    new_sum_bal = n+m
                if i == '(':
                    new_pref = pref + i
                    new_bal1 = bal1 + 1
                    new_count1 += 1
                elif i == ')':
                    new_pref = pref + i
                    new_bal1 = bal1 - 1
                elif i == '[':
                    new_pref = pref + i
                    new_bal2 = bal2 + 1
                    new_count2 += 1
                else:
                    new_pref = pref + i
                    new_bal2 = bal2 - 1
                if (len(new_pref) <= 2 * n + 2 * m) and (new_bal1 >= 0)\
                        and (new_bal1 <= n) and (new_bal2 <= m) and\
                        (new_bal2 >= 0):
                    yield from gen_n(n, m, new_pref, new_bal1,
                                     new_bal2, new_count1,
                                     new_count2, new_sum_bal)

    return list(gen_n(n, m))


if __name__ == "__main__":
    assert valuesunion({1: 2, 4: 8}) == {2, 8}
    assert valuesunion({1: 2}, {4: 8}) == {2, 8}
    assert valuesunion({1: 2, 4: 8}, {'a': 'b'}, {}, {}) == {2, 8, 'b'}
    print("valuesunion - OK")

    assert popcount(0) == 0
    assert popcount(1) == 1
    assert popcount(10) == 2
    assert popcount(1023) == 10
    print("popcount - OK")

    assert powers(3, 1000000000) == {1: 1, 2: 4, 3: 27}
    assert powers(4, 50) == {1: 1, 2: 4, 3: 27, 4: 6}
    assert powers(1, 1) == {1: 0}
    print("powers - OK")

    assert subpalindrome('abc') == 'a'
    assert subpalindrome('aaaa') == 'aaaa'
    assert subpalindrome('abaxfgf') == 'aba'
    assert subpalindrome('abacabad') == 'abacaba'
    print("subpalindrome - OK")

    assert isIPv4('192.168.0.15')
    assert isIPv4('255.255.255.255')
    assert not isIPv4('555.555.555.555')
    assert not isIPv4('190+2.168.0.0')
    assert not isIPv4('abacaba')
    assert not isIPv4('')
    print('isIPv4 - OK')

    print("pascals - OK")

    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    print("fibonacci - OK")

    assert list(brackets2(1, 0)) == ['()']
    assert list(brackets2(0, 1)) == ['[]']
    assert list(brackets2(1, 1)) == ['()[]', '([])', '[()]', '[]()']
    assert list(brackets2(3, 0)) == ['((()))', '(()())', '(())()', '()(())',
                                     '()()()']
    assert list(brackets2(2, 1)) == ['(())[]', '(()[])', '(([]))', '()()[]',
                                     '()([])', '()[()]', '()[]()', '([()])',
                                     '([]())', '([])()', '[(())]', '[()()]',
                                     '[()]()', '[](())', '[]()()']
    print("brackets2 - OK")
