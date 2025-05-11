import time
import tracemalloc

def load_cnf(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    clauses = []
    for line in lines:
        if line.startswith('p') or line.startswith('c'):
            continue
        literals = list(map(int, line.strip().split()))
        if literals[-1] == 0:
            literals.pop()
        clauses.append(set(literals))
    return clauses

def measure_execution(solver, formula):
    tracemalloc.start()
    start_time = time.time()
    result = solver([clause.copy() for clause in formula])  # deep copy
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return result, end_time - start_time, peak / (1024 * 1024)
