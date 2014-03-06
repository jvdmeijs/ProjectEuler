#!/bin/python

from math import sqrt

def check_if_prime(num):
    for x in range(3, int(1 + sqrt(num)), 2):
        if num % x == 0: return False
    return True

def find_primes(end):
    i = 0
    n = 3
    end = end -1
    max_prime = 0
    while i < end:
        if check_if_prime(n):
            i += 1
            if n > max_prime:
            	max_prime = n
        n += 2
    print max_prime

find_primes(10001)