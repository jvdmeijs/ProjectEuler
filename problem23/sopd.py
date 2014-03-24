from math import sqrt

def d(n):
    s = 1
    t = sqrt(n)
    for i in range(2, int(t)+1):
        if n % i == 0: s += i + n/i
    if t == int(t): s -= t    #correct s if t is a perfect square
    return s