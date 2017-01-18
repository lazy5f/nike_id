from random import random, randrange, sample
from math import exp

from f_sched import completion_times, display_sol


def sa(n, m, p, t0=1000, t1=0.00001, pi=0.999):
    """
    t0: initial temperature
    pi: temperature cooling parameter
    
    S, z: current solution and its quality
    S0, z0: best solution and quality, so far
    S1, z1: next candidate solution and its quality
    t: current temperature
    t1: termination temperature
    """
    S = S0 = sample(range(n), n)  # initial *random* sequence
    z = z0 = completion_times(n, m, p, S)[S[n - 1]][m - 1]
    
    t, num_iter = t0, 0
    while t > t1:
        num_iter += 1
        
        # Tweak.
        S1 = S[:]
        k, l = sample(range(n), 2)
        S1[k], S1[l] = S1[l], S1[k]
        z1 = completion_times(n, m, p, S1)[S1[n - 1]][m - 1]
        
        # Determine acceptance of candidate solution.
        if z1 <= z or random() < exp((z - z1) / t):
            S, z = S1, z1
            if z < z0:
                S0, z0 = S, z
                print('(i:%d) %s' % (num_iter, z))
        
        # Cooling
        t *= pi
    return S0


if __name__ == '__main__':
    # Input
    import f_sched
    n, m, p = f_sched.ex3()
    # Solve.
    S = sa(n, m, p, 10000, 0.00001, 0.9999)
    # Output solution.
    display_sol(n, m, p, S)
