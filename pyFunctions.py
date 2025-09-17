import sympy as sp
from geometry import *

# Functions to manipulate and retrieve point data
def set_point(name, x, y):
    """Set the coordinates of a point."""
    if name in points:
        points[name] = sp.Matrix([x, y])
    else:
        raise ValueError(f"Point {name} is not defined.")
    
def get_point(name):
    """Get the coordinates of a point."""
    if name in points:
        return points[name]
    else:
        raise ValueError(f"Point {name} is not defined.")

def vector(point1, point2):
    """Calculate the vector from point1 to point2."""
    return get_point(point2) - get_point(point1)

def vec_B(point):
    """Calculate the vector from point B to another point."""
    return vector("B", point)

# Function for moment calculation
def Mz(point, force):
    """Calculate the moment around the z-axis at a given point due to a force."""
    return point[0] * force[1] - point[1] * force[0]