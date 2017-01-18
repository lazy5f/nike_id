from math import ceil

from id_sched import display_sol


def sb1(n, m, L, p):
    S = [[] for _ in range(L)]
    
    p_sum = sum(sum(pj) for pj in p)
    p_avg = ceil(p_sum / L)
    
    l, j, p_part_sum = 0, 0, [0] * L
    while j < n:
        pj_sum = sum(p[j])
        if p_part_sum[l] + pj_sum <= p_avg:
            S[l].append(j)
            p_part_sum[l] += pj_sum
            j += 1
        else:
            l += 1
            if l == L:
                break
    
    for j in range(j, n):
        l = min(range(L), key=lambda x: p_part_sum[x])
        S[l].append(j)
        p_part_sum[l] += sum(p[j])
    
    return S


if __name__ == '__main__':
    # Input
    import id_sched
    n, m, L, p = id_sched.ex1()
    # Solve.
    S = sb1(n, m, L, p)
    # Output solution.
    display_sol(n, m, L, p, S)
