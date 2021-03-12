from vpython import *


# Define a class associating a vector and a label
class LabelledVector:
    def __init__(self, value: vec, color: vec = vector(1, 0, 0), label: str = ""):
        self.value = value
        self.color = color
        self.label = label


# Define a class associating position, color, and a label for an arrow
# as well as a functionality for drawing
class LabelledArrow:
    def __init__(self, pos: vec, axis: vec, color: vec = vector(1, 0, 0), label: str = ""):
        self.pos = pos
        self.axis = axis
        self.color = color
        self.label = label

    def draw(self):
        print(f'Drawing arrow {self.label} from {self.pos} to {self.axis}')
        label(pos=((self.pos + self.axis) - self.axis / 2), text=self.label)
        return arrow(pos=self.pos, axis=self.axis, color=self.color)


# Define a function to sum a set of vectors
def sum_vectors(*args: LabelledVector):
    start = vector(0, 0, 0)
    result = vector(0, 0, 0)

    last = None
    for current in args:
        result = result + current.value

        if last is None:
            last = LabelledArrow(start, current.value, color=current.color, label=current.label).draw()
        else:
            last = LabelledArrow(last.pos + last.axis, current.value, color=current.color, label=current.label).draw()

    return result


# Draw coordinate axes (R3); (y, z, x)
x_axis = cylinder(pos=vector(0, 0, -6), axis=vector(0, 0, 12), radius=0.05)
text(text='x', pos=x_axis.pos + x_axis.axis)
y_axis = cylinder(pos=vector(-10, 0, 0), axis=vector(20, 0, 0), radius=0.05)
text(text='y', pos=y_axis.pos + y_axis.axis)
z_axis = cylinder(pos=vector(0, -6, 0), axis=vector(0, 12, 0), radius=0.05)
text(text='z', pos=z_axis.pos + z_axis.axis)

# Problem info
print("Problem 3.16. Given vector A has magnitude 10 and is angled 20 degrees from the z axis onto the yz-plane, and "
      "vector B has magnitude 20 and is angled 30 degrees from the y axis onto the xy plane. We are told a third "
      "vector C returns to the origin. We proceed to find A and B in cartesian form, and then find C.\n")

# Solve problem 3.16 (using nonstandard (y, z, x) coordinates!)
A_mag = 10
A_theta = radians(20)  # from z axis
A_y = -(A_mag * sin(A_theta))  # negative due angle from z
A_z = A_mag * cos(A_theta)
A = vector(A_y, A_z, 0)
print(f"A = {A}")

B_mag = 20
B_theta = radians(30)  # from y axis
B_x = B_mag * sin(B_theta)
B_y = B_mag * cos(B_theta)
B = vector(B_y, 0, B_x)
print(f"B = {B}")

# A + B + C = origin => C = origin - (A + B)
origin = vector(0, 0, 0)
C = origin - (A + B)
C_mag = sqrt(pow(C.y, 2) + pow(C.z, 2) + pow(C.x, 2))
C_theta_z = degrees(acos(-1 * hat(C).y))
print(f"C = {C} = {C_mag:.2f} at {C_theta_z:.2f} degrees to the negative z-axis.")

print("\n")

# Call this function to graphically add the vectors
# LabelledVector's arguments are the vector and a label
result = sum_vectors(LabelledVector(A, vector(12 / 255, 245 / 255, 116 / 255), "A"),
                     LabelledVector(B, vector(1, 186 / 255, 73 / 255), "B"),
                     LabelledVector(C, vector(239 / 255, 91 / 255, 91 / 255), "C"))
print("\nVector Sum:", result)
