from vpython import *

plate = []

for x in arange(0, 5, 0.25):
    for y in arange(0, 5, 0.25):
        if y <= 0.5*x**2:
            ball = sphere(pos=vec(x, y, 0), radius=0.125)
            plate.append(ball)
        else:
            print()

for ball in plate:
    print(ball.pos.x)
