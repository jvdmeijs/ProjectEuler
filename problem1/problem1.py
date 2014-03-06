#!/bin/python

def sum(number):
	sum = 0
	for i in xrange(number):
		if i % 3 == 0 or i % 5 == 0:
			sum += i
	return sum
sum = sum(1000)
print sum
