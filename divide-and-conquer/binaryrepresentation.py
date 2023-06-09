def binary_representation(n):
    if n > 1:
        binary_representation(n // 2)
    print(n % 2, end='')

number = 12
binary_representation(number)