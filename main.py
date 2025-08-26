
from stats import get_num_words, get_num_chars, get_book_report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("""============ BOOKBOT ============
        Analyzing book found at books/frankenstein.txt...
        ----------- Word Count ----------""")
        content = get_book_text(sys.argv[1])
        word_count = get_num_words(content)
        print("--------- Character Count -------")
        char_count = get_num_chars(content)
        char_info= get_book_report(char_count)
        for c in char_info: 
            print(f"{c["char"]}: {c["num"]}")

main()