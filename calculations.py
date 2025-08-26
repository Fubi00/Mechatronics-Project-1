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

# Main body mesurements given
F_x = 1.32
G_main_x = 1.05
G_main_y = 0.25
B_x = 0.4
B_y = -0.2
D_x = 0.4
D_y = 0.42
rWheel = 0.23

# Lifting mechanism mesurements
BE_x = 0.4
BE_y =
BC_x = 0.8
BC_y = 0 
BG_lift_x = 0.4
BG_lift_y = 0.15
BG_load_x = 0.8
BG_load_y = 0.15

ForkLength = 1.2

# Center for the main cordinate system is point A, the center of the front wheel
A = (0, 0)  # Point A, center of the front wheel
F = (Fx, 0)  # Point F, center of the rear wheel

G_main = (G_main_x, G_main_y)  # Center of mass for the main body

B = (B_x, B_y)  # Point B, bottom of the tower

D = (D_x, D_y)  # Point D, bottom of the tilting cylinder

# Points for the lifting mechanism
E = (B[0] + BE_x, B[1] + BE_y)  # Point E, top of the tilting cylinder
C1 = (B[0] + BC_x, B[1] + BC_y)  # Point C, top of the tower


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
G_load = [Gx_load, Gy_load]
# Fork
Gy_fork = -((mass_fork * g) * math.cos(tilting_angel_rad))
Gx_fork = -((mass_fork * g) * math.sin(tilting_angel_rad))
G_fork = [Gx_fork, Gy_fork]
# Trolly
Gy_trolly = -((mass_trolly * g) * math.cos(tilting_angel_rad))
Gx_trolly = -((mass_trolly * g) * math.sin(tilting_angel_rad))
G_trolly = [Gx_trolly, Gy_trolly]
# Tower
Gy_tower = -((mass_tower * g) * math.cos(tilting_angel_rad))
Gx_tower = -((mass_tower * g) * math.sin(tilting_angel_rad))
G_tower = [Gx_tower, Gy_tower]
# Main body
Gy_mainBody = -(mass_mainBody * g)
Gx_mainBody = 0
G_mainBody = [Gx_mainBody, Gy_mainBody]
# Lifting cylinder
Gy_lifting_cylinder = -((mass_liftingCylinder * g) * math.cos(tilting_angel_rad))
Gx_lifting_cylinder = -((mass_liftingCylinder * g) * math.sin(tilting_angel_rad))
G_lifting_cylinder = [Gx_lifting_cylinder, Gy_lifting_cylinder]
# Tilting cylinder
Gy_tilting_cylinder = -(mass_tiltingCylinder * g)
Gx_tilting_cylinder = 0
G_tilting_cylinder = [Gx_tilting_cylinder, Gy_tilting_cylinder]
# Startcondition for ligting mechanism
Gy_lift = -((mass_liftingMechanism * g) * math.cos(tilting_angel_rad))
Gx_lift = -((mass_liftingMechanism * g) * math.sin(tilting_angel_rad))
G_lift = [Gx_lift, Gy_lift]


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



# Equilibrium equations for the forks



# Equilibrium equations for the trolly

# Equilibrium equations for the tower

# Equilibrium equations for the lifting cylinder

# Equilibrium equations for the tilting cylinder

# Equilibrium equations for the main body
