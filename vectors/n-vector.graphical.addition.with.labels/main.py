from vpython import *


# Define a class associating a vector and a label
class LabelledVector:
    def __init__(self, value: vec, label: str = ""):
        self.value = value
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
            last = LabelledArrow(start, current.value, label=current.label).draw()
        else:
            last = LabelledArrow(last.pos + last.axis, current.value, label=current.label).draw()

    LabelledArrow(pos=start, axis=result, label="R", color=vector(255, 255, 255)).draw()

    return result


# Draw coordinate axes
x_axis = cylinder(pos=vector(-10, 0, 0), axis=vector(20, 0, 0), radius=0.05)
text(text='x', pos=x_axis.pos + x_axis.axis)
y_axis = cylinder(pos=vector(0, -6, 0), axis=vector(0, 12, 0), radius=0.05)
text(text='y', pos=y_axis.pos + y_axis.axis)
z_axis = cylinder(pos=vector(0, 0, -6), axis=vector(0, 0, 12), radius=0.05)
text(text='z', pos=z_axis.pos + z_axis.axis)

# Modify these vectors
A = vector(0, -5, 0)
B = vector(0, 0, -15)
C = vector(10, 0, 0)
D = vector(0, 3, 5)

# Call this function to graphically add the vectors
# LabelledVector's arguments are the vector and a label
sum_vectors(LabelledVector(A, "A"), LabelledVector(B, "B"), LabelledVector(C, "C"), LabelledVector(D, "D"))
