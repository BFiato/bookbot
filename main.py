from stats import *

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

# def word_counter(file_contents):
   # return len(file_contents.split())
def main():
    #print( f"Found {get_num_words(get_book_text("books/frankenstein.txt"))} total words")
    #print(get_num_chars(get_book_text("books/frankenstein.txt")))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text('books/frankenstein.txt'))} total words")
    print("--------- Character Count -------")
    for item in sort_chars(get_num_chars(get_book_text("books/frankenstein.txt"))):
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()