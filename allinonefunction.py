def add(a,b):
	sum = a + b
	print(sum)
def area_of_circle(r):
	area = 3.14 * r * r
	print(area)	 
def area_of_rec(l,w):
	area = l * w
	print(area)



def main12():
	print ("1.addition of two number")
	print ("2.Area of Rectangle")
	print ("3.Area Of Circle")
	x=int(input("enter the Selected Function No : "))
	if x==1:	
		a = int(input('Enter number a:'))
		b = int(input('Enter number b:'))
		add(a,b)
	elif x==2:
		radius = float(input('Enter Radius:'))
		print('Area:',area_of_circle(radius))
	elif x==3:
		ans1 = int(input('Enter length:'))
		ans2 = int(input('Enter width:'))
		print('Area of Rectangle:',area_of_rec(ans1,ans2))



main12()	