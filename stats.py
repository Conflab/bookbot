def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

def sort_char_count(char_dict):
    new_list = []
    for char in char_dict:
        new_list.append({"char": char, "num": char_dict[char]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list


def sort_on(items):
    return items["num"]