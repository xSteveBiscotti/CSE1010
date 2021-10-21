#Define functions: addition, subtraction, multiplication, division, and exponents.
#Get first number that user wants to use
num1 = float(input('Enter a number '))
myList = []
myList.append(num1)
count = 0 

#Define addition
def addition():
   num2 = float(input('Enter the number you would like to add:'))
   result = (num1 + num2)
   print(str(num1) + ' + ' + str(num2) + ' is: ' + str(result))
   myList.append(result)

#Define Subtraction
def subtraction():
    num2 = float(input('Enter the number you would like to subtract:'))
    result = (num1 - num2)
    print(str(num1) + ' - ' + str(num2) + ' is: ' + str(result))
    myList.append(result)

#Define multiplication
def multiplication():
    num2 = float(input('Enter the number you would like to multiply by:'))
    result = (num1 * num2)
    print(str(num1) + ' * ' + str(num2) + ' is: ' + str(result))
    myList.append(result)

#Define division
def division():
    num2 = float(input('Enter the number you would like to divide by:'))
    
    try:
        result = (num1 / num2)
        print(str(num1) + ' / ' + str(num2) + ' is: ' + str(result))
        myList.append(result)
    except ZeroDivisionError:
        print('Error: Cannot divie by Zero')

#Define exponents
def exponents():
    num2 = float(input('Enter the number you would like to raise to the power of:'))
    result = (num1 ** num2)
    print(str(num1) + '^' + str(num2) + ' is: ' + str(result))
    myList.append(result)

#Give menu of options to select
def menu():
    print('Select a function:')
    print('A = Addition')
    print('S = Subtraction')
    print('M = Multiplication')
    print('D = Division')
    print('E = Exponent')
    print('N = Enter a new number')
    print('P = Return previous answer')
    print('O = Return original Number')
    print('Q = Quit')

#Get input from user and see what they want to do 

if __name__ == "__main__":
    stopFunction = 0

    while stopFunction != 1:

        print('')
        menu()
        desiredOperation = (input('What would you like to do ? '))
        #Apply the desired operation
        if desiredOperation == 'A':
            addition()
            count += 1
            num1 = myList[-1]
    
        elif desiredOperation == 'a':
            addition()
            count += 1
            num1 = myList[-1]

        elif desiredOperation == 'S':
            subtraction()
            count += 1
            num1 = myList[-1]

        elif desiredOperation == 's':
            subtraction()
            count += 1
            num1 = myList[-1]

        elif desiredOperation == 'M':
            multiplication()
            count += 1
            num1 = myList[-1]

        elif desiredOperation == 'm':
            multiplication()
            count += 1
            num1 = myList[-1]

        elif desiredOperation == 'D':
            division()
            count += 1
            num1 = myList[-1]

        elif desiredOperation == 'd':
            division()
            count += 1
            num1 = myList[-1]

        elif desiredOperation == 'E':
            exponents()
            count += 1
            num1 = myList[-1]

        elif desiredOperation == 'e':
            exponents()
            count += 1
            num1 = myList[-1]

        elif desiredOperation == 'N':
            num1 = float(input('Enter a new number '))
            count += 1
        
        elif desiredOperation == 'n':
            num1 = float(input('Enter a new number '))
            count += 1

        elif desiredOperation == 'P':
            print(myList[-2])

        elif desiredOperation == 'p':
            print(myList[-2])
        
        elif desiredOperation == 'O':
            print(myList[0])
        
        elif desiredOperation == 'o':
            print(myList[0])
        
        elif desiredOperation == 'Q':
            print('Done')
            stopFunction += 1

        elif desiredOperation == 'q':
            print('Done')
            stopFunction += 1 

        else:
            print('Invalid Selection')



