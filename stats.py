def get_num_words(text):
    word_array = text.split()
    return len(word_array)

def get_char_count(text):
    char_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def get_sorted_dict(dict):
    sorted_list = []
    for item in dict:
        new_dict = {}
        new_dict["char"] = item
        new_dict["num"] = dict[item]
        sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
        
        