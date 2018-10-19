def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def recurrent(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n % 2 == 0:
            return recurrent(n/2)
        else:
            return recurrent((n-1)/2)+recurrent((n+1)/2)


def digitsum(n, res=0):
    if n//10 == 0:
        if n == 0:
            return 0
        else:
            return res+n
    else:
        return digitsum(n//10, res+(n % 10))


def reversestring(s, i=0):
    if i >= len(s)-1:
        return s
    else:
        s = s[:i] + s[-1] + s[i:-1]
        return reversestring(s, i+1)


def ackermann(m, n):
    if m == 0:
        return n+1
    elif n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))


def genbinarystrings(n):

    def gen(n, pref=''):
        if len(pref) == n:
            yield pref
        else:
            for i in ['0', '1']:
                yield from gen(n, pref + i)

    return list(gen(n))


def istwopower(n):
    if n < 1:
        return False
    elif n == 1:
        return True
    elif n % 2 == 0:
        if n/2 == 1:
            return True
        else:
            return istwopower(n/2)
    else:
        return False


def concatnumbers(a, b):

    def sumdidits(b, i=0):
        if b//10 == 0:
            return i+1
        else:
            return sumdidits(b//10, i+1)

    return 10**sumdidits(b)*a+b


def abacaba(n):
    if n == 1:
        return [1]
    else:
        return abacaba(n-1)+[n]+abacaba(n-1)


def parentheses(s):
    if len(s) == 1 or len(s) == 2:
        return '('+s+')'
    else:
        return '('+s[0]+parentheses(s[1:-1])+s[-1]+')'


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    assert factorial(0) == 1
    assert factorial(2) == 2
    assert factorial(4) == 24
    print("factorial - OK")

    assert fibonacci(1) == 1
    assert fibonacci(4) == 3
    assert fibonacci(10) == 55
    print("fibonacci - OK")

    assert recurrent(2) == 1
    assert recurrent(3) == 2
    assert recurrent(5) == 3
    assert recurrent(7) == 3
    print("recurrent - OK")

    assert digitsum(0) == 0
    assert digitsum(123) == 6
    assert digitsum(192837465) == 45
    print("digitsum - OK")

    assert reversestring('') == ''
    assert reversestring('1') == '1'
    assert reversestring('asdf') == 'fdsa'
    assert reversestring('abacaba') == 'abacaba'
    print("reversestring - OK")

    assert ackermann(0, 10) == 11
    assert ackermann(1, 1) == 3
    assert ackermann(2, 2) == 7
    assert ackermann(2, 5) == 13
    assert ackermann(3, 3) == 61
    print("ackermann - OK")

    assert genbinarystrings(0) == ['']
    assert genbinarystrings(1) == ['0', '1']
    assert genbinarystrings(2) == ['00', '01', '10', '11']
    assert genbinarystrings(3) == ['000', '001', '010', '011',
                                   '100', '101', '110', '111']
    print("genbinarystrings - OK")

    assert istwopower(-5) is False
    assert istwopower(0) is False
    assert istwopower(1) is True
    assert istwopower(2) is True
    assert istwopower(4) is True
    assert istwopower(67) is False
    assert istwopower(1024) is True
    print("istwopower - OK")

    assert concatnumbers(1, 2) == 12
    assert concatnumbers(55, 88) == 5588
    assert concatnumbers(123, 789) == 123789
    assert concatnumbers(1000, 2) == 10002
    print("concatnumbers - OK")

    assert abacaba(1) == [1]
    assert abacaba(2) == [1, 2, 1]
    assert abacaba(3) == [1, 2, 1, 3, 1, 2, 1]
    assert abacaba(4) == [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1]
    print("abacaba - OK")

    assert parentheses('example') == '(e(x(a(m)p)l)e)'
    assert parentheses('odd') == '(o(d)d)'
    assert parentheses('even') == '(e(ve)n)'
    print("parentheses - OK")

    assert gcd(1, 5) == 1
    assert gcd(4, 6) == 2
    assert gcd(18, 12) == 6
    assert gcd(283918822, 595730520) == 22
    print("gcd - OK")
