#!/bin/python
# I chose to use a method which incuded a file to make the script more readable.
import os

def getcwd():
	cwd = os.getcwd()
	return cwd

def readfile(cwd,filename):
	filelocation = cwd + '/' + filename
	print 'File to open:' + filelocation
	f = open(filelocation, 'r' )
	lines = []
	for line in f.readlines():
		lines.append(line)
	return lines

def sum_on_list(num_list):
	total = 0
	for i in num_list:
		total = total + int(i)
	total = str(total)
	if len(total) >= 10:
		sub_tot = total[:10]
	else:
		quit('Error, cannot select the first ten decimals from your list. To few numbers.')
	return sub_tot
		

cwd = getcwd()
num_list = readfile(cwd,'numlist')
first_ten = sum_on_list(num_list)
print 'The first ten characters are:' + first_ten

