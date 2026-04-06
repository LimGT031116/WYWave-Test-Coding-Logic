# Time Complexity:
# Best case: O(n + m)
# Average case: O(n + m)
# Worst case: O(n + m)

# Space Complexity:
# O(n + min(n,m))

# Function to find intersection of two lists using a dictionary (hash map)
def list_intersection(list1, list2):
    map_dict = {}
    for item in list1:
        map_dict[item] = True  # Value doesn't matter, key existence is enough

    # Find intersection
    result = []
    for item in list2:
        if item in map_dict and item not in result:
            result.append(item)

    return result