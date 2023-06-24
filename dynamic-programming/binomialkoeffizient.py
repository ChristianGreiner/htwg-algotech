def binom(n, k):
    komb = [0] * (n + 1)
    for i in range(n):
        komb[0] = 1
        komb[i] = 1

        for k in range(i-1, 0, -1):
            komb[k] = komb[k] + komb[k-1]

    return komb[k]

print(binom(5, 9))