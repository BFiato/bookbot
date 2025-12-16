from stats import get_num_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

# def word_counter(file_contents):
   # return len(file_contents.split())
def main():
    print( f"Found {get_num_words(get_book_text("books/frankenstein.txt"))} total words")
    
main()