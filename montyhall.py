import random

# solve montyhall simulate
def montyhall():
    # 1. set the doors
    doors = [0, 0, 1]
    random.shuffle(doors)
    # 2. choose a door
    choice = random.randint(0, 2)
    # 3. open a door
    for i in range(3):
        if i != choice and doors[i] == 0:
            open_door = i
            break
    # 4. change the choice
    for i in range(3):
        if i != choice and i != open_door:
            choice = i
            break
    return doors[choice]

# calculate probabilty
win = 0
for i in range(10000):
    win += montyhall()
print(win/10000)


