def ggt(a, b):
    
    # Basisfälle
    if b == 0:
        return a
    
    # divide
    rest = a % b
    
    return ggt(b, rest)

print(ggt(54, 64))