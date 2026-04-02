def max_char(text):
    counts = {}
    for char in text:
        if char.isalnum(): # ignore spaces/punctuation
            if char in counts:
                counts[char] = counts[char] + 1 # increase count
            else:
                counts[char] = 1 # first occurrence

    # find character with max count
    max_c = ''
    max_count = 0
    for char in counts:
        if counts[char] > max_count:
            max_count = counts[char]
            max_c = char

    return max_c, max_count


    