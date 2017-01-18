from itertools import permutations

from f_sched import completion_times, display_sol


def all_enum(n, m, p):
    MS0, num_iter = 1e400, 0
    for S in permutations(range(n)):
        num_iter += 1
        C = completion_times(n, m, p, S)
        MS = C[S[n - 1]][m - 1]
        if MS < MS0:
            MS0, S0 = MS, S
            print('(i:%d) %s' % (num_iter, MS))
    return S0


if __name__ == '__main__':
    # Input
    import f_sched
    n, m, p = f_sched.ex3()
    # Solve.
    S0 = all_enum(n, m, p)
    # Output solution.
    display_sol(n, m, p, S0)
