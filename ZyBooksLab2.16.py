x = float(input())
y = float(input())
z = float(input())

value1 = ( x ** z )
value2 = ( x ** ( y ** z ))
value3 = abs(x - y)
value4 =  ((x ** z) ** .5 )

print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(value1, value2, value3, value4))