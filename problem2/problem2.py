#!/bin/python

def fibonacci(max):
	fibnumber = []
	fibnumber.append(1)
	fibnumber.append(1)
	while fibnumber[len(fibnumber)-1] < max:
		i = len(fibnumber)
		k = fibnumber[i-1]+fibnumber[i-2]
		fibnumber.append(k)
	return fibnumber

def sum(list):
	sum = 0
	for i in list:
		if i % 2 == 0:
			sum += i
	return sum

fiblist = fibonacci(4000000)
sum = sum(fiblist)
print sum
