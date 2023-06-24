def expo(basis: int, exponent: int):
    if basis == 0:
        return 1
    
    if exponent == 1:
        return basis
    
    return basis * expo(basis, exponent - 1)

print(expo(2, 3))
