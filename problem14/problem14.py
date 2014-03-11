#!/bin/python

def generate_numbers():
	chainlenth = 0
	maxchain = 0
	maxnumber= 0
	for i in xrange(1,1000000):
		n = i
		chainlenth = 0
		while n > 1:
			if (n % 2) == 0 :
				n = n / 2
				chainlenth += 1
			elif (n % 2) == 1:
				n = 3 * n + 1
				chainlenth += 1
			else:
				quit('Error, the number ' + i + ' is not odd nor even!')
		if chainlenth > maxchain:
			maxnumber = i
			maxchain = chainlenth
	return maxnumber

print 'The number you where looking for is: ' + generate_numbers()