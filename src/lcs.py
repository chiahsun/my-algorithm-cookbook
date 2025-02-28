
# Space O(M * N) version, easier to read
def lcs(a, b, get_seq=False):
    M, N = len(a), len(b)
    dp = [[0] * (N+1) for _ in range(M+1)]
    for i in range(M):
        for k in range(N):
            if a[i] == b[k]:
                dp[i+1][k+1] = dp[i][k] + 1
            else:
                dp[i+1][k+1] = max(dp[i+1][k], dp[i][k+1])

    if not get_seq:
        return dp[M][N]
    
    i, k, seq = M, N, []
    while i > 0 or k > 0:
        if i > 0 and dp[i-1][k] == dp[i][k]:
            i = i - 1
        elif k > 0 and dp[i][k-1] == dp[i][k]:
            k = k - 1
        else:
            i = i - 1
            k = k - 1
            seq.append(a[i])
    return "".join(reversed(seq))


if __name__ == '__main__':
    # https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
    a = "aggtab"
    b = "gxtxayb"
    assert lcs(a, b) == 4
    assert lcs(a, b, get_seq=True) == "gtab"

    # https://en.wikipedia.org/wiki/Longest_common_subsequence
    a = "xmjyauz"
    b = "mzjawxu"
    assert lcs(a, b) == 4
    assert lcs(a, b, get_seq=True) == "mjau"

