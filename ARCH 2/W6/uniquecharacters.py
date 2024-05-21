def unique_chars_dict(word):
    dicts = dict()
    for char in word:
        if char not in dicts:
            dicts[char] = char

    unique_count = 0
    for dict_value in dicts.values():
        unique_count += 1

    return unique_count





def unique_chars_set(word):
    sets = set()

    for char in word:
        sets.add(char)

    unique_count = 0
    for set_value in sets:
        unique_count += 1

    return unique_count

if __name__ == '__main__':
    input_word = input("Enter a word to count unique characters: ")
    print(unique_chars_dict(input_word))
    print(unique_chars_set(input_word))
