from strategies import choose_variable

def dpll_solver(clauses):
    return dpll(clauses, {})

def dpll(clauses, assignment):
    clauses = simplify_all(clauses, assignment)
    if not clauses:
        return True
    if any(not clause for clause in clauses):
        return False

    var = choose_variable(clauses)
    for val in [True, False]:
        new_assign = assignment.copy()
        new_assign[var] = val
        if dpll(clauses, new_assign):
            return True
    return False

def simplify_all(clauses, assignment):
    result = []
    for clause in clauses:
        new_clause = set()
        skip = False
        for lit in clause:
            var = abs(lit)
            sign = lit > 0
            if var in assignment:
                if assignment[var] == sign:
                    skip = True
                    break
            else:
                new_clause.add(lit)
        if not skip:
            result.append(new_clause)
    return result
