#!/bin/python

def palindromecheck(n):
	return int(str(n)[::-1]) == n

def findmaxnr():
	maxnr = 0
	for a in xrange(100,1000):
		for b in xrange(100,1000):
			product = a * b
			if palindromecheck(product) and product > maxnr:
				maxnr = product
	return maxnr

largest_palindrome = findmaxnr()
print(largest_palindrome)