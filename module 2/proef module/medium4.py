from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:

for x in range(5):
    robotArm.grab()
    for y in range (x + 2): robotArm.moveRight()
    robotArm.drop()
    for y in range (x + 2): robotArm.moveLeft()
for y in range (6):
    robotArm.moveRight()
for x in range(5):
    robotArm.grab()
    for y in range ((5 - x)): robotArm.moveLeft()
    robotArm.drop()
    for y in range ((5 - x) - 1): robotArm.moveRight()


# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

