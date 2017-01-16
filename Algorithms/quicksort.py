"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    idx_high = len(array) - 1
    idx_low = 0
    idx_pivot = idx_high

    while idx_low < idx_high:
        if array(idx_low) > array(idx_high):
            tmp = array(idx_high)
            

    return []


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)

