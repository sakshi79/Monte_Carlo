import random

def random_walk(n):
    ''' Return coordinates after 'n' block random walk. '''
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y += 1
        elif step == 'S':
            y -= 1
        elif step == 'E':
            x += 1
        elif step == 'W':
            x -= 1
    return (x,y)


# Now let's take 25 random walks, each 10 blocks long.
for i in range(25):
    walk = random_walk(10)
    print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))