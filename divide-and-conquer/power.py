def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    
    # divide
    half_exponent = exponent // 2
    result = power(base, half_exponent)
    
    # conquer
    if exponent % 2 == 0:
        return result * result
    else:
        return result * result * base

print(power(2, 5))