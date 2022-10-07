def deposit():
    print('1 spin = $100')
    depositing = True
    while depositing:
        depAmount = input('How much money would you like to bet\n$')
        if type(depAmount) == int:
            depAmount = int(depAmount)
            if depAmount > 100:
                break
            else:
                print('you need at least $100 to play')
        else:
            print('please input an amount!')
    
    return depAmount
    


deposit()
                
