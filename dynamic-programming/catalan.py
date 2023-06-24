def catalan(n: int = 0):
    c = [0] * (n + 1)
    c[0] = c[1] = 1

    for N in range(2, n + 1):
        c[N] = 0
        for k in range(N):
            c[N] += c[k] * c[N - k - 1]

    return c[n]

print(catalan(5))
