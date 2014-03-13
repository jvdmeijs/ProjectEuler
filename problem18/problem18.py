#!/bin/bash

import os

def readfile():
	file = os.getcwd() +'/triangle_18'		# The triangle used in problem 18
	''' file = os.getcwd() +'/triangle_67.txt' ''' 	# The triangle used in problem 67
	f = open (file,'r')
	triangle = []
	for line in f.readlines():
		numbers = line.split()
		for i in xrange(0,len(numbers)):
			numbers[i] = int(numbers[i])
		triangle.append(numbers)
	f.close()
	return triangle

def calculate_sum(l):
	for i in xrange(len(l)-1,0,-1):
		for k in xrange(0,len(l[i-1])):
			l[i-1][k] = l[i-1][k] + max(l[i][k],l[i][k+1])
	return l[0]

triangle = readfile()
print calculate_sum(triangle)