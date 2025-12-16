import sys
from stats import *

if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
else:
    book_path = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path} ...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(book_path))} total words")
    print("--------- Character Count -------")
    for item in sort_chars(get_num_chars(get_book_text(book_path))):
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()