import sys
from stats import get_word_count, get_char_count, sort_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path)

    print("----------- Word Count ----------")
    print(f"Found {get_word_count(text)} total words")

    print("--------- Character Count -------")
    char_dict = get_char_count(text)

    char_count_list = sort_char_count(char_dict)
    for k in char_count_list:
        if k['char'].isalpha():
            print(f"{k['char']}: {k['num']}")

main()