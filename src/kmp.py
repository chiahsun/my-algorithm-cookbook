def built_in_index(haystack: str, needle: str):
    try:
        return haystack.index(needle)
    except ValueError:
        return -1


def kmp_index(haystack, needle):
    N = len(needle)
    fallback = [-1] * N
    for i in range(1, N):
        c, prev = needle[i], fallback[i - 1]
        while prev >= 0 and c != needle[prev + 1]:
            prev = fallback[prev]
        if c == needle[prev + 1]:  # Reuse python array[-1]
            fallback[i] = prev + 1
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
    s1, s2 = "abababac", "abac"
    assert kmp_index(s1, s2) == built_in_index(s1, s2)
