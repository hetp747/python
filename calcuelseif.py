no1=int(input("Enter number 1:"))
no2=int(input("Enter number 2:"))

print("1.Addition ")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

no = int(input("Select operation :"))

if no==1:
	sum=no1+no2
	print("Addition is  : ",sum)
elif no==2:
	sub=no1-no2
	print("Substraction is :",sub)
elif no==3:
	mul=no1*no2
	print("Substraction is :",mul)
elif no==4:	
	div=no1/no2
	print("Substraction is :",sub)
else:
	print("invalid choose the 1 to 4")
