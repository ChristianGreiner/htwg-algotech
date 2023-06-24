def binom(n, k):
    komb = [0] * (n + 1)
    komb[0] = 1

    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            komb[j] = komb[j] + komb[j-1]

    return komb[k]

print(binom(9, 5))
