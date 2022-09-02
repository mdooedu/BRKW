import random
#  import maya.cmds as cmds


def setRotate():
    temptype = random.choice(range(1, 3))

        if temptype == 1:
            setrotatevec = [0, 90, 0]
        else:
            setrotatevec = [0, 0, 0]

        return setrotatevec

