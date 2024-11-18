from time import sleep

while True:
    for x in range(20):
        print("Rood", x + 1)
        sleep(0.8)
    for x in range(30):
        print("Groen", x + 1)
        sleep(0.8)
    for x in range(10):
        print("Oranje", x + 1)
        sleep(0.8)