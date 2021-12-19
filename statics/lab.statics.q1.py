from vpython import *

# assumptions
L = 1.0  # length of rod and support cable
m = 1.0  # mass of rod
M = 4.0  # mass of hanging block
g = 9.8  # g
x = 0.05  # length from wall to end of support cable
y = sqrt(L ** 2 - x ** 2)  # height of wall from rod to start of support cable

# set up the scene
scene = canvas(title='Statics Lab', width=1200, height=800, center=vec(0.5, 0, 0), range=10, background=vec(0, 0, 0), )

# draw coordinate axes
x_axis = cylinder(pos=vec(-10, 0, 0), axis=vec(20, 0, 0), radius=0.05)
y_axis = cylinder(pos=vec(0, -10, 0), axis=vec(0, 20, 0), radius=0.05)
z_axis = cylinder(pos=vec(0, 0, -10), axis=vec(0, 0, 20), radius=0.05)

# create all of the objects in the scene
the_wall = box(pos=vec(-0.07, 0, 0), length=0.5, width=0.25, height=8, opacity=0.5)
pivot = sphere(pos=vec(0, 0, 0), radius=0.25, color=color.purple)
rod = cylinder(pos=vec(0, 0, 0), axis=vec(L, 0, 0), radius=0.05, color=color.cyan)
hanging_block = box(pos=rod.pos + rod.axis - vec(0, 1.5, 0))
hanging_block_string = cylinder(pos=rod.pos + rod.axis, axis=hanging_block.pos - (rod.pos + rod.axis), radius=0.05)
support_cable = cylinder(pos=vec(0, y, 0), axis=vec(x, -y, 0), radius=0.05)

# scale all the arrows down by this much so it's not going crazy
arrow_scale = 0.05

# draw arrows for all the forces
rod_weight = arrow(pos=rod.pos + 0.5 * rod.axis, axis=arrow_scale * vec(0, -m * g, 0), color=color.magenta)
hanging_block_weight = arrow(pos=rod.pos + rod.axis, axis=arrow_scale * vec(0, -M * g, 0), color=color.magenta)
tension = arrow(pos=support_cable.pos, axis=arrow_scale * vec((-L / y) * (M + m / 2) * g, (L / x) * (M + m / 2) * g, 0),
                color=color.blue)
reaction = arrow(pos=pivot.pos, axis=-1 * (tension.axis + rod_weight.axis + hanging_block_weight.axis),
                 color=color.green)

# create plot
tension_x_plot = graph(title='T vs x', xtitle='<em>x</em> (m)', ytitle='<em>T</em> (N)', width=500)
curve = gcurve(color=color.blue)

# animate as x changes from 0.05m to 0.95m
dx = 0.001
sim_speed = 0.5

while 0.05 <= x < 0.95:
    rate(sim_speed / dx)

    # set new y
    y = sqrt(L ** 2 - x ** 2)

    # update the support cable
    support_cable.pos.x = x
    support_cable.axis = vec(x, -y, 0)

    # update the tension
    tension.pos = support_cable.pos
    tension.axis = arrow_scale * vec((-L / y) * (M + m / 2) * g, (L / x) * (M + m / 2) * g, 0)

    # update the reaction force
    reaction.axis = -1 * (tension.axis + rod_weight.axis + hanging_block_weight.axis)

    # plot the data for this iteration
    curve.plot(x, mag(tension.axis/arrow_scale))

    # increment x
    x += dx
