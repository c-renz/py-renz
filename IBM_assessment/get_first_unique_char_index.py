def get_unique_character_index(s):
    char_count = {}

    # Count each character's occurrences
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the index of the first unique character
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i + 1

    return -1


print(get_unique_character_index("hackthegame"))
