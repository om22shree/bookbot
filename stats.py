def word_count(text):
    return len(text.split())

def char_count(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
                
def report_char_count(char_dict):
    rep_list = []
    for char, count in sorted(char_dict.items(), reverse=True, key=lambda item: item[1]):
        rep_list.append({"char":char, "num":count})
    return rep_list
        