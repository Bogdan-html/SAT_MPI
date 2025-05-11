def resolution_solver(clauses):
    new = set()
    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i+1, n)]
        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            if set() in resolvents:
                return False
            new.update(frozenset(clause) for clause in resolvents)
        
        existing = set(map(frozenset, clauses))
        if new.issubset(existing):
            return True
        for clause in new:
            if clause not in existing:
                clauses.append(set(clause))

def resolve(ci, cj):
    resolvents = []
    for l in ci:
        if -l in cj:
            resolvent = (ci - {l}) | (cj - {-l})
            resolvents.append(resolvent)
    return resolvents
