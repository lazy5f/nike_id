"""
n: number of jobs
m: number of machines
p[j][i]: processing time of job j at machine i
"""


def completion_times(n, m, p, S):
    """
    RETURN C[j][i]: completion time of job j at machine i
    
    C[S[n - 1]][m - 1]: makespan
    """
    C = [[0] * (m + 1) for _ in range(n + 1)]
    for k in range(n):
        for i in range(m):
            C[S[k]][i] = max(C[S[k]][i - 1], C[S[k - 1]][i]) + p[S[k]][i]
    return C


def display_sol(n, m, p, S):
    print('Schedule:', '-'.join(map(str, S)))
    C = completion_times(n, m, p, S)
    for i in range(m):
        print('M%d:' % i, end=' ')
        for j in S:
            print(C[j][i], end=' ')
        print()
    print('MS =', C[S[n - 1]][m - 1])


#
# Problems

def ex1():
    p = [(2,4,8), (2,3,4), (1,3,5), (4,6,8)]
    n = len(p)
    m = len(p[0])
    return n, m, p

def ex2():
    p = [(1,3,5), (2,4,8), (2,3,4), (4,6,8), (1,2,3), (2,4,6), (3,4,5)]
    n = len(p)
    m = len(p[0])
    return n, m, p

def ex3():
    p = [(4,3,5), (2,4,8), (7,3,4), (4,6,8), (2,2,3), (2,4,6), (1,3,5), (2,4,2), (2,3,4), (3,4,5)]
    n = len(p)
    m = len(p[0])
    return n, m, p


if __name__ == '__main__':
    n, m, p = ex1()
    S = [3, 1, 0, 2]
    display_sol(n, m, p, S)
