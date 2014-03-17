#!/bin/python

# First a function to give all the primefactors of a random number n.
def find_factor(n):
	primefac = []
	d = 2
	while d*d <= n:
		while (n % d) == 0:
			primefac.append(d)
			n /= d
		d += 1
	if n > 1:
		primefac.append(n)
	return primefac
# A function to find the unique prime factors out of a list of all prime factors and how often the uniqe primefactors occurs.
def multiply_list (primefac):
	a = 0
	a_l = []
	p = 0
	p_l = []
	for i in primefac:
		if i > p:
			if a != 0 and p != 0 :
				a_l.append(a)
				p_l.append(p)
			p = i
			a = 1
		elif i == p:
			a += 1
	a_l.append(a)
	p_l.append(p)
	mul_list = [p_l,a_l]
	return mul_list
# A function to calculate the product of all the primenumbers.
def multiply_numbers(l):
	prod = 1 
	for i in xrange(0,len(l[0])):
		prod = prod * ( l[0][i] ** ( l[1][i] + 1 ) - 1 ) / ( l[0][i] - 1 )
	return prod

# A function to bind them all, and give a list of all amicable numbers.
def find_amicables(n):
	numbers = []
	for j in xrange(2,n+1):
		prime_list = find_factor(j)
		mul_list = multiply_list(prime_list)
		prod = multiply_numbers(mul_list) - j
		if prod > j and prod <= n:
			sec_prime_list = find_factor(prod)
			sec_mul_list = multiply_list(sec_prime_list)
			sec_prod = multiply_numbers(sec_mul_list) - prod
			if sec_prod == j:
				numbers.append(j)
				numbers.append(prod)
	return numbers

print sum(find_amicables(10000))