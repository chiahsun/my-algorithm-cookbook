
# mississippi
# 012345678910
# 10 i
# 7  ippi
# 4  issippi
# 1  ississippi
# 0  mississippi
# 9  pi
# 8  ppi
# 6  sippi
# 3  sissippi
# 5  ssippi
# 2  ssissippi


def suffix_sort_slow(s):
    N = len(s)
    L = list(range(N))
    L.sort(key=lambda i: s[i:])
    return L


def suffix_sort(s):
    def normalize(A):
        s = list(sorted(list(set(A))))
        d = {s[i]: i for i in range(len(s))}
        return list(map(lambda a: d[a], A))

    N, d = len(s), 1
    order, L = normalize(list(s)), [0] * N
    while d < N:
        nxt = [order[i] * (N+1) + (order[i+d] if i+d < N else -1) for i in range(N)]  # Use N+1 since we have -1
        order = normalize(nxt)
        d *= 2

    for i in range(N):
        L[order[i]] = i
    return L


if __name__ == '__main__':
    #print(suffix_sort("abc"))
    #print(suffix_sort("cba"))


    s = "mississippi"
    assert suffix_sort("mississippi") == [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]
    assert suffix_sort(s) == suffix_sort_slow(s)

    s = "cabaaa"
    assert suffix_sort(s) == [5, 4, 3, 1, 2, 0]
    assert suffix_sort(s) == suffix_sort_slow(s)

    s = "banana"
    assert suffix_sort(s) == [5, 3, 1, 0, 4, 2]
    assert suffix_sort(s) == suffix_sort_slow(s)

    s = "babad"
    assert suffix_sort(s) == [1, 3, 0, 2, 4]
    assert suffix_sort(s) == suffix_sort_slow(s)
