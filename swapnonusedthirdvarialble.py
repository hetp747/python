x = int(input('enter value X :'))
y = int(input('enter value Y :'))
print("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
x = x + y # x = 15.7, y = 10.3
y = x - y # x = 15.7, y = 5.4
x = x - y # x = 10.3, y = 5.4
print("After swapping: ")
print("Value of x : ", x, " and y : ", y)
