from random import shuffle, random

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
    return random()
    
x = ['Y','V','T','R','W',7,'X','D','A','S']

shuffle(x,randomizer)

print(x)
