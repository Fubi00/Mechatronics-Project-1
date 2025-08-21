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
The system consists of forks for carying the load, a trolley that the forks are welded to, a inner and outer tower, the main body of the forklift, and the two wheels.
These are split into their own bodys, and the mass center of each body is calculated.
"""
# Load mass centers of the mecanisme from hinge point
G_load = mass_loade * g # N  G_I
x_load = length_hingePointToMassLoad  # m  x_I
y_load = hight_massCenterLoadFromFork + hight_fork # m  y_I

x_fork = (length_hingePointToE + length_forks) / 2  # m  x_FK
y_fork = hight_fork  # m  y_FK

x_trolly = length_hingePointToCC + (trolly_width / 2)  # m  x_T
