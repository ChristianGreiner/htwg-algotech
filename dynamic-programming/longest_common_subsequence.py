def longest_common_subsequence(a, b):
    arr = [[0] * (len(a) + 1) for _ in range(len(b) + 1)]
    
    for i in range(1, len(b) + 1):
        for j in range(1, len(a) + 1):
            if a[j - 1] == b[i - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])

    # Trace back
    result = []
    i, j = len(b), len(a)
    
    while i > 0 and j > 0:
        if a[j - 1] == b[i - 1]:
            result.append(a[j - 1])
            i -= 1
            j -= 1
        elif arr[i][j - 1] > arr[i - 1][j]:
            j -= 1
        else:
            i -= 1

    result.reverse()
    
    return result


# Beispielaufruf
a = [2, 4]
b = [1, 2, 3, 4]
result = longest_common_subsequence(a, b)
print("Längste aufsteigende Teilfolge:", result)
