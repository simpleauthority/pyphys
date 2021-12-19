from vpython import *

# create pivot point about which we will rotate
pivot = sphere()
pivot.color = vec(0, 1, 1)
pivot.pos = vec(-1, 0, 0)
pivot.radius = 0.25

# create coordinate axes
x_axis = cylinder(radius=0.05, pos=vec(-2, 0, 0), axis=vec(4, 0, 0), color=vec(1, 0, 0))
y_axis = cylinder(radius=0.05, pos=vec(0, -2, 0), axis=vec(0, 4, 0), color=vec(1, 1, 0))

# create some variables indicating the initial angle and rotational axis
angle = radians(60)  # theta initial; rad
rot_axis = vec(0, 1, 0)  # axis of rotation

# create the object which we want to rotate
line = cylinder()
line.radius = 0.05
line.pos = vec(-2, 0, 0)
line.axis = vec(3, 0, 0)
line.alpha = 2 * rot_axis  # angular acceleration; defined as a scalar multiplied by the rotational axis; units: rad/s^2
line.omega = -1.5 * rot_axis  # angular velocity; defined as a scalar multiplied by the rotational axis; units: rad/s
line.rotate(angle=angle, axis=rot_axis, origin=pivot.pos)  # rotate to theta initial

# create the initial values for tracking and display the tangential velocity
tip = line.pos + line.axis  # get the tip of the line for measuring values (velocity, acceleration, etc) at that point
r = tip - pivot.pos  # define an r vector from the pivot to the tip


# v_tan = omega x r
def tick_v_tan(omega, new_r):
    return cross(omega, new_r)


# a_c = rw^2 in -r_hat direction (toward center)
def tick_a_c(omega, new_r):
    return (mag(tick_v_tan(omega, new_r)) ** 2 / mag(new_r)) * -hat(new_r)


# a_tan = alpha x r
def tick_a_tan(alpha, new_r):
    return cross(alpha, new_r)


# create initial v_tan
# v_tan_arrow = arrow(pos=tip, axis=tick_v_tan(), color=color.purple)

# create initial a_c
a_c_arrow = arrow(pos=tip, axis=tick_a_c(line.omega, r), color=color.red)

# # create initial a_tan
a_tan_arrow = arrow(pos=tip, axis=tick_a_tan(line.alpha, r), color=color.blue)

# # create initial a_tot
# a_tot = a_c + a_tan
# a_tot_arrow = arrow(pos=tip, axis=a_tot, color=color.yellow)

t = 0  # elapsed time
dt = 0.01  # time step
sim_speed = 1  # speed of simulation

# wait to click the mouse before beginning
scene.waitfor('click')

# simulate the motion
while t < 6:
    # set fps
    rate(sim_speed / dt)

    # alpha = dw/dt -> dw = alpha*dt -> wf = wi + alpha*dt
    line.omega += line.alpha * dt

    # omega = dtheta/dt -> dtheta = omega*dt -> final_theta = initial_theta + omega*dt
    # dot product required because line.omega is a vector; this is the cleanest way to
    # get the correct vector component
    dtheta = dot(line.omega, rot_axis) * dt
    print(dtheta)

    # update line rotation
    line.rotate(angle=dtheta, axis=rot_axis, origin=pivot.pos)

    # update the tip, r vector
    tip = line.pos + line.axis  # get the tip of the line for measuring values (velocity, acceleration, etc) at that point
    r = tip - pivot.pos  # define an r vector from the pivot to the tip

    # v_tan_arrow.pos = tip
    # v_tan_arrow.axis = tick_v_tan()

    # update a_c
    a_c_arrow.pos = tip
    a_c_arrow.axis = tick_a_c(line.omega, r)

    # # update a_tan
    a_tan_arrow.pos = tip
    a_tan_arrow.axis = tick_a_tan(line.alpha, r)

    # # update a_tot
    # a_tot = a_c + a_tan
    # a_tot_arrow.pos = tip
    # a_tot_arrow.axis = a_tot

    # update dt
    t += dt
