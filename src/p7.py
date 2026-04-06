# Time Complexity:
# Best case: O(1)
# Average case: O(log x)
# Worst case: O(log x)

# Space Complexity:
# O(1)

def integer_sqrt(x):
    # Use binary search

    if x == 0 or x == 1:
        return x

    l, r = 1, x // 2
    while l <= r:
        m = (l + r) // 2
        square = m * m

        if square == x:
            return m
        elif square < x:
            l = m + 1
        else:
            r = m - 1

    return -1