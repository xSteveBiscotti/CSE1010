userNum = int(input('Enter integer:\n'))

num2 = (userNum * userNum)
num3 = (userNum ** 3)

print('You entered: '+ str(userNum))
print(str(userNum) + ' Squared is ' + str(num2)) 
print('And ' + str(userNum) + ' cubed is ' + str(num3) + ' !!')

userNum2 = int(input('Enter another integer:\n'))
num4 = (userNum + userNum2)
num5 = (userNum * userNum2)

print(str(userNum) + ' + ' + str(userNum2) + ' is ' + str(num4))
print(str(userNum) + ' * ' + str(userNum2) + ' is ' + str(num5))