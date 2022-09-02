import random
#  import maya.cmds as cmds


def setRotate():
    type = random.choice([0, 1])

    if type == 1:
        setrotatevec = [0, 90, 0]
    else:
        setrotatevec = [0, 0, 0]

    return setrotatevec


print(setRotate())

def setvectob(tempvec):


