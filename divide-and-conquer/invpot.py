def invpot(x, k):
    # Basisfälle
    if k == 1:
        return 1/x
    elif k == 0:
        return 1

    # Divide
    k1 = k // 2
    k2 = k - k1 # <- Rest berechnen

    return invpot(x, k1) * invpot(x, k2)

print(invpot(2, 10))