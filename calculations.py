"""
This sctipt contains functions and data to perform various calculations in our worck in designing the lifting mechanism for an forcklift.
The project is part of the course MAS238 "Mekkatronikkprosjekt 1" at the University of Agder (UiA).
"""

""" Created by: [Fabian A. Alsaker, Julian F. Idsø, Daniel, Nasar, 20-08-2025] """

import math
import sympy as sp
import numpy as np
from geometry import *
from pyFunctions import *


# Constants for gyometry and physics
g = 9.81  # m/s^2, acceleration due to gravity

# Masses of the components
mass_loade = 1500  # kg
mass_mainBody = 3500  # kg
mass_liftingMechanism = 300  # kg
mass_trolly = 0  # kg
mass_fork = 0  # kg
mass_cylinder = 0  # kg
mass_tower = 0  # kg

# Reaction forces and weights of the system
A_x, A_y = sp.symbols('A_x A_y')
A = sp.Matrix([A_x, A_y]) # Reaction force at point A (front wheel)
B_x, B_y = sp.symbols('B_x B_y')
B = sp.Matrix([B_x, B_y])  # Reaction force at point B (tower to main body)
D_x, D_y = sp.symbols('D_x D_y')
D = sp.Matrix([D_x, D_y])  # Force from the tilting cylinder at point D
F_x, F_y = sp.symbols('F_x F_y')
F = sp.Matrix([F_x, F_y])  # Reaction force at point F (rear wheel)
G_main = sp.Matrix([0, mass_mainBody * g])  # Weight of the main body acting at G_main
G_lift = sp.Matrix([0, mass_liftingMechanism * g])  # Weight of the lifting mechanism acting at G_lift
G_load = sp.Matrix([0, mass_loade * g])  # Weight of the load acting at G_load

# Preliminary calculations with assumed starting values
sum_forces_x = sp.Eq(A[0] - B[0] - D[0], 0) # Sum of forces in x-direction
sum_forces_y = sp.Eq(A[1] - B[1] - D[1] + F[1] - G_main[1], 0) # Sum of forces in y-direction
# Sum of moments around point B
sum_moment_B = sp.Eq(
    Mz(vec_B("A"), A) + 
    Mz(vec_B("D"), D) + 
    Mz(vec_B("F"), F) + 
    Mz(vec_B("G_main"), G_main), 
    0
)