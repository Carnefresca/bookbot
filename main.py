from stats import number_of_words
from stats import get_book_text
from stats import number_of_characters

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = number_of_words(text)
    print(f"{num_words} words found in the document")
    
    print(number_of_characters(text))

main()