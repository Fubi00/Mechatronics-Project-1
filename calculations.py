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

hight_massCenterMain = 0.25  # m  H_G


radus_wheel = 0.23  # m  R_W

# Geometry of the lifting mechanism