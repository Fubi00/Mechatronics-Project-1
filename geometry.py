import sympy as sp

# This file is for establishing the geometry of the forklift and its components.
# and this will be used in further calculations.


# Points of interest in the forklift geometry
points = {
    "A": sp.Matrix([0, 0]),  # Center of the front wheel
    "F": sp.Matrix([-1.32, 0]),  # Center of the rear wheel
    "G_main": sp.Matrix([-1.05, 0.25]),  # Center of mass for the main body
    "B": sp.Matrix([0.15, -0.15]),  # Connecting point for the tower and the main body
    "D": sp.Matrix([-0.11, 0.42]),  # Bottom of the tilting cylinder

    "E": sp.Matrix([0.22, 0.5]),  # Top of the tilting cylinder
    "H": sp.Matrix([0.35, 0.15]),  # Preliminary point for the massenter for the lifting mechanism
    "I": sp.Matrix([0.95, 0.35]),  # Preliminary point for the massenter for the load

    "R_G": sp.Matrix([0.4, 0.05]),  # Lower contact point between the trolly and the tower
    "R_H": sp.Matrix([0.4, 0.35]),  # Upper contact point between the trolly and the tower
    "R_I": sp.Matrix([0.4, 0.35]),  # Upper contact point between the trolly and the forks
    "R_J": sp.Matrix([0.4, 0.05]),  # Lower contact point between the trolly and the forks
    
    "G_load": sp.Matrix([0, 0]),  # Center of mass for the load
    "G_forks": sp.Matrix([0, 0]),  # Center of mass for the lifting mechanism
    "G_trolly": sp.Matrix([0, 0]),  # Center of mass for the trolly
    "G_tower": sp.Matrix([0, 0]),  # Center of mass for the tower
    "G_mainCylinder": sp.Matrix([0, 0]),  # Center of mass for the main cylinder
    "G_tiltingCylinder": sp.Matrix([0, 0]),  # Center of mass for the tilting cylinder
}

