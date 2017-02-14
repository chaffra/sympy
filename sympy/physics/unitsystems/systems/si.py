# -*- coding: utf-8 -*-

"""
SI unit system.

SI stands for "...".
"""

from __future__ import division

from sympy.physics.unitsystems.simplifiers import qsimplify, usimplify
from sympy.physics.unitsystems import (Dimension, DimensionSystem, Unit,
                                       Constant, UnitSystem)
from sympy import latex
from sympy.physics.unitsystems.prefixes import PREFIXES, prefix_unit
import sys

# base dimensions
length = Dimension(name="length", symbol="L", length=1)
mass = Dimension(name="mass", symbol="M", mass=1)
time = Dimension(name="time", symbol="T", time=1)
temperature = Dimension(name="temperature", symbol="K", temperature=1)

# derived dimensions
velocity = Dimension(name="velocity", length=1, time=-1)
acceleration = Dimension(name="acceleration", length=1, time=-2)
momentum = Dimension(name="momentum", mass=1, length=1, time=-1)
force = Dimension(name="force", symbol="F", mass=1, length=1, time=-2)
energy = Dimension(name="energy", symbol="E", mass=1, length=2, time=-2)
power = Dimension(name="power", length=2, mass=1, time=-3)
pressure = Dimension(name="pressure", mass=1, length=-1, time=-2)
frequency = Dimension(name="frequency", symbol="f", time=-1)
action = Dimension(name="action", symbol="A", length=2, mass=1, time=-1)

dims = (velocity, acceleration, momentum, force, energy, power, pressure,
        frequency, action)

# dimension system
si_dim = DimensionSystem(base=(length, mass, time, temperature), dims=dims, name="SI")

# base units
m = Unit(length, abbrev="m")
kg = Unit(mass, abbrev="g", prefix=PREFIXES["k"])
s = Unit(time, abbrev="s")
K = Unit(temperature,abbrev="K")

# gram; used to define its prefixed units
g = Unit(mass, abbrev="g")

# derived units
v = speed = Unit(velocity,abbrev=latex(m/s))
a = Unit(acceleration)
p = Unit(momentum)
J = Unit(energy, factor=10**3, abbrev="J")
N = Unit(force, factor=10**3, abbrev="N")
W = Unit(power, factor=10**3, abbrev="W")
Pa = Unit(pressure, factor=10**3, abbrev="Pa")
Hz = Unit(frequency, abbrev="Hz")

eV = Unit(energy, factor=1.6021766208e-19*J.factor, abbrev="eV")

# constants
# Newton constant
G = Constant(usimplify(m**3*kg**-1*s**-2), factor=6.67384e-11, abbrev="G")
# speed of light
c = Constant(velocity, factor=299792458, abbrev="c")

boltzmann = Constant(usimplify(J/K), factor=1.38064852e-23, abbrev='k_b')

units = [m, g, s, J, N, W, Pa, Hz, eV]
all_units = []

# Prefixes of units like g, J, N etc get added using `prefix_unit`
# in the for loop, but the actual units have to be added manually.
all_units.extend([g, J, N, W, Pa, Hz, eV])

for u in units:
    all_units.extend(prefix_unit(u, PREFIXES))

all_units.extend([v, a, p, G, c, boltzmann])

# unit system
si = UnitSystem(base=(m, kg, s, K), units=all_units, name="SI")

for unit in all_units:
    setattr(sys.modules[__name__], unit.__repr__(), unit)
