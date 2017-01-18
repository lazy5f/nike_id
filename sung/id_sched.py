"""
n: number of jobs
m: number of machines
L: number of lines
p[j][i]: processing time of job j at i'th machine
"""


def makespan(n, m, L, p, S):
    return max(makespan_flowshop(m, p, Sk) for Sk in S)


def makespan_flowshop(m, p, Sl):
    """
    Sl: schedule of a flowshop
    
    C[i]: completion time at machine i of considering job
    """
    C = [0] * (m + 1)
    for j in Sl:
        for i in range(m):
            C[i] = max(C[i - 1], C[i]) + p[j][i]
    return C[m - 1]


def display_sol(n, m, L, p, S):
    for l in range(L):
        print('Line', l, ':', '-'.join(map(str, S[l])))
    print('MS =', makespan(n, m, l, p, S))


#
# Problems

def ex1():
    p = [(1,3,5), (2,4,8), (2,3,4), (4,6,8), (1,2,3), (2,4,6), (3,4,5)]
    n = len(p)
    m = len(p[0])
    L = 3
    return n, m, L, p

def ex2():
    p = [(1,3,5), (2,4,8), (2,3,4), (4,6,8), (1,2,3), (2,4,6), (3,4,5), (3,4,5)]
    n = len(p)
    m = len(p[0])
    L = 3
    return n, m, L, p


if __name__ == '__main__':
    n, m, L, p = ex1()
    S = [(0, 1), (2, 3), (6, 5, 4)]
    display_sol(n, m, L, p, S)
