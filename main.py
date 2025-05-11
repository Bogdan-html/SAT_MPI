from utils import load_cnf, measure_execution
from resolution import resolution_solver
from dp import dp_solver
from dpll import dpll_solver

import os
import csv

def run_all_tests():
    folder = "test_formulas"
    output_file = "results/summary.csv"

    os.makedirs("results", exist_ok=True)  # Asigură că există directorul results

    with open(output_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Formula", "Method", "Result", "Time (s)", "Memory (MB)"])

        for filename in os.listdir(folder):
            if filename.endswith(".cnf"):
                print(f"Testing on: {filename}")
                formula = load_cnf(os.path.join(folder, filename))

                for name, solver in [("Resolution", resolution_solver), ("DP", dp_solver), ("DPLL", dpll_solver)]:
                    print(f"Running {name}...")
                    result, time_taken, memory = measure_execution(solver, formula)
                    print(f"{name}: Result={result}, Time={time_taken:.4f}s, Memory={memory:.2f}MB\n")
                    writer.writerow([filename, name, result, f"{time_taken:.4f}", f"{memory:.2f}"])

if __name__ == "__main__":
    run_all_tests()
