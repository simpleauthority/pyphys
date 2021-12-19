from vpython import *

# assumptions
R = 5
dy = dx = 0.15

# givens
x_min = -R
x_max = R
y_min = -R
y_max = R

# draw coordinates
line_x = cylinder(pos=vec(-R - 2, 0, 0), axis=vec(2*R + 4, 0, 0), radius=0.05)
line_y = cylinder(pos=vec(0, -R - 2, 0), axis=vec(0, 2*R + 4, 0), radius=0.05)

# reduce output visualization window height
# should make it easier to read print statements
scene.height = 200

# square diagonal = R = sqrt(2) * s => s = R/sqrt(2)
square_side = R / sqrt(2)

# draw circle with missing square
for x in arange(x_min, x_max, dx):
    for y in arange(y_min, y_max, dy):
        if y ** 2 + x ** 2 <= R ** 2:
            # this was fun to figure out! the square is in the first quadrant and goes from (0,0) to (s,s)
            # thus if any sphere would fall inside this, then they should not be drawn
            if not (0 <= x <= square_side and 0 <= y <= square_side):
                ball = sphere(pos=vec(x + dx/2, y + dy/2, 0), opacity=0.4, radius=0.2)

# mass_circle = pi * R^2 * sigma
# com_circle = (0,0)
# mass_square = square_side^2 * sigma
# com_square = (s/2, s/2)
# com_shape = ((mass_circle * com_circle) - (mass_square * com_square)) / (mass_circle - mass_square) ; sigma drops out of equation!
# com_circle = (0,0) => com_shape = (0-(mass_square * com_square)) / (mass_circle - mass_square)
mass_circle = pi * (R ** 2)
mass_square = square_side ** 2
com_square = vec(square_side / 2, square_side / 2, 0)
com_shape = (-(mass_square * com_square)) / (mass_circle - mass_square)  # this is numer/denom, just not using variables for them

# center the camera on the com
scene.center = com_shape

# show the com visually
com_indicator = sphere(pos=com_shape, radius=0.25, color=color.purple)

# print out the answer to the question
print(f"center of mass for thin plate with square cutout: {com_shape}")
print(f"x center of mass (rounded to 3 decimal places): {com_shape.x:.3f}")

# compute theoretical COM.x
# per solution, COM should be -0.0669 * R in either dimension
COM_th = vec(-0.0669 * R, -0.0669 * R, 0)
p_diff_COMx = (com_shape.x - COM_th.x) / COM_th.x * 100
print(f"% diff for COM_x = {p_diff_COMx:.3f}")
