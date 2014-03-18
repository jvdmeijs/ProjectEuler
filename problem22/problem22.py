#!/bin/python

import os
#import locale

def name_list():
	names_list = []
	file_name = os.getcwd() +'/names.txt'
	f = open(file_name,'r')
	for line in f.readlines():
		line = line.replace('"','')
		names_list = line.split(',')
	return names_list

def sort_list(nlist):
	nlist.sort()
	#locale.setlocale(locale.LC_ALL, 'en_US.UTF-8'
	#assert sorted(nlist, key=cmp_to_key(locale.strcoll)
	return nlist

nlist = name_list()
nlist = sort_list(nlist)

def values():
	vals = []
	for i in xrange(1,27):
		vals.append(i)
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	return [alphabet,vals]

value_list = values()

def assignvalues(nlist,val):
	tot_val = 0
	for i in xrange(0,len(nlist)):
		word_val = 0
		for j in xrange(0,len(nlist[i])):
			for k in xrange(0,26):
				if nlist[i][j].lower() == val[0][k]:
					word_val += val[1][k]
		tot_val += word_val * (i+1)	
	return tot_val

print assignvalues(nlist,value_list)