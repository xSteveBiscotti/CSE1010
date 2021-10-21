import math

initfreq = int(input())
r = (2 ** (1 / 12))
value1 = (initfreq)
value2 = (initfreq * (r ** 1))
value3 = (initfreq * (r ** 2))
value4 = (initfreq * (r ** 3))
value5 = (initfreq * (r ** 4))

print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(value1, value2, value3, value4, value5))