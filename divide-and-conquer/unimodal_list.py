
def unimodal_list(a: list, links: int, rechts: int) -> int:
    """Return the index of the maximum value in a unimodal list."""
    if (links == rechts):
        return links
    mid = (links + rechts) // 2

    if (a[mid] > a[mid + 1]):
        return unimodal_list(a, links, mid)
    
    return unimodal_list(a, mid + 1, rechts)

a = [1, 2, 3, 4, 2, 1]
print(unimodal_list(a, 0, len(a) - 1))