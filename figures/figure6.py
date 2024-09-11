import sys
import os.path as o

sys.path.append(o.abspath(o.join(o.dirname(sys.modules[__name__].__file__), "..")))

# Import the Experiment class and other useful functions
from wrapper_base_onlylog import Experiment, read_experiment_results, post_normalize, plot_progress_curves, plot_solvability_profiles

m = 20 # Macro-replication
L = 200 # Post-replication

solvers = ["TWOMODEL", "ONEMODEL", "NELDMD"]

problem_name = "SYNTWOMODEL-1"

budget = [2000, 50000]
all_solutions = (3,3)

num_problems = len(budget)

for i in range(num_problems):
    problem_fixed_factors = {"initial_solution": all_solutions, "budget": budget[i]}
    problem_rename = f"SYNTWOMODEL-1_solution={all_solutions}_budget={budget[i]}"

    # Temporarily store experiments on the same problem for post-normalization.
    experiments_same_problem = []
    solver_fixed_factors = {}

    for solver in solvers:
        solver_name = solver
        # Temporarily store experiments on the same problem for post-normalization.
        print(f"Testing solver {solver} on problem {problem_rename}.")

        # Specify file path name for storing experiment outputs in .pickle file.
        file_name_path = "experiments/outputs/" + solver + "_on_" + problem_rename + ".pickle"
        print(f"Results will be stored as {file_name_path}.")

        # Initialize an instance of the experiment class.
        myexperiment = Experiment(solver_name=solver_name,
                                solver_rename=solver,
                                solver_fixed_factors=solver_fixed_factors,
                                problem_name="SYNTWOMODEL-1",
                                problem_rename=problem_rename,
                                problem_fixed_factors=problem_fixed_factors)

        # Run a fixed number of macroreplications of the solver on the problem.
        myexperiment.run(n_macroreps=m)

        print("Post-processing results.")

        # Run a fixed number of postreplications at all recommended solutions.
        myexperiment.post_replicate(n_postreps=L)
        experiments_same_problem.append(myexperiment)

    # Find an optimal solution x* for normalization.
    post_normalize(experiments=experiments_same_problem, n_postreps_init_opt=L)

myexperiment = []
ind_experiment = []
n = len(solvers)

for solver in solvers:
    experiments_same_solver = []
    solver_name = solver
    if solver == "TWOMODEL":
        solver_name = "ASTRO-DF with two local models"
    elif solver == "ONEMODEL":
        solver_name = "ASTRO-DF with one local model"
    elif solver == "NELDMD":
        solver_name = "Nelder-Mead"
    
    for i in range(num_problems):
        problem_rename = f"SYNTWOMODEL-1_solution={all_solutions}_budget={budget[i]}"
        file_name = f"{solver}_on_{problem_rename}"
        # Load experiment.
        new_experiment = read_experiment_results(f"experiments/outputs/{file_name}.pickle")
        new_experiment.problem.name = f"SYN-1_initial_solution={all_solutions}_budget={budget[i]}"
        new_experiment.solver.name = solver_name
        experiments_same_solver.append(new_experiment)

    myexperiment.append(experiments_same_solver)

n_solvers = len(myexperiment)
n_problems = len(myexperiment[0])
print("Plotting results.")

for i in range(n_problems):
    plot_progress_curves([myexperiment[solver_idx][i] for solver_idx in range(n_solvers)], plot_type="mean", normalize=False)
    
print("Finished. Plots can be found in experiments/plots folder.")
