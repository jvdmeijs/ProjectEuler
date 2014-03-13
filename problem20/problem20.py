#!/bin/pyhton

import math as m

def count_numbers(n):
	k = str(m.factorial(n))
	count = 0
	for i in xrange(0,len(k)):
		count += int(k[i])
	return count

print count_numbers(100)