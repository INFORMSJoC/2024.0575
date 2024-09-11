"""
Generate .pickle fils in /experiments/outputs (figure13a) and .npy fils in /experiments/outputs (figure 13b)
"""

import sys
import os.path as o

sys.path.append(o.abspath(o.join(o.dirname(sys.modules[__name__].__file__), "..")))

# Import the Experiment class and other useful functions
from wrapper_base import Experiment, read_experiment_results, post_normalize, plot_progress_curves, plot_solvability_profiles

m = 20 # Macro-replication
L = 200 # Post-replication

p = 1 # circuit depths
communication_costs = 0 # communication costs

solvers = ["VMI3IT", "ASTRODFRPQIT"]
problem_name = "MAXCUT-1"
# Temporarily store experiments on the same problem for post-normalization.
experiments_same_problem = []
solver_fixed_factors = {}

for solver in solvers:
    solver_name = solver

    if solver == "VMI3IT":
        solver_name = "ASTRODFLDQAQIT"
        solver_fixed_factors = {"overhead_burden": 0, "sampling_version": 3}
    else:
        solver_name = "ASTRODFRPQIT"
        solver_fixed_factors = {"overhead_burden": 0}

    # Temporarily store experiments on the same problem for post-normalization.
    print(f"Testing solver {solver} on problem {problem_name}.")

    # Specify file path name for storing experiment outputs in .pickle file.
    file_name_path = "experiments/outputs/" + solver + "_on_" + problem_name + ".pickle"
    print(f"Results will be stored as {file_name_path}.")

    # Initialize an instance of the experiment class.
    myexperiment = Experiment(solver_name=solver_name,
                              solver_rename=solver,
                              solver_fixed_factors=solver_fixed_factors,
                              problem_name="MAXCUT-1")

    # Run a fixed number of macroreplications of the solver on the problem.
    myexperiment.run(n_macroreps=m)
    myexperiment.post_replicate(n_postreps=L)
