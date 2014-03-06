#!/bin/python

from fractions import gcd
from functools import reduce

def lcm(a,b):
	c = a*b//gcd(a,b)
	return c

def smallest_multiplier():
	k = reduce(lcm,range(1,21))
	return k

smallest_multiplier = smallest_multiplier()
print smallest_multiplier