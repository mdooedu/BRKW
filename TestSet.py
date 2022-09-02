import random
import maya.cmds as cmds


targetcount = list(range(int(input("targetcount"))))

print(targetcount)

for ctemp in targetcount:
    tempvec = [0, 90, 0]
    bfoloc = [cmds.getAttr("BRK" + ctemp - 1 + "translate")]
    cmds.duplicate("BRK" + ctemp)
    cmds.setAttr("BRK" + ctemp + ".rotate")
    templocc = bfoloc.pop[-1] + mvloc
    chgloc = bfoloc.append(templocc)
    cmds.setAttr("BRK" + ctemp + ".translate", chgloc)

    if ctemp == targetcount[-1]:
        break

print(ctemp)
