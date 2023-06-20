from math import floor

def merge(left: list, right: list):
    sorted_arr = []
    l, r = 0, 0
    switch = 0
    while l != len(left) or r != len(right):
        if l == len(left):
            # If the left element is greater than the right element, then we have to switch
            if left[l - 1] > right[r]:
                switch += 1

            sorted_arr.append(right[r])
            r += 1
        elif r == len(right):

            # If the left element is greater than the right element, then we have to switch
            if left[l] > right[r]:
                switch += 1

            sorted_arr.append(left[l])
            l += 1
        elif left[l] < right[r]:
            
            # If the left element is greater than the right element, then we have to switch
            if left[l] > right[r]:
                switch += 1

            sorted_arr.append(left[l])
            l += 1
        else:
            # If the left element is greater than the right element, then we have to switch
            if left[l] > right[r]:
                switch += 1

            sorted_arr.append(right[r])
            r += 1

    return sorted_arr, switch
        
def mergeSort(arr: list):
    if len(arr) <= 1:
        return arr, 0
    switch = 0

    m = floor(len(arr) / 2)
    l, l_switch = mergeSort(arr[:m])
    r, r_switch = mergeSort(arr[m:])

    switch += l_switch + r_switch

    sorted_arr, merge_flips = merge(l, r)
    switch += merge_flips

    return sorted_arr, switch

def main():
    arr = [1, 3, 5, 2, 4, 6]
    sorted_arr, switch = mergeSort(arr)
    print(f"Array: {arr}")
    print(f"Sorted Array: {sorted_arr}", f"Switched: {switch}")

if __name__ == "__main__":
    main()