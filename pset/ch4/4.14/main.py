from vpython import *


def get_arrow_axis(obj, arrow_type, arrow_direction):
    axes = {
        'v': {
            'x': vec(obj.v_x, 0, 0),
            'y': vec(0, obj.v_y, 0)
        },
        'a': {
            'x': vec(obj.a_x, 0, 0),
            'y': vec(0, obj.a_y, 0)
        }
    }

    return axes[arrow_type][arrow_direction]


def create_arrows(obj):
    v_color = vec(0.24, 0.92, 0.42)
    a_color = vec(0.92, 0.89, 0.12)

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
x_axis = cylinder(pos=vec(0, 0, 0), axis=vec(60, 0, 0), color=vec(0.8, 0.82, 0.82), radius=0.1)
label(pos=x_axis.pos + x_axis.axis, text='<i>x</i>', box=False)

y_axis = cylinder(pos=vec(0, 0, 0), axis=vec(0, 20, 0), color=vec(0.8, 0.82, 0.82), radius=0.1)
label(pos=y_axis.pos + y_axis.axis, text="<i>y</i>", box=False)

# Set up scene
scene.background = vec(0.314, 0.314, 0.314)
scene.camera.pos = vec(30, 10, -80)

#
# PROBLEM 4.14 SOLVED BELOW
#

# Define projectile object
ball = sphere(pos=vec(0, 10, 0), color=vec(0, 0, 1), trail_color=vec(1, 0, 0.82), radius=0.5, make_trail=True)

# Set our known information
ball.vi_mag = 19.6
ball.vi_dir = radians(30.0)
ball.vi_x = ball.vi_mag * cos(ball.vi_dir)
ball.vi_y = ball.vi_mag * sin(ball.vi_dir)
ball.vf_x = ball.vi_x
ball.v_x = ball.vi_x
ball.v_y = ball.vi_y
ball.a_x = 0
ball.a_y = -9.8
ball.dy = -10

# Let's first find vf_y
# (vfy)^2 = (viy)^2 + 2(ay)(y)
# vf = -sqrtA((viy)^2+2(ay)(y)), negative as we are heading down
ball.vf_y = -sqrt((ball.vi_y ** 2) + (2 * ball.a_y * ball.dy))

# Now let's find t so we know when it hits the ground
# vfy = viy + at => vfy-viy = at => t = (vfy-viy)/a
ball.flight_time = (ball.vf_y - ball.vi_y) / ball.a_y

# Now, let's find the range of the projectile by using the flight time with the other known information
# x = (vi_x)(t) + (1/2)(a_x)(t^2) => since a_x = 0, x = (vi_x)(t)
ball.dx = ball.vi_x * ball.flight_time

print(f"4.14.a, range of projectile: {ball.dx:.1f} meters.")

# Next to last, let's get the final velocity into polar form
ball.vf_mag = sqrt((ball.vf_x ** 2) + (ball.vf_y ** 2))
ball.vf_dir = degrees(atan(ball.vf_y / ball.vf_x))

print(f"4.14.b, impact velocity in polar form: {ball.vf_mag:.1f} m/s directed at {ball.vf_dir:.0f} degrees to the horizontal.")

#
# PROBLEM 4.14 SOLVED ABOVE
#

# Set up velocity and acceleration tracking arrows on object
arrows = create_arrows(ball)

# Create a graph of the x component of velocity vs time
graph(width=600, height=225, title="<b><i>v<sub>x</sub> vs <i>t</i></b>", xtitle="<i>t</i> (s)",
      ytitle="<i>v<sub>x</sub></i> (m)", foreground=vec(0, 0, 0), background=vec(1, 1, 1))
v_xt_curve = gcurve(color=vec(0, 0.4, 1))

# Create a graph of the y component of velocity vs time
graph(width=600, height=225, title="<b><i>v<sub>y</sub> vs <i>t</i></b>", xtitle="<i>t</i> (s)",
      ytitle="<i>v<sub>y</sub></i> (m)", foreground=vec(0, 0, 0), background=vec(1, 1, 1))
v_yt_curve = gcurve(color=vec(0, 0.4, 1))

# Define simulation variables
t = 0  # time
dt = 0.0001  # time step
sim_speed = 0.25  # speed of simulation used in calculating FPS

while ball.pos.y > 0 and t < ball.flight_time:
    rate(sim_speed / dt)

    # Update velocity and position
    ball.v_x += ball.a_x * dt  # update velocity in the x (vf_x = vi_x + a_xt)
    ball.v_y += ball.a_y * dt  # update velocity in the y (vf_y = vi_y + a_yt)
    ball.pos.x += ball.v_x * dt  # update position in the x (xf = xi + v_xt)
    ball.pos.y += ball.v_y * dt  # update position in the y (yf = yi + v_yt)

    # Update velocity and acceleration indicators on ball
    tick_arrow(ball, 'v', 'x')
    tick_arrow(ball, 'v', 'y')
    tick_arrow(ball, 'a', 'x')
    tick_arrow(ball, 'a', 'y')

    # Plot v_y and v_x vs time
    v_xt_curve.plot(t, ball.v_x)
    v_yt_curve.plot(t, ball.v_y)

    # Increment time
    t += dt

# Calculate percent difference from the theoretical (after loop to use experimental data)
vf_mag_th = ball.vf_mag
vf_mag_exp = mag(vec(ball.v_x, ball.v_y, 0))
percent_diff = ((vf_mag_exp - vf_mag_th) / vf_mag_th) * 100

print(f"Percent difference: {percent_diff}%")
