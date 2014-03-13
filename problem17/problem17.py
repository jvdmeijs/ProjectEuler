#!/bin/python

unit_names = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
tens_names = 'zero ten twenty thirty forty fifty sixty seventy eighty ninety'.split()

def number_of_apperanceses(n,i):
	a = '1'

	if i == 1000:
		a = '000'
	elif i == 100:
		a = '00'
	elif i == 10:
		a = '0'
	elif i == 1:
		a = '' 

	return int(str(n)[0]+''+a) // i

def dictinary(n):
	if n > 9999:
		quit('cannot exceed limit of 9999')
	number_name = ''
	while n>0:
		if n >= 1000:
			number_of_apperance = number_of_apperanceses(n,1000)
			number_name = number_name + unit_names[number_of_apperance] + ' thousand'
			n = n % 1000
		elif n >= 100:
			number_of_apperance = number_of_apperanceses(n,100)
			if n % 100 == 0:
				number_name = number_name + unit_names[number_of_apperance] + ' hundred'
			else:
				number_name = number_name + unit_names[number_of_apperance] + ' hundred and'
			n = n % 100
		elif n >= 20:
			number_of_apperance = number_of_apperanceses(n,10)
			if n % 10 == 0:
				number_name = number_name + tens_names[number_of_apperance]
			else:
				number_name = number_name + tens_names[number_of_apperance] + '-'
			n = n % 10
		else:
			number_name = number_name + unit_names[n]
			n = n % 1
	print number_name
	return number_name

def sum_over_the_numbers(x):
	total_count = 0
	for i in xrange(1,x+1):
		total_count += len(dictinary(i).replace(' ','').replace('-',''))
	print total_count

sum_over_the_numbers(1000)