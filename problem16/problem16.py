#!/bin/python

def addingnumbers(x):
	n = 2 ** x
	sum_of_n = 0
	for i in xrange(0,len(str(n)[i])):
		sum_of_n += int(str(n)[i])
	return sum_of_n

print addingnumbers(1000)