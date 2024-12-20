from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code starts here:

for x in range(9):
    robotArm.grab()
    if robotArm.scan() == "red":
        for y in range(9 - x): robotArm.moveRight()
        robotArm.drop()
        for y in range(9 - x): robotArm.moveLeft()
    else: robotArm.drop()
    robotArm.moveRight()

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

