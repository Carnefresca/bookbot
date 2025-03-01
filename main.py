import sys
from stats import number_of_words
from stats import get_book_text
from stats import number_of_characters
from stats import list_of_characters


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    try:
        get_book_text(book)
    except FileNotFoundError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(book)
    num_words = number_of_words(text)
    character_dict = number_of_characters(text)
    sorted_list_of_chars = list_of_characters(character_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_list_of_chars:
        char = list(char_dict.keys())[0]
        if char.isalpha():
            count = char_dict[char]
            print(f"{char}: {count}")
    print("============= END ===============")
        
    

main()