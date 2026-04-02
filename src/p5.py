# Time Complexity:
# Best case: O(n + m)
# Average case: O(n + m)
# Worst case: O(n + m)

# Space Complexity:
# O(n + m)

# Function to find symmetric difference of two lists using a dictionary (hash map)
def symmetric_difference(list1, list2):
    map_dict = {}
    for item in list1:
        map_dict[item] = True   # Value doesn't matter, key existence is enough

    result = []
    for item in list2:
        if item not in map_dict:
            result.append(item) # it's only in list2
        else:
            del map_dict[item]  # it's in both, remove from map

    for item in map_dict:
        result.append(item) # The leftover items from list1

    return result