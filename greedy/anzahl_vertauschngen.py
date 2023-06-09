
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

    print(left)
    print(right)

    if len(left) > 1:
        left = anzahl_vertauschungen(left)
        right = anzahl_vertauschungen(right)
    


anzahl_vertauschungen([2, 3, 4, 1, 5, 8, 7, 6])