from stats import number_of_words
from stats import get_book_text
from stats import number_of_characters
from stats import list_of_characters

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = number_of_words(text)
    character_dict = number_of_characters(text)
    sorted_list_of_chars = list_of_characters(character_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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