#!/usr/bin/env python
"""
Summary
-------
Provide dictionary directories listing solvers, problems, and models.

Listing
-------
solver_directory : dictionary
problem_directory : dictionary
model_directory : dictionary
"""
# import solvers
from solvers.neldmd import NelderMead
from solvers.spsa import SPSA

# QUANTUM
from solvers.astrodfldqaq import ASTRODFLDQAQ
from solvers.astrodfldqaqpf import ASTRODFLDQAQPF
from solvers.astrodfldqaqit import ASTRODFLDQAQIT

from solvers.astrodfrpq import ASTRODFRPQ
from solvers.astrodfrpqpf import ASTRODFRPQPF
from solvers.astrodfrpqit import ASTRODFRPQIT

from solvers.neldmdq import NelderMeadQ
from solvers.spsaq import SPSAQ

# Twomodels
from solvers.twomodel import TWOMODEL
from solvers.onemodel import ONEMODEL

# import models and problems
from models.synthetic import SYNTHETIC, SYNTHETIC_MIN
from models.syntheticvmi import SYNTHETICVMI, SYNTHETICVMI_MIN
from models.maxcut import MAXCUT, MaxCutMinEnergy
from models.syntwomodel import SYNTHETICTWOMODEL, SYNTHETICTWOMODEL_MIN

# directory dictionaries
solver_directory = {
    # QUANTUM
    "NELDMDQ": NelderMeadQ,
    "ASTRODFLDQAQ": ASTRODFLDQAQ,
    "ASTRODFLDQAQPF": ASTRODFLDQAQPF,
    "ASTRODFLDQAQIT": ASTRODFLDQAQIT,
    "ASTRODFRPQ": ASTRODFRPQ,
    "ASTRODFRPQPF": ASTRODFRPQPF,
    "ASTRODFRPQIT": ASTRODFRPQIT,
    "SPSAQ": SPSAQ,
    #
    "TWOMODEL": TWOMODEL,
    "ONEMODEL": ONEMODEL,
    #
    "SPSA": SPSA,
    "NELDMD": NelderMead
}
problem_directory = {
    "SYN-1": SYNTHETIC_MIN,
    "SYNVMI-1": SYNTHETICVMI_MIN,
    "SYNTWOMODEL-1": SYNTHETICTWOMODEL_MIN,
    "MAXCUT-1": MaxCutMinEnergy
}
model_directory = {
    "SYN-1": SYNTHETIC,
    "SYNVMI-1": SYNTHETICVMI,
    "SYNTWOMODEL-1": SYNTHETICTWOMODEL,
    "MAXCUT-1": MAXCUT
}
