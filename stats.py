def words_in_book(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def letters_in_book(book_text):
    char_count = {}
    for char in book_text:
        lowered_char = char.lower()
        if lowered_char in char_count:
            char_count[lowered_char] += 1
        else:
            char_count[lowered_char] = 1
    return char_count

def sort_on(dict):
    return dict["count"]

def sort_letters(char_dict):
    dict_list = []
    for char in char_dict:
        dict_list.append({"letter": char, "count":char_dict[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
