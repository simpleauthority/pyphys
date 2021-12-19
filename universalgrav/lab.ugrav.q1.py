from vpython import *

G = 6.67e-11  # Universal gravitation constant


def compute_grav(m1, m2, r):
    return ((G * m1 * m2) / (mag(r) ** 2)) * -hat(r)


def compute_pe(m1, m2, r):
    return -((G * m1 * m2) / mag(r))


# draw a set of coordinate axes
x_axis = cylinder(pos=vec(-1, 0, 0), axis=vec(2, 0, 0), radius=0.005)
y_axis = cylinder(pos=vec(0, -1, 0), axis=vec(0, 2, 0), radius=0.005)

scale_factor = 1  # used to scale force arrows (to make arrows visible)

rock1 = sphere(color=color.orange, radius=0.05)
rock2 = sphere(color=color.cyan, radius=0.05)
rock3 = sphere(color=color.yellow, radius=0.05)

# set initial rock positions
rock1.pos = vec(0, .4, 0)
rock2.pos = vec(-.3, .4, 0)
rock3.pos = vec(0, 0, 0)

# set rock masses
rock1.m = 1e4
rock2.m = 2e4
rock3.m = 3e4

# calculate center-to-center distances for each rock-rock system
r_1to3 = rock3.pos - rock1.pos
r_2to3 = rock3.pos - rock2.pos

# calculate initial forces
F_1on3 = compute_grav(rock1.m, rock3.m, r_1to3)
F_2on3 = compute_grav(rock2.m, rock3.m, r_2to3)

# calculate net forces
F_net_on3 = F_1on3 + F_2on3

# create initial force arrows
F_1on3_arrow = arrow(pos=rock3.pos, axis=scale_factor * F_1on3, color=rock3.color)
F_2on3_arrow = arrow(pos=rock3.pos, axis=scale_factor * F_2on3, color=rock3.color)

# Compute the potential energy
U_13 = compute_pe(rock1.m, rock3.m, r_1to3)
U_23 = compute_pe(rock2.m, rock3.m, r_2to3)
U_net = U_13 + U_23

print(f'The gravitational FORCE is {F_net_on3} N.')
print(f'The MAGNITUDE of gravitational force ON 3 is {mag(F_net_on3):.2f} N.')
print(f'The gravitational potential energy is {U_net:.1f} J.')
