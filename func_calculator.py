def calculator(a,op,b):
	if op == '+':
		result  = a+b
	elif op == '-':
		result = a-b
	elif op == '*':
		result = a*b
	elif op == '/':
		result = a/b
	return result

a = float(input('Enter First Number:'))
op = input('Enter Operator (+,-,*,/):')
b = float(input('Enter Second Number:'))
print('Result:',calculator(a,op,b))



