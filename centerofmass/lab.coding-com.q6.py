from vpython import *


# calculate linear mass density with given expression
def mu(x):
    return 5 * cos(x / 4) ** 2


rod_length = 5.2  # length of rod
x_min = -1.9  # left end x position
x_max = x_min + rod_length  # right end x position
N = 22  # number of slices to make
dx = rod_length / N  # x differential

# create a rod with length L, left end at x_min
rod_visual_guide = cylinder(pos=vec(x_min, 0, 0), axis=vec(x_max, 0, 0), opacity=0.15, radius=0.5)

# coordinate axes
x_axis = cylinder(pos=vec(-6, 0, 0), axis=vec(12, 0, 0), radius=0.05)
y_axis = cylinder(pos=vec(0, -6, 0), axis=vec(0, 12, 0), radius=0.05)

# initialize numerator of com formula
numerator = vec(0, 0, 0)

# initialize denominator of com formula
denominator = 0

# initialize list for organizational purposes
rod = []

# initialize increment parameter
i = 0

# initialize counter for max mass
dm_max = 0

for x in arange(x_min, x_max, dx):
    rate(2)

    ball_pos_x = (x + dx / 2) if x == x_min else (x + dx)

    # draw each chunk of the rod as a sphere
    ball = sphere(pos=vec(ball_pos_x, 0, 0), radius=0.5)

    # define attribute dm (differential mass) for each slice
    # this computes the equation dm = (linear mass density) * dx
    ball.dm = mu(ball_pos_x) * dx

    if ball.dm > dm_max:
        dm_max = ball.dm
        print(dm_max)

    # add each chunk into the list named rod
    # useful if we need to change aspects of rod later
    rod.append(ball)

    # sum m_i * x_i in 3D
    numerator += rod[i].dm * rod[i].pos

    # figure out the total mass
    denominator += rod[i].dm

    i += 1

for ball in rod:
    ball.color = vec(1, 0, 0)
    ball.opacity = ball.dm / dm_max

com = numerator/denominator
print(f"Center of mass: {com}")
print(f"Center of mass (x): {com.x:.4f} meters")

com_indicator = sphere(pos=com, color=color.purple, radius=0.5)