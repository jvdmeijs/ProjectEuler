#!/bin/python

def primefactor(n):
	all_factors =[]
	d = 2	#smallest primefactor
	while n>1:
		while n % d ==0:
			all_factors.append(d)
			n /= d
		d = d + 1
		if d*d >n:
			if n>1:
				 all_factors.append(n)
			break
	return all_factors
primefactor = primefactor(600851475143)
largest_primefactor = max(primefactor)
print largest_primefactor
