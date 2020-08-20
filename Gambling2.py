# Dice Roll gambling simulation using Monte Carlo method

import random

def RollDice() :
    roll = random.randint(1,100)

    if roll == 100:
        #print(roll, 'roll was 100, you lose. Play again!')
        return False
    elif roll <= 50:
        #print(roll, 'roll was 1-50, you lose. Play again!')
        return False
    elif 100 > roll > 50 :
        #print(roll, 'roll was 51-100, you won. Play more!')
        return True


def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    currentWager = 0

    while currentWager <= wager_count :
        if RollDice():
            value += wager
        else :
            value -= wager

        currentWager += 1
    print('Funds: ', value)


x = 0
while x < 100 : 
    simple_bettor(1000, 100, 100)
    x += 1

