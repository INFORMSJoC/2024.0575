"""
Generate .pickle fils in /experiments/outputs (figure 14)
"""

import sys
import os.path as o

sys.path.append(o.abspath(o.join(o.dirname(sys.modules[__name__].__file__), "..")))

# Import the Experiment class and other useful functions
from wrapper_base import Experiment, read_experiment_results, post_normalize, plot_progress_curves, plot_solvability_profiles

m = 20 # Macro-replication
L = 200 # Post-replication

solvers = ["VMI3PF-0-cv10", "ASTRODFRPQPF-0"] 
problem_name = "MAXCUT-1"

p = 1

if p == 1:
    budget = 5000 
    theta = (1.6, 1.6) 
elif p == 10:
    budget = 10000 
    theta = (1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6)

all_edges = [[[0,1],[1,2],[0,2]],
            [[0,3],[0,4],[1,3],[2,4]],
            [[0,1],[1,2],[0,2],[0,3]],
            [[0,1],[0,2],[0,3],[0,4]],
            [[0,3],[1,3],[1,2],[0,2]],
            [[0,3],[0,4],[1,3],[1,4],[1,2],[2,4]],
            [[0,3],[0,4],[1,3],[1,4],[1,2],[0,2]],
            [[2,4],[2,1],[3,4],[3,1],[0,2]],
            [[2,4],[2,3],[3,4],[3,1],[0,2]],
            [[0,1],[1,3],[1,4],[1,5],[2,4],[2,5]],
            [[0,3],[1,5],[2,3],[2,4],[2,5],[3,4]],
            [[0,1],[0,2],[1,4],[2,3],[2,5],[3,5]]]


num_problems = len(all_edges)

for i in range(num_problems):
    model_fixed_factors = {"edges": all_edges[i], "p": p, "theta": theta}
    problem_fixed_factors = {"budget": budget, "initial_solution": theta}
    problem_rename = f"MAXCUT-1_edges={all_edges[i]}_p={p}"

    # Temporarily store experiments on the same problem for post-normalization.
    experiments_same_problem = []
    solver_fixed_factors = {}

    for solver in solvers:
        solver_name = solver

        if solver == "VMI3PF-0-cv10":
            solver_name = "ASTRODFLDQAQPF"
            solver_fixed_factors = {"overhead_burden": 0, "sampling_version": 3, "cv": 10}

        # Temporarily store experiments on the same problem for post-normalization.
        print(f"Testing solver {solver} on problem {problem_rename}.")

        # Specify file path name for storing experiment outputs in .pickle file.
        file_name_path = "experiments/outputs/" + solver + "_on_" + problem_rename + ".pickle"
        print(f"Results will be stored as {file_name_path}.")

        # Initialize an instance of the experiment class.
        myexperiment = Experiment(solver_name=solver_name,
                                solver_rename=solver,
                                solver_fixed_factors=solver_fixed_factors,
                                problem_name="MAXCUT-1",
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
