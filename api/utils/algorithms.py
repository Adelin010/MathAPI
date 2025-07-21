import math


def fibo(n: int) -> int:
    if n < 3:
        return 1
    c1, c2 = 1, 1
    count = 3
    while count != n:
        c3 = c1 + c2
        c1 = c2
        c2 = c3
        count += 1

    return c1 + c2


def fact(n: int) -> int:
    return math.prod([x for x in range(2, n + 1)])


def pow(n: int, m: int) -> int:
    return n**m


def gama_sum(n: int) -> int:
    return sum([i for i in range(1, n + 1)])


def cmmdc(n: int, m: int) -> int:
    rest = n % m
    while rest != 0:
        n = m
        m = rest
        rest = n % m

    return m


def cmmmc(n: int, m: int) -> float:  # float type not int
    cdc = cmmdc(n, m)
    return (n * m) / cdc
