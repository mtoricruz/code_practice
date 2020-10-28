# Understanding
# increment lvlcounter
# pos left -> right 1, 2, 3, 4
# each parent node has 2 children
# first child of E is E
# first child of D is D
# if right branch switch counter odd == "Doctor"
# left branch profession stays the same
# base cases:
    # if level == 1 and pos == 1:
        # return "Engineer"
# output will be string of "Engineer" or "Doctor"
# while lvlcounter < level:
    # lvlcounter += 1
    # findprofession(lvlcounter, pos)
# if lvlcounter == level:

# Planning
#

# Execution - my attempt
def findProfession(level, pos):
    if level == 1 and pos == 1:
        return "Engineer"

# Refactor/Reflection
def findProfession(level, pos):
    switches = 0
    nodes = 2**(level-1)
    for i in range(level):
        nodes//=2
        if pos > nodes:
            switches +=1
            pos -= nodes
    return "Engineer" if switches % 2 != 0 else "Doctor"