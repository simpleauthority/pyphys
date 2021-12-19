from vpython import *

G = 6.67e-11  # Universal gravitation constant


def compute_grav(m1, m2, r):
    return ((G * m1 * m2) / (mag(r) ** 2)) * -hat(r)


def compute_pe(m1, m2, r):
    return -((G * m1 * m2) / mag(r))


# draw a set of coordinate axes
x_axis = cylinder(pos=vec(-16000, 0, 0), axis=vec(32000, 0, 0), radius=700)
y_axis = cylinder(pos=vec(0, -16000, 0), axis=vec(0, 32000, 0), radius=700)

scale_factor = 0.000025  # used to scale force arrows (to make arrows visible)

planet = sphere(color=color.orange, radius=6370)
satellite = sphere(color=color.cyan, radius=1500)

# set initial rock positions
planet.pos = vec(0, 0, 0)
satellite.pos = vec(0, 14000, 0)

# set rock masses
planet.m = 5.972e24  # mass of earth
satellite.m = 100  # mass of CubeSat

# calculate center-to-center distances for the earth-satellite system
r_planet_to_sat = satellite.pos - planet.pos

# set initial momentum for satellite
satellite.p = vec(0, 0, 0)
# mv^2/r = GmM/r^2 => v^2 = GM/r => v = sqrt(GM/r) => mv = m*sqrt(GM/r) => p = m*sqrt(GM/r)
satellite.p.x = satellite.m * sqrt((G * planet.m) / mag(r_planet_to_sat))

# calculate initial forces
F_planet_on_sat = compute_grav(planet.m, satellite.m, r_planet_to_sat)

# create initial force arrows
F_planet_on_sat_arrow = arrow(pos=satellite.pos, axis=scale_factor * F_planet_on_sat, color=satellite.color)

# Compute the potential energy
U_net = compute_pe(planet.m, satellite.m, r_planet_to_sat)

# Print info
print(f'The gravitational FORCE is {F_planet_on_sat} N.')
print(f'The MAGNITUDE of gravitational force ON the satellite is {mag(F_planet_on_sat):.2f} N.')
print(f'The gravitational potential energy is {U_net:.1f} J.')

# Create plot of radius vs time
radius_vs_time_plot = graph(width=640, height=300, title='<b><i>radius</i> (m) vs <i>time</i> (s)</b>',
                            xtitle='<i>t</i> (s)', ytitle='<i>radius</i> (m)', foreground=color.black,
                            background=color.white)
radius_vs_time_curve = gcurve(color=color.purple)

# Animate
# Loop parameters
t = 0
dt = 0.005

# Wait to click before starting
scene.waitfor('click')

# Loop
while t < 1e20:
    # set fps
    rate(25)

    # recalculate center-to-center distances for the earth-satellite system
    r_planet_to_sat = satellite.pos - planet.pos

    # record data in plot
    radius_vs_time_curve.plot(t, mag(r_planet_to_sat))

    # recalculate gravity
    F_planet_on_sat = compute_grav(planet.m, satellite.m, r_planet_to_sat)

    # update momentum of satellite
    satellite.p += F_planet_on_sat * dt

    # update positions
    satellite.pos += (satellite.p / satellite.m) * dt

    # update arrows
    F_planet_on_sat_arrow.pos = satellite.pos
    F_planet_on_sat_arrow.axis = scale_factor * F_planet_on_sat

    # update time
    t += dt
