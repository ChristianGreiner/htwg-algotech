def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n  # Initialisierung der LIS-Länge für jedes Element als 1

    # Berechnung der LIS-Länge für jedes Element in arr
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Bestimmung der maximalen LIS-Länge
    max_length = max(lis)

    # Bestimmung der tatsächlichen LIS
    lis_sequence = []
    current_length = max_length
    for i in range(n - 1, -1, -1):
        if lis[i] == current_length:
            lis_sequence.append(arr[i])
            current_length -= 1

    lis_sequence.reverse()  # Umkehrung der Reihenfolge

    return lis_sequence


# Beispielaufruf
arr = [3,5,76,1,45,2,31,89,90,0,4,15,23,47,95,21,67]
result = longest_increasing_subsequence(arr)
print("Längste aufsteigende Teilfolge:", result)
