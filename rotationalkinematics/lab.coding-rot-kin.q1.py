from vpython import *


# some functions
def r(a, b):
    return a.pos - b.pos


def square_vec(input_vector):
    return dot(hat(input_vector), vec(input_vector.x ** 2, input_vector.y ** 2, input_vector.z ** 2))


# set up scene
scene = canvas(title='Rotational Kinematics', width=300, height=200, center=vec(0, 0, 0), background=vec(1, 1, 1))
scene.range = 1.1

# draw & label a set of coordinate axes
line_x = cylinder(pos=vec(-1, 0, 0), axis=vec(2, 0, 0), radius=0.005, color=vec(0, 0, 0))
text(text='x', pos=line_x.pos + line_x.axis, color=vec(0.8, 0, 0.7), billboard=True, height=0.1)
line_y = cylinder(pos=vec(0, -1, 0), axis=vec(0, 2, 0), radius=0.005, color=vec(0, 0, 0))
text(text='y', pos=line_y.pos + line_y.axis, color=vec(0.8, 0, 0.7), billboard=True, height=0.1)

# draw a pivot at the center of the screen
pivot = sphere(pos=vec(0, 0, 0), radius=0.01, color=color.magenta)

# draw a horizontal rod of length 1
rod = cylinder(pos=pivot.pos, radius=0.01, axis=vec(1, 0, 0), color=color.red)

# draw a bug on the rod
bug_r = 0.6  # radius from pivot to bug
bug = sphere(pos=rod.pos + vec(bug_r, 0, 0), radius=0.05, color=color.blue, make_trail=True, trail_type="points",
             interval=2, retain=30, trail_radius=0.01)

# define a ball's acceleration as well as initial position & initial velocity
theta = radians(30)  # this converts the angle to RADIANS
omega = 5  # units are RADIANS/sec
alpha = -1  # units are RADIANS/sec**2
rotation_axis = vec(0, 0, 1)  # specifies axis of rotation as the z-axis

omega_vector = omega * rotation_axis
bug_velocity = cross(omega_vector, r(bug, pivot))
scale_arrow = 0.05
bug_arrow = arrow(pos=bug.pos, color=bug.color, axis=scale_arrow * bug_velocity)

# rotate rod and bug to initial angle
rod.rotate(angle=theta, axis=rotation_axis, origin=pivot.pos)
bug.rotate(angle=theta, axis=rotation_axis, origin=pivot.pos)

# simulation variables
t = 0
dt = 0.1
dtheta = 0
sim_speed = 1

# simulate
while t < 10:
    rate(sim_speed / dt)

    omega += alpha * dt  # update omega
    dtheta = omega * dt  # set change in theta

    print(f'omega now {omega}; rotating to {dtheta}')

    # rotate rod and bug to the new angle
    rod.rotate(angle=dtheta, axis=rotation_axis, origin=pivot.pos)
    bug.rotate(angle=dtheta, axis=rotation_axis, origin=pivot.pos)

    omega_vector = omega * rotation_axis

    bug_velocity = cross(omega_vector, r(bug, pivot))
    bug_arrow.pos = bug.pos
    bug_arrow.axis = scale_arrow * bug_velocity

    # a_c = w^2 * r
    centripetal_accel = square_vec(omega_vector) * r(bug, pivot)

    # a_tan = alpha * r
    tangential_accel = alpha * r(bug, pivot)

    t += dt

print(f'a_c = {centripetal_accel}')
print(f'a_tan = {tangential_accel}')
