#Coin Flip Streaks
#Write a program to find out how often a streak of six heads or a streak
#of six tails comes up in a randomly generated list of heads and tails

import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    rawData = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            rawData.append('H')
        else:
            rawData.append('T')    
        
    # Code that checks if there is a streak of 6 heads or tails in a row.
    i = 0
    heads = 0
    tails = 0
    while (heads<6) and (tails<6) and (i<100):
        if rawData[i] == "H":
            heads += 1
            tails = 0
        else:
            tails += 1
            heads = 0
        i += 1

    if (heads == 6) or (tails == 6):
        numberOfStreaks += 1
    
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
