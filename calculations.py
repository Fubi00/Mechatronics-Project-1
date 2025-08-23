#!/usr/bin/env python3
"""
This sctipt contains functions and data to perform various calculations in our worck in designing the lifting mechanism for an forcklift.
The project is part of the course MAS238 "Mekkatronikkprosjekt 1" at the University of Agder (UiA).
"""

""" Created by: [Fabian A. Alsaker, Julian F. Idsø, Daniel, Nasar, 20-08-2025] """

import math


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
degrees = 0
tilting_angel_rad = math.radians(degrees)  # rad
friction_coefficient = 0.2  # Coefficient of friction between the load and the forks

# FBD Load
Gy_load = -((mass_loade * g) * math.cos(tilting_angel_rad))  # N
Gx_load = -((mass_loade * g) * math.sin(tilting_angel_rad))  # N
Ny_load = -Gy_load  # N
if tilting_angel_rad > 0:
    Nx_load = -Gx_load  # N
else:
    Nx_load = 0 # N
if tilting_angel_rad < 0:
    R_load = Ny_load * frition_coefficient  # N, friction force at the load
else:
    R_load = 0  # N

# FBD Fork
Gy_fork = -((mass_fork * g) * math.cos(tilting_angel_rad)) # N
Gx_fork = -((mass_fork * g) * math.sin(tilting_angel_rad))  # N
F1y = -Ny_load # N, force from the load
F1x = -R_load  # N, friction force at the load
F2y = -(Gy_fork + F1y)  # N, counter force at the fork/trolly weld
F2x = -(Gx_fork + F1x)  # N, counter force at the fork/trolly weld

# FBD Trolly
Gy_trolly = -((mass_trolly * g) * math.cos(tilting_angel_rad))  # N
Gx_trolly = -((mass_trolly * g) * math.sin(tilting_angel_rad))  # N
F3y = -F2y  # N, force from the fork/trolly weld
F3x = -F2x  # N, force from the trolly/fork weld
F4x = -Nx_load  # N, force from the load if tilted backwards
F6x = 0  # N, force trolly top connection
F5y = -(Gy_trolly + F3y)  # N, counter force at the trolly/fork weld
F5x = -(Gx_trolly + F3x + F4x)  # N, counter force at the trolly/fork weld

# FBD Tower
Gy_tower = -((mass_tower * g) * math.cos(tilting_angel_rad))  # N
Gx_tower = -((mass_tower * g) * math.sin(tilting_angel_rad))  # N

# FBD Liftting cylinder
aplied_force_lifting_cylinder = 0  # N, force applied by the lifting cylinder
F11

# FBD tilting cylinder
aplied_force_tilting_cylinder = 0  # N, force applied by the tilting cylinder




# FBD Main body
Gy_mainBody = -(mass_mainBody * g)  # N

F17y = F18y = -()   # N, force from ground at the wheels
F17x = F18x = -()  # N, force from ground at the wheels