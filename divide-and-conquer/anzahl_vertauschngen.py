def merge(liste, left, right):
    i = j = k = 0
    inversions = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            liste[k] = left[i]
            i += 1
        else:
            liste[k] = right[j]
            j += 1
            inversions += len(left) - i
        k += 1

    while i < len(left):
        liste[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        liste[k] = right[j]
        j += 1
        k += 1

    return inversions

def anzahl_vertauschungen(liste):
    """
    Gibt die Anzahl der Vertauschungen zurück, die nötig sind, um die Liste zu sortieren.
    """
    if len(liste) <= 1:
        return 0

    # divide
    middle = len(liste) // 2
    left = liste[:middle]
    right = liste[middle:]

    # conquer
    count = anzahl_vertauschungen(left) + anzahl_vertauschungen(right)

    # merge
    inversions = merge(liste, left, right)

    return count + inversions

result = anzahl_vertauschungen([2, 3, 4, 1, 5, 8, 7, 6])
print("Anzahl der Vertauschungen:", result)
