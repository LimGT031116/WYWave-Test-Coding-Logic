# Time Complexity:
# Best case: O(n + m)
# Average case: O(n + m)
# Worst case: O(n + m)
# where n = len(text1), m = len(text2)

# Space Complexity:
# O(k)
# where k = number of unique characters

def anagram_checker(text1, text2):
    counts_text1 = {}
    counts_text2 = {}

    # Count characters in text1
    for char in text1:
        if char.isalnum(): # ignore spaces/punctuation
            char_lower = char.lower() # ignore case
            if char_lower in counts_text1:
               counts_text1[char_lower] = counts_text1[char_lower] + 1
            else:
               counts_text1[char_lower] = 1

    # Count characters in text2
    for char in text2:
        if char.isalnum(): # ignore spaces/punctuation
            char_lower = char.lower() # ignore case
            if char_lower in counts_text2:
               counts_text2[char_lower] = counts_text2[char_lower] + 1
            else:
               counts_text2[char_lower] = 1

    # compare text1 count and text2 count
    return counts_text1 == counts_text2