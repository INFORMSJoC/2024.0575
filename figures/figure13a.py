import sys
import os.path as o
import time

sys.path.append(o.abspath(o.join(o.dirname(sys.modules[__name__].__file__), "..")))

# Import the Experiment class and other useful functions
from wrapper_base import Experiment, read_experiment_results, post_normalize, plot_progress_curves, plot_solvability_profiles


m = 20 # Macro-replication
L = 200 # Post-replication

problem_name = "MAXCUT-1"

myexperiment = []
n = 2

file_name = f"{'VMI3IT'}_on_{problem_name}"
experiment = read_experiment_results(f"experiments/outputs/{file_name}.pickle")
experiment.solver.name = "VMI-2STRO-DF-3"
myexperiment.append(experiment)

file_name = f"{'ASTRODFRPQIT'}_on_{problem_name}"
experiment = read_experiment_results(f"experiments/outputs/{file_name}.pickle")
experiment.solver.name = "ASTRO-DF"
myexperiment.append(experiment)

post_normalize(experiments=myexperiment, n_postreps_init_opt=L)
print("Plotting results.")

# Produce basic plots of the solver on the problem
plot_progress_curves(experiments=[myexperiment[idx] for idx in range(n)], plot_type="mean", normalize=False, all_in_one=True)

# Plots will be saved in the folder experiments/plots.
print("Finished. " + problem_name + " Plots can be found in experiments/plots folder.")