#!/bin/python

import math as m

def number_of_steps(x):
	numerator = m.factorial(2 * x)
	denominator = ( m.factorial( x ) ) ** 2
	numberofsteps = numerator / denominator
	return numberofsteps

print number_of_steps(20)