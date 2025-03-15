def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    result = {}
    for char in text.lower():
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def print_dictionary(dictionary):
    list_of_items = []
    for key, value in dictionary.items():
        if key.isalpha():
            list_of_items.append({"char": key, "count": value})
    list_of_items.sort(key=lambda x: x["count"], reverse=True)
    return list_of_items
        