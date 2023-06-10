def catalan(n: int = 0):
    liste = [0] * (n + 1)
    liste[0] = liste[1] = 1

    for i in range(2, n + 1):
        for j in range(i):
            liste[i] += liste[j] * liste[i - j - 1]

    return liste[n]    

print(catalan(5))
