def choose_variable(clauses):
    count = {}
    for clause in clauses:
        for lit in clause:
            var = abs(lit)
            count[var] = count.get(var, 0) + 1
    return max(count, key=count.get)
