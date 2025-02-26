def number_of_words(book_text):
    word_count = 0
    for words in book_text.split():
        word_count += 1
    return word_count
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
def number_of_characters(text):
    characters = {}
    for letters in text.lower():
        if letters in characters:
            characters[letters] += 1
        else:
            characters[letters] = 1
    return characters