#!/bin/python

def sum_of_squares():
	a=0
	for i in xrange(0,101):
		a = a + (i*i)
	return a
def square_of_sum():
	b = 0
	for i in xrange(0,101):
		b = b + i
	b = b*b
	return b

difference = square_of_sum() - sum_of_squares()
print difference