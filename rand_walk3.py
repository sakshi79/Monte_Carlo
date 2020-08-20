''' What is the longest random walk you can take so that on average you end up 4 blocks or fewer from your home?
No transport fee in that case. '''


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


number_of_walks = 10000

for walk_length in range(1,31):
    no_transport = 0      # number of no transport walks
    for i in range(number_of_walks):     # beginning of Monte Carlo loop
        (x,y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_fr = float(no_transport) /  number_of_walks     # fraction of total walks that required no transport fee.
    print("Walk size = ", walk_length, " , %age of no transport walks = ", no_transport_fr*100)

# Here our answer will be the longest walk in the output with no transport %age > 50
# Hence, answer = 22 (by viewing output) 
