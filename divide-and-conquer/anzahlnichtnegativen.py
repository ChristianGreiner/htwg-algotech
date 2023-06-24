
def count_non_negative_numbers(arr):
    if len(arr) == 0:
        return 0
    
    if len(arr) == 1:
        if arr[0] >= 0:
            return 1
        else:
            return 0
    
    mid = len(arr) // 2
    count_left = count_non_negative_numbers(arr[:mid])
    count_right = count_non_negative_numbers(arr[mid:])

    return count_left + count_right

numbers = [2, -1, 0, 5, -3, 10, 8]
result = count_non_negative_numbers(numbers)
print(result)
