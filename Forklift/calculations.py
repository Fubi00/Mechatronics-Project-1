#!/usr/bin/env python3
"""
This sctipt contains functions and data to perform various calculations in our worck in designing the lifting mechanism for an forcklift.
The project is part of the course MAS238 "Mekkatronikkprosjekt 1" at the University of Agder (UiA).
"""

""" Created by: [Fabian A. Alsaker, Julian F. Idsø, Daniel, Nasar, 20-08-2025] """

import math
import sympy as sp


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


# Geometry of the forklift body
# Posision of the connection points and mass centers using a global cordinate system with the origin at the front wheel contact point with the ground
xA, yA, xB, yB, xC1, yC1, xC2, yC2, xD, yD, xE, yE, xF, yF, xG, yG, xH, yH, xI, yI, xJ, yJ, xK, yK, xL, yL, xN1, yN2, xN2, yN2, xR, yR = sp.symbols('xA yA xB yB xC1 yC1 xC2 yC2 xD yD xE yE xF yF xG yG xH yH xI yI xJ yJ xK yK xL yL xN1 yN1 xN2 yN2 xR yR')
A = (xA, yA)
B = (xB, yB)
C1 = (xC1, yC1)
C2 = (xC2, yC2)
D = (xD, yD)
E = (xE, yE)
F = (xF, yF)
G = (xG, yG)
H = (xH, yH)
I = (xI, yI)
J = (xJ, yJ)
K = (xK, yK)
L = (xL, yL)
N1 = (xN1, yN1)
N2 = (xN2, yN2)
R = (xR, yR)
A_num = (0, 0)  # Front wheel center
F_num = (length_wheelBase, 0)  # Rear wheel center
G_num = (length_massCenterMain, hight_massCenterMain)  # Mass center of the main body
B_num = (length_frontWheelToHingePoint, hight_hingePoint)  # Hinge point between the main body and the tower
D_num = (length_frontWheelToD, hight_pointD)  # Connection point for the tilting cylinder to the main body
C1_num = ()

# Lengths in x-direction
length_wheelBase = 1.32  # m  L_W                                       Between the front and rear wheels / point A and F
length_frontWheelToHingePoint = 0.4  # m  L_BF                          From the front wheel to the hinge point / point A and B
length_massCenterMain = 1.05  # m  L_G                                  From the front wheel to the mass center of the main body / point A and G
length_frontWheelToD = 0.4  # m  L_D                                    From the front wheel to the point D / point A and D

# Heights in y-direction from point A
hight_hingePoint = -0.2  # m  y_B                                       From the front wheel to the hinge point / point A and B
hight_massCenterMain = 0.25  # m  H_G                                   From the front wheel to the mass center of the main body / point A and G
hight_pointD = 0.42  # m  y_D                                           from the front wheel to the point D / point A and D

# Radius of the wheels
radus_wheel = 0.23  # m  R_W

# Geometry of the lifting mechanism
# Lenghts in x-direction of the lifting mechanism / Seprate cordinate system for tilting mechanism
length_hingePointToE = 0.4  # m  L_BC                                   From the hinge point to the point E / point B and C 
length_hingePointToCC = 0  # m x`c                                      From the hinge point to the CC axis / point C and axis CC
length_hingePointToMassLift = 0.4  # m  L_BC                            From the hinge point to the mass center of the lifting mechanism / point B and H
length_hingePointToMassLoad = 0  # m  L_BC                              From the hinge point to the mass center of the load / point B and I
length_forks = 1.2 # m  L_FK                                            Length of the forks

# Heights in y-direction of the lifting mechanism / Seprate cordinate system for tilting mechanism
hight_massCenterLiftingMechanismFromFork = 0.15  # m  H_TTF             From the hinge point to the mass center of the lifting mechanism / point B and H
hight_massCenterLoadFromFork = 0 # m  H_PL                              From the hinge point to the mass center of the load / point B and I
hight_fork= 0  # m  y`FK                                                From the hinge point to the underside of the forks / point B and FK

# Other geometry parameters
trolly_width = 0.8  # m  W_T                                            Width of the trolly


# Contraints for the engineering design

