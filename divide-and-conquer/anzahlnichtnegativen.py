
def count_non_negative_numbers(arr, start, end):
    if start > end:
        return 0
    
    if start == end:
        if arr[start] >= 0:
            return 1
        else:
            return 0
    
    mid = (start + end) // 2
    count_left = count_non_negative_numbers(arr, start, mid)
    count_right = count_non_negative_numbers(arr, mid+1, end)

    return count_left + count_right

numbers = [2, -1, 0, 5, -3, 10, 8]
result = count_non_negative_numbers(numbers, 0, len(numbers)-1)
print(result)
