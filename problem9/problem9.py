#!bin/pyhton

def findproduct(x):
	for a in xrange(1,x/3):
		for b in xrange(a,x/2):
			c = x - a - b
			if (a*a + b*b) == (c*c):
				print a*b*c
				break
findproduct(1000)