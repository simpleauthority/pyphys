from vpython import *

rod_length = 5
x_min = 0
x_max = x_min + rod_length
mu = 1.00  # linear mass density
N = 5  # how many slices of the rod to take
dx = rod_length / N  # width of one tiny chunk of the rod

# create a rod with length rod_length, left end at origin
rod_visual_guide = cylinder(pos=vec(x_min, 0, 0), axis=vec(rod_length, 0, 0), opacity=0.15, radius=0.5)

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

for x in arange(x_min, x_max, dx):
    rate(2)

    # draw each chunk of the rod as a sphere
    ball = sphere(pos=vec(x + dx/2, 0, 0), radius=rod_visual_guide.radius, opacity=0.35)

    # define attribute dm (differential mass) for each slice
    # this computes the equation dm = (linear mass density) * dx
    ball.dm = mu * dx

    # add each chunk into the list named rod
    # useful if we need to change aspects of rod later
    rod.append(ball)

    # sum m_i * x_i in 3D
    numerator += rod[i].dm * rod[i].pos

    # figure out the total mass
    denominator += rod[i].dm

    i += 1

print(f"total mass {denominator}")

mtot_th = mu * rod_length
mtot_pdiff = ((denominator - mtot_th) / mtot_th) * 100
print(f"total mass percent difference {mtot_pdiff}%")

com = numerator / denominator
print(f"center of mass is located at {com}")

# for a rod of uniform mass, the com should (theoretically) be directly at the center
com_th_x = (rod_visual_guide.pos.x + rod_length / 2)
com_x_pdiff = ((com.x - com_th_x) / com_th_x) * 100
print(f"x center of mass percent difference {com_x_pdiff}%")
