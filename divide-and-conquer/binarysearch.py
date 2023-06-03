
def binarysearch(arr: list, key: int) -> int:
    indexAnfang = 0
    indexEnde = len(arr) - 1 # auf letzte Element setzen
    while (indexAnfang <= indexEnde): # Abbruchbedingung testen
        indexMitte = (indexAnfang + indexEnde) // 2 # Devide
        if key == arr[indexMitte]: # Bester Fall
            return indexMitte
        if (key < arr[indexMitte]):
            indexEnde = indexMitte - 1
        else:
            indexAnfang = indexMitte + 1
    return -1


print(binarysearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))