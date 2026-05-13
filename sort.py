

def bubble_sort(arr):

    n = len(arr)

    # Outer loop for each pass
    for i in range(n):
        swapped = False # Flag to detect if any swap occurs

    # Inner loop for comparing adjacent elements
        for j in range(0, n - i - 1):
            # Compare and swap if elements are out of order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

             # If no swaps occurred, the list is already sorted
        if not swapped:
            break
    return arr