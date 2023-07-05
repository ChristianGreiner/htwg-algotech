def binary(n):
    # Basisfall
    if n > 1:
        binary(n // 2) # <- Divide und rekursiver Aufruf
    print(n % 2, end='') # Herschen

binary(12)