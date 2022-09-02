import random
#  import maya.cmds as cmds


rng = [1, 2]
print(rng)

temp = random.choice(rng)

if temp == 1:
    retnrt = [0, 90, 0]

if temp == 2:
    retnrt = [0, 0, 0]

print(retnrt)
