def dp_solver(clauses):
    variables = {abs(lit) for clause in clauses for lit in clause}
    return dp(clauses, variables)

def dp(clauses, variables):
    if not clauses:
        return True
    if any(not clause for clause in clauses):
        return False

    var = next(iter(variables))
    variables = variables - {var}

    pos = simplify(clauses, var)
    if dp(pos, variables.copy()):
        return True

    neg = simplify(clauses, -var)
    return dp(neg, variables.copy())

def simplify(clauses, literal):
    new_clauses = []
    for clause in clauses:
        if literal in clause:
            continue
        new_clause = clause - {-literal}
        new_clauses.append(new_clause)
    return new_clauses
