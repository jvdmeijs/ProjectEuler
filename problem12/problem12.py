#!/bin/python

import math

def div(n,imax):
	l = 0
	for i in range(1,imax):
		if (n % i) == 0:
			l = l + 2
	return l

def trianglenumber(number_of_div):
	check = False
	n = 0
	while check == False:
		number = (n * (n + 1)) / 2
		imax = int(math.sqrt(number)) + 1
		l = div(number,imax)

		if l > number_of_div:
			check = True
		else:
			n = n + 1
	return number

a = trianglenumber(500)
print 'The number you where looking for is: ', a