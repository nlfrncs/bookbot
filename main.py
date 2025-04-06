import sys
from stats import get_book_word_count
from stats import get_character_count
from stats import book_report

def get_book_text(path):
    file_contents = 0
    with open(path) as book:
        file_contents = book.read()
    
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    num_words = get_book_word_count(book_path)
    print(f"{num_words} words found in the document")
    test = (get_character_count(book_path))
    char_report = book_report(test)

    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{char_report}============= END ===============""")



main()