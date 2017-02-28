# -*- coding: utf-8 -*-

"""
SI unit system.

SI stands for "...".
"""

from __future__ import division

from sympy.physics.unitsystems.simplifiers import qsimplify, usimplify
from sympy.physics.unitsystems import (Dimension, DimensionSystem, Unit,
                                       Constant, UnitSystem, Quantity)
from sympy import latex
from sympy.physics.unitsystems.prefixes import PREFIXES, prefix_unit
import sys
import math

# base dimensions
length = Dimension(name="length", symbol="m", length=1)
mass = Dimension(name="mass", symbol="kg", mass=1)
time = Dimension(name="time", symbol="s", time=1)
temperature = Dimension(name="temperature", symbol="K", temperature=1)
electric_current = Dimension(name='electric_current', symbol="A", electric_current=1)

# derived dimensions
velocity = Dimension(name="velocity", length=1, time=-1, symbol=latex(length/time))
acceleration = Dimension(name="acceleration", length=1, time=-2)
momentum = Dimension(name="momentum", mass=1, length=1, time=-1)
force = Dimension(name="force", symbol="N", mass=1, length=1, time=-2)
energy = Dimension(name="energy", symbol="J", mass=1, length=2, time=-2)
power = Dimension(name="power", length=2, mass=1, time=-3, symbol='W')
pressure = Dimension(name="pressure", mass=1, length=-1, time=-2, symbol='Pa')
frequency = Dimension(name="frequency", symbol="Hz", time=-1)
action = Dimension(name="action", symbol="A", length=2, mass=1, time=-1)

electric_charge = Dimension(name="electric_charge", symbol="C", time=1, electric_current=1)

dims = (velocity, acceleration, momentum, force, energy, power, pressure,
        frequency, action, electric_charge)

# dimension system
si_dim = DimensionSystem(base=(length, mass, time, temperature, electric_current),
                         dims=dims, name="SI")

# base units
m = Unit(length, abbrev="m")
kg = Unit(mass, abbrev="kg" #, prefix=PREFIXES["k"]
          )
s = Unit(time, abbrev="s")
K = Unit(temperature,abbrev="K")
A = Unit(electric_current, abbrev="A")

# gram; used to define its prefixed units
g = Unit(mass, factor=1e-3, abbrev="g")

# derived units
v = speed = Unit(velocity,abbrev=latex(m/s))
a = Unit(acceleration)
p = Unit(momentum)
J = Unit(energy, factor=1.0, abbrev='J')
N = Unit(force, factor=1.0, abbrev="N")
W = Unit(power, abbrev="W")
Pa = Unit(pressure, factor=1.0, abbrev="Pa")
Hz = Unit(frequency, abbrev="Hz")
C = Unit(electric_charge, abbrev="C")

V = Unit(usimplify(W/A), abbrev='V')



# constants
# Newton constant
G = Constant(usimplify(m**3*kg**-1*s**-2), factor=6.67384e-11, abbrev="G")
# speed of light

c = Constant(usimplify(m/s), factor=299792458, abbrev="c")
#c = Quantity(factor=299792458, unit=usimplify(m/s), abbrev="c")

boltzmann = Constant(usimplify(J/K), factor=1.38064852e-23, abbrev='k_b')
#boltzmann = Quantity(factor=1.38064852e-23, unit=usimplify(J/K), abbrev='k_b')

h = Constant(usimplify(J*s), factor=6.626070040e-34, abbrev='h')
#h = Quantity(factor=6.626070040e-34, unit=usimplify(J*s), abbrev='h')

hbar = Constant(usimplify(J*s), factor=h.factor/2.0/math.pi, abbrev=r'\hbar')
#hbar = Quantity(factor=h.factor/2.0/math.pi, unit=usimplify(J*s), abbrev=r'\hbar')

qe = Constant(C, factor=1.60217733e-19, abbrev='q')

eV = Unit(usimplify(qe*V), abbrev="eV")

units = [m, g, s, J, N, W, Pa, Hz, eV, C, V]
all_units = []

# Prefixes of units like g, J, N etc get added using `prefix_unit`
# in the for loop, but the actual units have to be added manually.
all_units.extend([g, J, N, W, Pa, Hz, eV, C, V])

for u in units:
    all_units.extend(prefix_unit(u, PREFIXES, exclude=['kg']))

all_units.extend([v, a, p, G, c, boltzmann, h, hbar, qe])

# unit system
si = UnitSystem(base=(m, kg, s, K), units=all_units, name="SI")

for unit in all_units:
    setattr(sys.modules[__name__], unit.__repr__(), unit)
