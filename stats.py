

def get_book_word_count(path):
    file_contents = 0
    with open(path) as book:
        file_contents = book.read()
    
    words = file_contents.split()
    count = len(words)

    return count

def get_character_count(path):
    file_contents = 0
    with open(path) as book:
        file_contents = book.read()
    
    char_set = {}
    for char in (file_contents.lower()):
        if char in char_set:
            char_set[char] += 1
        else:
            char_set[char] = 1

    return char_set

def sort_on(dict):
    return dict["count"]


def book_report(char_dict):
    char_list = []
    dict = {}

    for chars in char_dict:
        if chars.isalpha():
            dict["character"] = chars
            dict["count"] = char_dict[chars]
            char_list.append(dict)
            dict = {}

    char_list.sort(key=sort_on, reverse=True)
    
    char_report = ""
    for char in char_list:
        char_report += f"{char["character"]}: {char["count"]}\n"

    return char_report
