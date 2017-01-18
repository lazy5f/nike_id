from itertools import permutations

from id_sched import makespan, display_sol


def all_enum(n, m, L, p):
    def all_sequence(A, l=0):
        for Sl in permutations(A[l]):
            if l == len(A) - 1:
                yield [Sl]
            else:
                for S_after_l in all_sequence(A, l + 1):
                    yield [Sl] + S_after_l
    #
    MS0 = 1e400
    for a_num in range(L**n):
        A = [[] for _ in range(L)]
        for j in range(n):
            A[a_num % L].append(j)
            a_num //= L
        for S in all_sequence(A):
            MS = makespan(n, m, L, p, S)
            if MS < MS0:
                MS0, S0 = MS, S
    return S0


if __name__ == '__main__':
    # Input
    import id_sched
    n, m, L, p = id_sched.ex1()
    # Solve.
    S0 = all_enum(n, m, L, p)
    # Output solution.
    display_sol(n, m, L, p, S0)
