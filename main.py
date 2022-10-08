from random import shuffle, random, choice
from time import sleep
from keyboard import is_pressed


'''def deposit():
    print('1 spin = $100')
    depositing = True

    while depositing:
        depAmount = input('How much money would you like to bet\n$')
        if depAmount.isdigit():
            depAmount = int(depAmount)
            if depAmount > 100:
                depositing = False
            else:
                print('you need at least $100 to play')
        else:
            print('please input an amount!')
    
    return depAmount'''
    

'''def jackpot():
    j = open('jackpot.txt', 'r+')
    jackpotValue = j.read()
    
    return jackpotValue'''


'''def spins():
    global depAmount
    costPerSpin = 100
    noSpins = (d // costPerSpin)

    return noSpins'''


def randomizer():
    return 1 - random()
    
x = ['Y','V','T','7⭐','R']
y = ['Y','V','T','7⭐','R']
z = ['Y','V','T','7⭐','R']

shuffle(x,randomizer)
shuffle(y, randomizer)
shuffle(z, randomizer)

game = ['.','.','.']

def intervals(gap):
    return sleep(gap)

def slotsGame():
    global x, y, z, game

    rotations = 0
    gap = 0.1
    playing = True

    while playing:
        for i in range(0,1):
            game[0] = x[i]
            game[1] = y[i]
            game[2] = z[i]

            x.append(x.pop(x.index(x[i])))
            y.append(y.pop(y.index(y[i])))
            z.append(z.pop(z.index(z[i])))

            print(game)
            intervals(gap)
        rotations += 1
        if rotations == 1:
            gap = 0.15
        if rotations == 5:
            gap = 0.2
        if rotations == 10:
            gap = 0.25
        if rotations == 15:
            print(game)
            break
        


def winCheck():
    print('---------------------------')
    if (game[0] == game[1] == game[2]):
        print('YOU WIN!!')
        print('---------------------------')
        
    else:
        print('YOU LOSE')
        print('---------------------------')



slotsGame()
winCheck()

    





        