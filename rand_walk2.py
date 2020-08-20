import random

def random_walk(n):
    ''' Return coordinates after 'n' block random walk. '''
    x = 0
    y = 0
    for i in range(n):
        (dx, dy) = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        ''' dx: difference in x, dy: difference in y '''
        x += dx
        y += dy
    return (x,y)


# Now let's take 25 random walks, each 10 blocks long.
for i in range(25):
    walk = random_walk(10)
    print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))
