from random import shuffle, random, choice
from time import sleep

def deposit():
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
    
    return depAmount
    

def jackpot():
    j = open('jackpot.txt', 'r+')
    jackpotValue = j.read()
    
    return jackpotValue


def spins():
    global depAmount
    costPerSpin = 100
    noSpins = (depAmount // costPerSpin)

    return noSpins


def randomizer():
    return 1 - random()
    
x = ['Y','V','T','R','W',7,'X','D','A','S']
y = ['Y','V','T','R','W',7,'X','D','A','S']
z = ['Y','V','T','R','W',7,'X','D','A','S']

shuffle(x,randomizer)
shuffle(y, randomizer)
shuffle(z, randomizer)

game = ['.','.','.']

def intervals(gap):
    return sleep(gap)

def slotsGame():
    global x, y, z, game

    playing = True
    rotations = 0
    gap = 0.1

    while playing:
        for i in range(0,1):
            game[0] = x[i]
            game[1] = y[i]
            game[2] = z[i]

            x.append(x.pop(x.index(x[i])))
            y.append(y.pop(y.index(y[i])))
            z.append(z.pop(z.index(z[i])))

            print(f'\r{game}')
            intervals(gap)
        rotations += 1
        if rotations == 5:
            gap = 0.2
        if rotations == 15:
            gap = 0.25
        if rotations == 25:
            gap = 0.4
        if rotations == 30:
            print(game)
            break

        
        

slotsGame()
    




        