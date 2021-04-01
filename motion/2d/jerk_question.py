from vpython import *
from decimal import Decimal

Jerk = 6

ball = sphere()
ball.v = vec(0, 0, 0)
ball.a = vec(0, 0, 0)

t = Decimal('0')
dt = Decimal('0.05')

while t <= 1:
    rate(1/dt)

    ball.a.x = Jerk * float(t)
    ball.v += ball.a * float(dt)
    ball.pos += ball.v * float(dt)

    t += dt

range_exp = ball.pos.x
range_th = 1

p_diff = (range_exp-range_th)/range_th*100
print(range_exp)
print(abs(p_diff))
