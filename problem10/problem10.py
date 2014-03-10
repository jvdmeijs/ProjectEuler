#!/bin/python

import math as m

def prime_sieve(maximum):
	# Mark every number between 0 and maximum as a primenumber.
	primes = [1 for x in xrange(maximum)]
	# Remove 0 and 1 as primenumbers.
	primes[0]=0
	primes[1]=0
	# Only need to go to sqrt(maximum).
	imax = int(m.sqrt(maximum) + 1)
	# As we removed 0 and 1 as primes let's start with 2. (no need to remove zero and one twice)
	i = 2
	# Loop trough the list and remove all non primes.
	while i<imax:
		j = i + i
		# Remove all the w
		while j < maximum:
			primes[j]=0
			j += i
		while True:
			i += 1
			if primes[i] == 1:
				break
	return primes

s = prime_sieve(2000000)
print sum(i for i in xrange(len(s)) if s[i] ==1 )