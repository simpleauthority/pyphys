from vpython import *


def get_arrow_axis(obj, arrow_type, arrow_direction):
    axes = {
        'v': {
            'x': vec(obj.v.x, 0, 0),
            'y': vec(0, obj.v.y, 0)
        },
        'a': {
            'x': vec(obj.a.x, 0, 0),
            'y': vec(0, obj.a.y, 0)
        }
    }

    return axes[arrow_type][arrow_direction]


def create_arrows(obj):
    v_color = vec(0, 0.4, 1)
    a_color = vec(2, 0, 1)

    arrow_vx = arrow(pos=obj.pos, color=v_color)
    arrow_vx.axis = get_arrow_axis(obj, 'v', 'x')

    arrow_vy = arrow(pos=obj.pos, color=v_color)
    arrow_vy.axis = get_arrow_axis(obj, 'v', 'y')

    arrow_ax = arrow(pos=obj.pos, color=a_color)
    arrow_ax.axis = get_arrow_axis(obj, 'a', 'x')

    arrow_ay = arrow(pos=obj.pos, color=a_color)
    arrow_ay.axis = get_arrow_axis(obj, 'a', 'y')

    return {
        'v': {
            'x': arrow_vx,
            'y': arrow_vy
        },
        'a': {
            'x': arrow_ax,
            'y': arrow_ay
        }
    }


def tick_arrow(obj, arrow_type, arrow_direction):
    tickable = arrows[arrow_type][arrow_direction]
    tickable.pos = obj.pos
    tickable.axis = get_arrow_axis(obj, arrow_type, arrow_direction)


# Create coordinate axes
x_axis = cylinder(pos=vec(-5, 0, 0), axis=vec(10, 0, 0), radius=0.05)
label(pos=x_axis.pos + x_axis.axis, text='<i>x</i>', box=False)

y_axis = cylinder(pos=vec(0, -5, 0), axis=vec(0, 10, 0), radius=0.05)
label(pos=y_axis.pos + y_axis.axis, text="<i>y</i>", box=False)

# Define projectile object
cow = sphere(pos=vec(0, 0, 0), color=vec(0, 0, 1), trail_color=vec(0, 0, 1), v=vec(3, -4, 0), a=vec(-1, 2, 0), radius=0.5, make_trail=True)

# Set up velocity and acceleration tracking arrows on object
arrows = create_arrows(cow)

# Create a graph of the y component of velocity versus time
graph(width=600, height=225, title="<b><i>v<sub>y</sub> vs <i>t</i></b>", xtitle="<i>t</i> (s)", ytitle="<i>v<sub>y</sub></i> (m)", foreground=vec(0, 0, 0), background=vec(1, 1, 1))
v_yt_curve = gcurve(color=vec(0, 0.4, 1))

# Define simulation variables
t = 0  # time
dt = 0.1  # time step
sim_speed = 1  # speed of simulation used in calculating FPS

while t < 5:
    rate(sim_speed / dt)

    cow.v += cow.a * dt  # update velocity (vf = vi + at)
    cow.pos += cow.v * dt  # update position (xf = xi + vt)

    tick_arrow(cow, 'v', 'x')
    tick_arrow(cow, 'v', 'y')
    tick_arrow(cow, 'a', 'x')
    tick_arrow(cow, 'a', 'y')

    v_yt_curve.plot(t, cow.v.y)

    t += dt
