''' Type your code here. '''
x = int(input())
str1 = ''

while x > 0:
    out = x % 2 
    str1 += str(out)
    x = x//2
print(str1)
