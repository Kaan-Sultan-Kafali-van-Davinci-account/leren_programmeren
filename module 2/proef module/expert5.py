from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:

c = {"red": 0, "yellow": 0, "blue": 0}
preference = {"red": False, "yellow": False, "blue": False}
color_indices = []

robotArm.moveRight()
for x in range(9):
    robotArm.grab()
    c[robotArm.scan()] += 1
    if x == 0: preference[robotArm.scan()] = True
    color_indices.append(robotArm.scan())
    robotArm.drop()
    if x < 8: robotArm.moveRight()

max_value = max(c.values())
candidates = [color for color, count in c.items() if count == max_value]
preferred_color = next((color for color in candidates if preference[color]), None)
mc = preferred_color if preferred_color else candidates[0]

print(mc)

for x in range(8): robotArm.moveLeft()

for x in range(9):
    if mc == color_indices[x]:
        robotArm.grab()
        if robotArm.scan() == mc:
            for y in range(x + 1): robotArm.moveLeft()
            robotArm.drop()
            for y in range(x + 2):
                if x < 8 and y < 9: robotArm.moveRight()
    else:
        #robotArm.drop()
        if x < 8: robotArm.moveRight()

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

