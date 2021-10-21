is_leap_year = False
   
input_year = int(input())

''' Type your code here. '''
if input_year%400 == 0:
    print(input_year, '- leap year')
elif input_year%100 == 0:
    print(input_year, '- not a leap year')
elif input_year%4 == 0:
    print(input_year, '- leap year')
else:
    print(input_year, '- not a leap year')