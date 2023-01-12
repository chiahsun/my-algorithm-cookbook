def built_in_index(haystack: str, needle: str):
    try:
        return haystack.index(needle)
    except ValueError:
        return -1


def kmp_index(haystack, needle, trace=False):
    N = len(needle)
    fallback = [-1] * N
    for i in range(1, N):
        c, prev = needle[i], fallback[i - 1]
        while prev >= 0 and c != needle[prev + 1]:
            prev = fallback[prev]
        if c == needle[prev + 1]:
            fallback[i] = prev + 1
    if trace:
        print('fallback: ', fallback)
    pos = -1
    for i, c in enumerate(haystack):
        while pos >= 0 and c != needle[pos + 1]:
            pos = fallback[pos]
        if c == needle[pos + 1]:
            pos += 1
        if pos == N - 1:
            return i - N + 1
    return -1


if __name__ == "__main__":
    # abac
    # --0-
    s1, s2 = "abababac", "abac"
    assert kmp_index(s1, s2, trace=True) == built_in_index(s1, s2)

    # ababac
    # --012-
    s1, s2 = "abababac", "ababac"
    assert kmp_index(s1, s2, trace=True) == built_in_index(s1, s2)

    # aaabaaabaaaab
    # -0100123456
    # 0123456
    #     6->2->1
    #            23
    s1, s2 = "abababac", "aaabaaabaaaab"
    # print(kmp_index(s1, s2, trace=True))
    assert kmp_index(s1, s2, trace=True) == built_in_index(s1, s2)
