from stats import get_book_text, num_words, match, total_chars, sort_dict, print_report
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
    
    with open(sys.argv[1]) as f:



        path = sys.argv[1]
        book_string = get_book_text(f)
        word_count = num_words(book_string)
        book_dict = total_chars(book_string)
        char_list = sort_dict(book_dict)

        print_report(path, word_count, char_list)

main()