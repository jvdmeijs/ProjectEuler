#!/bin/python

from math import sqrt
from sopd import d
import time as t

print 'start time: ' + t.strftime("%a %d %b %Y %X", t.gmtime())

def sum_of_non_abundant_numbers():
	L, s = 20162, 0
	abn = set()
 
	for n in range(1, L):
		if d(n) > n:
			abn.add(n)
		if not any( (n-a in abn) for a in abn ):
			s += n
	return s
 
print sum_of_non_abundant_numbers()

print 'Time finished: ' + t.strftime("%a %d %b %Y %X", t.gmtime())