# Safe working load
safe_working_load = 1500  # kg  SWL                                     
# Maximum height of the forks
max_height_forks = 1.8  # m  H_FK_MAX  
# Hoisting time
hoisting_time = 6  # +- s  T_HOISTING
# Tilting angle
tilting_angle = 5  # deg  ALPHA_TILTING                                
# Tilting time
tilting_time = 5  # s  T_TILTING
# Top speed of the forklift
top_speed_forklift = 15  # km/h  V_FORKLIFT
# Simultaneous lifting and tilting
simultaneous_lifting_tilting = 6 # s  SIMULTANEOUS_LIFTING_TILTING




# Plinimary calculations
""" 
The system consists of forks for carying the load, a trolley that the forks are welded to, a tower (2 ish m), the main body of the forklift, and the two wheels.
These are split into their own bodys, and the mass center of each body is calculated.
A hydraulic cylinder is used to lift the trollt/forks with a chain, and the load is lifted by the forks.
"""
# Tilt angle in radians
""" The tilt angle is the angle between the forks and the horizontal plane where positive is tilting backwards and negative is tilting forwards."""
degrees = 0
tilting_angel_rad = math.radians(degrees)  # rad
friction_coefficient = 0.2  # Coefficient of friction between the load and the forks

# Gravity force
# Load
Gy_load = -((mass_loade * g) * math.cos(tilting_angel_rad))
Gx_load = -((mass_loade * g) * math.sin(tilting_angel_rad))
# Fork
Gy_fork = -((mass_fork * g) * math.cos(tilting_angel_rad))
Gx_fork = -((mass_fork * g) * math.sin(tilting_angel_rad))
# Trolly
Gy_trolly = -((mass_trolly * g) * math.cos(tilting_angel_rad))
Gx_trolly = -((mass_trolly * g) * math.sin(tilting_angel_rad))
# Tower
Gy_tower = -((mass_tower * g) * math.cos(tilting_angel_rad))
Gx_tower = -((mass_tower * g) * math.sin(tilting_angel_rad))
# Main body
Gy_mainBody = -(mass_mainBody * g)
# Lifting cylinder
Gy_lifting_cylinder = -((mass_liftingCylinder * g) * math.cos(tilting_angel_rad))
Gx_lifting_cylinder = -((mass_liftingCylinder * g) * math.sin(tilting_angel_rad))
# Tilting cylinder
Gy_tilting_cylinder = -(mass_tiltingCylinder * g)


# Load reaction forces
Ny_load = -Gy_load
if tilting_angel_rad < 0:
    R_load = Ny_load * frition_coefficient
else:
    R_load = 0
# Force on trolly from the load
if tilting_angel_rad > 0:
    Nx_load = -Gx_load
else:
    Nx_load = 0

# Unknown reaction forces
Jx, Jy = sp.symbols('Jx Jy')  # Reaction forces at the welding between the forks and the trolly
C1x, C1y = sp.symbols('C1x C1y')  # Reaction forces at the lower conection between the trolly and the tower
C2x, C2y = sp.symbols('C2x C2y')  # Reaction forces at the upper conection between the trolly and the tower
Kx, Ky = sp.symbols('Kx Ky')  # Reaction forces at the upper conection of the lifting cylinder to the chain
Lx, Ly = sp.symbols('Lx Ly')  # Reaction forces at the lower conection of the lifting cylinder to the tower
Ex, Ey = sp.symbols('Ex Ey')  # Reaction forces at the conection of the tilting cylinder to the tower
Bx, By = sp.symbols('Bx By')  # Reaction forces at the tower hinge point to the main body
Dx, Dy = sp.symbols('Dx Dy')  # Reaction forces at the conection of the tilting cylinder to the main body
Ax, Ay = sp.symbols('Ax Ay')  # Reaction forces at the front wheel to the main body
Fx, Fy = sp.symbols('Fx Fy')  # Reaction forces at the rear wheel to the main body

# Equilibrium equations for the forks
eqs.append


# Equilibrium equations for the trolly

# Equilibrium equations for the tower

# Equilibrium equations for the lifting cylinder

# Equilibrium equations for the tilting cylinder

# Equilibrium equations for the main body
