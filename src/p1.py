# Time Complexity:
# Best: O(n)
# Average: O(n^2)
# Worst: O(n^2)

# Space Complexity:
# O(1)

def sort_numbers(array):
    n = len(array)
    # Outer loop: controls the number of passes
    for outer in range(n - 1):
        swapped = False
        # Inner loop: the largest number in the current range will move to index n-1-outer
        for inner in range(n - 1 - outer):
            if array[inner] > array[inner + 1]:
                # Swap elements
                array[inner], array[inner + 1] = array[inner + 1], array[inner]
                swapped = True
        # If no swaps, array is sorted
        if not swapped:
            break
    return array