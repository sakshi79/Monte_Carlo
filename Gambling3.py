

import random
import matplotlib
import matplotlib.pyplot as plt 



def RollDice():
    roll = random.randint(1,100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll > 50:
        return True


def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    wX = []
    vY = []

    currentWager = 0

    while currentWager <= wager_count :
        if RollDice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else :
            value -= wager
            wX.append(currentWager)
            vY.append(value)
        currentWager += 1

        plt.plot(wX, vY)    


x = 0
while x < 100 : 
    simple_bettor(1000, 100, 1000)
    x += 1

plt.ylabel('Current value')
plt.xlabel('Wager count')
plt.show()