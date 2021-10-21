''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

''' Type your code here. '''
def func1(x, y):
    return a*x + b*y - c
def func2(x, y):
    return d*x + e*y - f
finalx = 100
finaly = 100
for x in range(-10, 11):
    for y in range(-10,11):
        if func1(x,y) == func2(x,y) and func1(x,y) == 0:
            finalx = x
            finaly = y
if finalx != 100:
    print('x =',finalx,', y =', finaly)
else:
    print('There is no solution')