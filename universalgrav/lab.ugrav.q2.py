from vpython import *

G = 6.67e-11  # Universal gravitation constant


def compute_grav(m1, m2, r):
    return ((G * m1 * m2) / (mag(r) ** 2)) * -hat(r)


def compute_pe(m1, m2, r):
    return -((G * m1 * m2) / mag(r))


# draw a set of coordinate axes
x_axis = cylinder(pos=vec(-3e9, 0, 0), axis=vec(6e9, 0, 0), radius=3e7)
y_axis = cylinder(pos=vec(0, -3e9, 0), axis=vec(0, 6e9, 0), radius=3e7)

scale_factor = 1e13  # used to scale force arrows (to make arrows visible)

rock1 = sphere(color=color.orange, radius=5e8)
rock2 = sphere(color=color.cyan, radius=2e8)
rock3 = sphere(color=color.yellow, radius=5e8)

# set initial rock positions
rock1.pos = vec(0, 3e9, 0)
rock2.pos = vec(6e9, 0, 0)
rock3.pos = vec(0, -3e9, 0)

# set rock masses
rock1.m = 10e24
rock2.m = 1
rock3.m = 10e24

# set initial momentum for rocks
rock2.p = vec(0, 0, 0)

# calculate center-to-center distances for each rock-rock system
r_1to2 = rock2.pos - rock1.pos
r_3to2 = rock2.pos - rock3.pos

# calculate initial forces
F_1on2 = compute_grav(rock1.m, rock2.m, r_1to2)
F_3on2 = compute_grav(rock3.m, rock2.m, r_3to2)

# calculate net forces
F_net_on2 = F_1on2 + F_3on2

# create initial force arrows
F_1on2_arrow = arrow(pos=rock2.pos, axis=scale_factor * F_1on2, color=rock2.color)
F_3on2_arrow = arrow(pos=rock2.pos, axis=scale_factor * F_3on2, color=rock2.color)

t = 0
dt = 300
sim_speed = 100e9

scene.waitfor('click')

while t < 1e20:
    rate(sim_speed / dt)

    # calculate center-to-center distances for each rock-rock system
    r_1to2 = rock2.pos - rock1.pos
    r_3to2 = rock2.pos - rock3.pos

    # update forces
    F_1on2 = compute_grav(rock1.m, rock2.m, r_1to2)
    F_3on2 = compute_grav(rock3.m, rock2.m, r_3to2)

    # find new net forces
    F_net_on2 = F_1on2 + F_3on2

    # update momentums
    rock2.p += F_net_on2 * dt

    # update positions
    rock2.pos += (rock2.p / rock2.m) * dt

    # update arrows
    F_1on2_arrow.pos = rock2.pos
    F_1on2_arrow.axis = scale_factor * F_1on2
    F_3on2_arrow.pos = rock2.pos
    F_3on2_arrow.axis = scale_factor * F_3on2

    t += dt

# Compute the potential energy
U_12 = compute_pe(rock1.m, rock2.m, r_1to2)
U_32 = compute_pe(rock2.m, rock3.m, r_3to2)
U_net = U_12 + U_32

print('The gravitational FORCE is ' + F_net_on2 + ' N.')
print(f'The MAGNITUDE of gravitational force ON 2 is {mag(F_net_on2):.2f} N.')
print(f'The gravitational potential energy is {U_net:.1f} J.')
