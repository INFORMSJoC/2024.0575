"""
Generate .pickle fils in /experiments/outputs (figure 8c and 8d)
"""

import sys
import os.path as o

sys.path.append(o.abspath(o.join(o.dirname(sys.modules[__name__].__file__), "..")))

# Import the Experiment class and other useful functions
from wrapper_base import Experiment, post_normalize

m = 20 # Macro-replication
L = 200 # Post-replication

communication_costs = 0
problem_name = "SYNVMI-1"

if communication_costs == 0:
    solvers = ["VMI1-0", "VMI2-0", "VMI3-0-cv10"]
    budget = 10000
elif communication_costs == 1000:
    solvers = ["VMI1-1000", "VMI2-1000", "VMI3-1000-cv10"]
    budget = 500000


all_sigma_version = [0,1,2,3]
d = 2
num_problems = len(all_sigma_version)


initial_solution = (0, 0)

for i in range(num_problems):
    model_fixed_factors = {"sigma_version": all_sigma_version[i], "dim": d}
    problem_fixed_factors = {"budget": budget, "initial_solution": initial_solution}
    problem_rename = f"SYNVMI-1_sigma_version={all_sigma_version[i]}_dim={d}"

    experiments_same_problem = []
    for solver in solvers:
        solver_name = solver

        if solver == "VMI3-0":
            solver_name = "ASTRODFLDQAQ"
            solver_fixed_factors = {"overhead_burden": 0, "sampling_version": 3}
        elif solver == "VMI3-0-cv10":
            solver_name = "ASTRODFLDQAQ"
            solver_fixed_factors = {"overhead_burden": 0, "sampling_version": 3, "cv":10}
        elif solver == "VMI2-0":
            solver_name = "ASTRODFLDQAQ"
            solver_fixed_factors = {"overhead_burden": 0, "sampling_version": 2}
        elif solver == "VMI1-0":
            solver_name = "ASTRODFLDQAQ"
            solver_fixed_factors = {"overhead_burden": 0, "sampling_version": 1}
        elif solver == "NELDMDQ-0":
            solver_name = "NELDMDQ"
            solver_fixed_factors = {"overhead_burden": 0}
        elif solver == "SPSAQ-0":
            solver_name = "SPSAQ"
            solver_fixed_factors = {"overhead_burden": 0}
        elif solver == "ASTRODFRPQ-0":
            solver_name = "ASTRODFRPQ"
            solver_fixed_factors = {"overhead_burden": 0}

        if solver == "VMI3-1000":
            solver_name = "ASTRODFLDQAQ"
            solver_fixed_factors = {"overhead_burden": 1000, "sampling_version": 3}
        elif solver == "VMI3-1000-cv10":
            solver_name = "ASTRODFLDQAQ"
            solver_fixed_factors = {"overhead_burden": 1000, "sampling_version": 3, "cv":10}
        elif solver == "VMI2-1000":
            solver_name = "ASTRODFLDQAQ"
            solver_fixed_factors = {"overhead_burden": 1000, "sampling_version": 2}
        elif solver == "VMI1-1000":
            solver_name = "ASTRODFLDQAQ"
            solver_fixed_factors = {"overhead_burden": 1000, "sampling_version": 1}
        elif solver == "NELDMDQ-1000":
            solver_name = "NELDMDQ"
            solver_fixed_factors = {"overhead_burden": 1000}
        elif solver == "SPSAQ-1000":
            solver_name = "SPSAQ"
            solver_fixed_factors = {"overhead_burden": 1000}
        elif solver == "ASTRODFRPQ-1000":
            solver_name = "ASTRODFRPQ"
            solver_fixed_factors = {"overhead_burden": 1000}

        # Temporarily store experiments on the same problem for post-normalization.
        print(f"Testing solver {solver} on problem {problem_rename}.")

        # Specify file path name for storing experiment outputs in .pickle file.
        file_name_path = "experiments/outputs/" + solver + "_on_" + problem_rename + ".pickle"
        print(f"Results will be stored as {file_name_path}.")

        # Initialize an instance of the experiment class.
        myexperiment = Experiment(solver_name=solver_name,
                                solver_rename=solver,
                                solver_fixed_factors=solver_fixed_factors,
                                problem_name="SYNVMI-1",
                                problem_rename=problem_rename,
                                problem_fixed_factors=problem_fixed_factors,
                                model_fixed_factors=model_fixed_factors)

        # Run a fixed number of macroreplications of the solver on the problem.
        myexperiment.run(n_macroreps=m)

        print("Post-processing results.")

        # Run a fixed number of postreplications at all recommended solutions.
        myexperiment.post_replicate(n_postreps=L)
        experiments_same_problem.append(myexperiment)

    # Find an optimal solution x* for normalization.
    post_normalize(experiments=experiments_same_problem, n_postreps_init_opt=L)
