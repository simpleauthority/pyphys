from vpython import *

M = 10
L = 6
H = 3
x_min = 0
x_max = x_min + L
y_min = 0
y_max = y_min + H
dx = 0.2
dy = dx

# draw coordinates
line_x = cylinder(pos=vec(-2, 0, 0), axis=vec(L + 4, 0, 0), radius=0.05)
line_y = cylinder(pos=vec(0, -2, 0), axis=vec(0, H + 4, 0), radius=0.05)

# reduce output visualization window height
# should make it easier to read print statements
scene.height = 200

numer = vec(0, 0, 0)  # initialize NUMERATOR of center of mass formula
denom = 0  # initialize DENOMINATOR of center of mass formula
plate = []  # initialize list for organizational purposes
N = 0  # counter for total number of balls drawn

# draw triangular plate
for x in arange(x_min, x_max, dx):
    for y in arange(y_min, y_max, dy):
        if y <= (H/L)*x:
            ball = sphere(pos=vec(x + dx/2, y + dy/2, 0), opacity=0.4)
            plate.append(ball)
            N += 1

dm = M / N
print(f"Total mass = {M}")
print(f"Total number of balls = {N}")
print(f"Mass per ball = {dm:.3f}")

# note: now that you know the mass for each ball
# compute the COM with a single FOR loop
for ball in plate:
    numer += dm * ball.pos
    denom += dm

# compute the center of mass
# notice this gives (Sum of x_i*m_i)/(total mass)
COM = numer / denom
print(f"Center of mass is at {COM}")
COM_indicator = sphere(pos=COM, color=vec(1, 0.2, 0.8))
COM_indicator.radius = 0.5

# this line of code centers the camera on the COM
scene.center = COM

# compute theoretical COM.x
# for triangular plate, should be 1/3 from the fat end
COM_th = vec(2 * L / 3, 1 / 3 * H, 0)
p_diff_COMx = (COM.x - COM_th.x) / COM_th.x * 100
print(f"% diff for COM_x = {p_diff_COMx:.3f}")

# compute theoretical COM.y
# for triangular plate, should be 1/3 from the fat end
p_diff_COMy = (COM.y - COM_th.y) / COM_th.y * 100
print(f"% diff for COM_y = {p_diff_COMy:.3f}")
