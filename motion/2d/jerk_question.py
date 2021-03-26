from vpython import *

Jerk = 6

ball = sphere()
ball.v = vec(0, 0, 0)
ball.a = vec(0, 0, 0)

t = 0
dt = 0.25
while t <= 1:
    rate(1/dt)
    ball.a.x = Jerk*t
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    t += dt
    print("incr")

range_exp = ball.pos.x
range_th = 1

p_diff = (range_exp-range_th)/range_th*100
print(range_exp)
print(abs(p_diff))
