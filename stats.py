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
def list_of_characters(character_dict):
    def sort_on(dict):
        return list(dict.values())[0]
    sorted_list = []
    for characters in character_dict:
        single_dict = {}
        amount = character_dict[characters]
        single_dict[characters] = amount
        sorted_list.append(single_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list