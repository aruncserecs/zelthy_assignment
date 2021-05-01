# Create lcs funcation.
def lcs(s, t, n, m):
    # Create DP table
    dp = [[0 for i in range(m + 1)] for j in range(2)]
    res = 0
    index = 0

    for i in range(n + 1):
        for j in range(m + 1):
            if (s[i - 1] == t[j - 1]):
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
                if (dp[i % 2][j] > res):
                    res = dp[i % 2][j]
                    index = i
            else:
                dp[i % 2][j] = 0

    return res, index


# Input values
X = [3, 6, 7, 4, 2, 7, 9, 1, 0, 3, 5, 6]
Y = [1, 5, 6, 9, 7, 4, 2, 7, 9, 9, 2, 1]

l, index = lcs(X, Y, len(X), len(Y))
print(X[index - l:index])
