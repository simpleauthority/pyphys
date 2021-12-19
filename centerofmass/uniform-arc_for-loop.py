from vpython import *

# coordinate axes
x_axis = cylinder(pos=vec(-5, 0, 0), axis=vec(10, 0, 0), radius=0.05)
y_axis = cylinder(pos=vec(0, -5, 0), axis=vec(0, 10, 0), radius=0.05)
z_axis = cylinder(pos=vec(0, 0, -5), axis=vec(0, 0, 10), radius=0.05)

mu = 1.00  # linear mass density of arc
R = 2.0  # radius of arc
N = 5  # how many slices of the arc to take
theta_min_deg = 0  # min arc angle in degrees
theta_max_deg = 180  # max arc angle in degrees
theta_min = radians(theta_min_deg)  # min arc angle in radians
theta_max = radians(theta_max_deg)  # max arc angle in radians

# determine angular increment and arclength increment
dtheta = (theta_max - theta_min) / N  # compute angular increment in radians
ds = R * dtheta  # arclength of a single arc slice

# initialize numerator of com formula
numerator = vec(0, 0, 0)
# initialize denominator of com formula
denominator = 0
# initialize list for organizational purposes
arc = []
# initialize increment parameter
i = 0

for theta in arange(theta_min, theta_max, dtheta):
    rate(2)

    # draw each chunk of the rod as a sphere
    ball = sphere(pos=R * vec(cos(theta + dtheta / 2), sin(theta + dtheta / 2), 0), radius=0.45 * ds, opacity=0.35)

    # define and compute mass of slice (UNFINISHED)

    # define attribute dm (differential mass) for each slice
    # this computes the equation dm = (linear mass density) * dx
    ball.dm = mu * ds

    # add each chunk into the list named rod
    # useful if we need to change aspects of rod later
    arc.append(ball)

    # sum m_i * x_i in 3D
    numerator += arc[i].dm * arc[i].pos

    # figure out the total mass
    denominator += arc[i].dm

    i += 1

print(f"total mass {denominator}")

# mtot_th = mu * rod_length
# mtot_pdiff = ((denominator - mtot_th) / mtot_th) * 100
# print(f"total mass percent difference {mtot_pdiff}%")

com = numerator / denominator
print(f"center of mass is located at {com}")

# # for a rod of uniform mass, the com should (theoretically) be directly at the center
# com_th_x = (rod_visual_guide.pos.x + rod_length / 2)
# com_x_pdiff = ((com.x - com_th_x) / com_th_x) * 100
# print(f"x center of mass percent difference {com_x_pdiff}%")

com_ball = sphere(pos=com, radius=0.5, color=vec(0.85, 0, 0))
