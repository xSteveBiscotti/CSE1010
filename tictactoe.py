#Tic tac toe game

winner = 0
movecount = 0
charwinner = ''
topleft = ' '
topmid = ' '
topright = ' '
midleft = ' '
mid = ' '
midright = ' '
botleft = ' '
botmid = ' '
botright = ' '

#print board
def printboard():
    print(topleft + '|' + topmid + '|' + topright)
    print('-+-+-')
    print(midleft + '|' + mid + '|' + midright)
    print('-+-+-')
    print(botleft + '|' + botmid + '|' + botright)

#give move options
def menu():
    print('')
    print('Select a space')
    print('TL = Top left')
    print('TM = Top Middle')
    print('TR = Top right')
    print('ML = Middle left')
    print('M = Middle')
    print('MR = Middle Right')
    print('BL = Bottom Left')
    print('BM = Bottom Middle')
    print('BR = Bottom Right')

#Get Desired move, check if space not taken, change board
while winner != 1:

    printboard()
    menu()

    desiredMove = input('Choose a space: ')

    if desiredMove.upper() == 'TL':
        if topleft == ' ':
            if (movecount%2) == 0:
                topleft = 'X'
                movecount +=1 
            else:
                topleft = 'O'
                movecount +=1
        else:
            print('Invalid Move')

    elif desiredMove.upper() == 'TM':
        if topmid == ' ':
            if (movecount%2) == 0:
                topmid = 'X'
                movecount +=1 
            else:
                topmid = 'O'
                movecount +=1
        else:
            print('Invalid Move')

    elif desiredMove.upper() == 'TR':
        if topright == ' ':
            if (movecount%2) == 0:
                topright = 'X'
                movecount +=1 
            else:
                topright = 'O'
                movecount +=1
        else:
            print('Invalid Move')

    elif desiredMove.upper() == 'ML':
        if midleft == ' ':
            if (movecount%2) == 0:
                midleft = 'X'
                movecount +=1 
            else:
                midleft = 'O'
                movecount +=1
        else:
            print('Invalid Move')

    elif desiredMove.upper() == 'M':
        if mid == ' ':
            if (movecount%2) == 0:
                mid = 'X'
                movecount +=1 
            else:
                mid = 'O'
                movecount +=1
        else:
            print('Invalid Move')

    elif desiredMove.upper() == 'MR':
        if midright == ' ':
            if (movecount%2) == 0:
                midright = 'X'
                movecount +=1 
            else:
                midright = 'O'
                movecount +=1
        else:
            print('Invalid Move')

    elif desiredMove.upper() == 'BL':
        if botleft == ' ':
            if (movecount%2) == 0:
                botleft = 'X'
                movecount +=1 
            else:
                botleft = 'O'
                movecount +=1
        else:
            print('Invalid Move')

    elif desiredMove.upper() == 'BM':
        if botmid == ' ':
            if (movecount%2) == 0:
                botmid = 'X'
                movecount +=1 
            else:
                botmid = 'O'
                movecount +=1
        else:
            print('Invalid Move')

    elif desiredMove.upper() == 'BR':
        if botright == ' ':
            if (movecount%2) == 0:
                botright = 'X'
                movecount +=1 
            else:
                botright = 'O'
                movecount +=1
        else:
            print('Invalid Move')

    else:
        print('Invalid Selection')

    #check if winner for X's

    if topleft == 'X':
        if topmid == 'X':
            if topright == 'X':
                winner += 1
                charwinner = 'X\'s'
        elif midleft == 'X':
            if botleft == 'X':
                winner += 1
                charwinner = 'X\'s'
        elif mid == 'X':
            if botright == 'X':
                winner += 1
                charwinner = 'X\'s'

    elif topmid == 'X':
        if mid == 'X':
            if botmid == 'X':
                winner += 1
                charwinner = 'X\'s'

    elif topright == 'X':
        if midright == 'X':
            if botright == 'X':
                winner += 1
                charwinner = 'X\'s'

        elif mid == 'X':
            if botleft == 'X':
                winner += 1
                charwinner = 'X\'s'

    elif midleft == 'X':
        if mid == 'X':
            if midright == 'X':
                winner += 1
                charwinner = 'X\'s'

    elif botleft == 'X':
        if botmid == 'X':
            if botright == 'X':
                winner += 1
                charwinner = 'X\'s'

    #check if winner for O's

    elif topleft == 'O':
        if topmid == 'O':
            if topright == 'O':
                winner += 1
                charwinner = 'O\'s'

        elif midleft == 'O':
            if botleft == 'O':
                winner += 1
                charwinner = 'O\'s'

        elif mid == 'O':
            if botright == 'O':
                winner += 1
                charwinner = 'O\'s'

    elif topmid == 'O':
        if mid == 'O':
            if botmid == 'O':
                winner += 1
                charwinner = 'O\'s'

    elif topright == 'O':
        if midright == 'O':
            if botright == 'O':
                winner += 1
                charwinner = 'O\'s'

        elif mid == 'O':
            if botleft == 'O':
                winner += 1
                charwinner = 'O\'s'

    elif midleft == 'O':
        if mid == 'O':
            if midright == 'O':
                winner += 1
                charwinner = 'O\'s'

    elif botleft == 'O':
        if botmid == 'O':
            if botright == 'O':
                winner += 1
                charwinner = 'O\'s'

    if winner == 1:
        printboard()
        print(charwinner + ' Won!')
        restart = input('Would you like to play again y/n')
        if restart.upper() == 'Y':
            winner = 0
            movecount = 0
            charwinner = ''
            topleft = ' '
            topmid = ' '
            topright = ' '
            midleft = ' '
            mid = ' '
            midright = ' '
            botleft = ' '
            botmid = ' '
            botright = ' '
            

    if movecount == 9:
        print('You tied')
        winner += 1
        restart = input('Would you like to play again y/n: ')
        if restart.upper() == 'Y':
            winner = 0
            movecount = 0
            charwinner = ''
            topleft = ' '
            topmid = ' '
            topright = ' '
            midleft = ' '
            mid = ' '
            midright = ' '
            botleft = ' '
            botmid = ' '
            botright = ' '
    
