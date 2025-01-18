Eng 	=int(input('Enter The marks of english :' ))
Sci 	=int(input('Enter The marks of science :' ))	
Maths	=int(input('Enter The marks of Maths :' ))	
Hindi	=int(input('Enter The marks of hindi:' ))
Python	=int(input('Enter The marks of python :' ))
java	=int(input('Enter The marks of java:' ))
web	=int(input('Enter The marks of web :' ))

Total = Eng + Sci + Maths + Hindi + Python + java + web

Per = Total / 7

print('Total Marks : ',Total)

fail = False
for sub in [Eng , Sci , Maths , Hindi , Python , java , web]:
  if sub < 35:
    fail = True
    break

print('Percentage :',Per,'%')

