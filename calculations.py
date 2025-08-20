#!/usr/bin/env python3
"""
This sctipt contains functions and data to perform various calculations in our worck in designing the lifting mechanism for an forcklift.
The project is part of the course MAS238 "Mekkatronikkprosjekt 1" at the University of Agder (UiA).
"""
""Created by: [Fabian A. Alsaker, Julian F. Idsø, Daniel, Nasar, 2025-08-20]""

import math


# Constants for gyometry

# Masses of the components
mass_loade = 1500  # kg
mass_mainBody = 3500  # kg
mass_liftingMechanism = 300  # kg

# Geometry of the forklift body
length_wheelBase = 1.32  # m  L_W
length_massCenterMain = 1.05  # m  L_G
length_ePointToCC = 0  # m x`c
length_hingePointToE = 0.4  # m  L_BC
length_hingePointToCC = 0.4  # m  L_BC
length_hingePointToMassLift = 0.4  # m  L_BC
length_hingePointToMassLoad = 0  # m  L_BC
length_forks = 1.2 # m  L_FK

hight_massCenterMain = 0.25  # m  H_G
hight_massCenterLiftingMechanismFromFork = 0.15  # m  H_TTF
hight_massCenterLoadFromFork = 0 # m  H_PL
hight_forkUnder = 0  # m  y`FK
hight_hingePoint = -0.2  # m  y_B


radus_wheel = 0.23  # m  R_W

# Geometry of the lifting mechanism