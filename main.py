def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        nb_words = counts(text)
        nb_char = counts_char(text)
        print_report(book_path, nb_words, nb_char)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def counts(file_contents):
    words = file_contents.split()
    return len(words)

def counts_char(text):
    nb_char = {}
    lower_text = text.lower()
    for single_char in lower_text:
        if single_char in nb_char:
            nb_char[single_char] += 1
        else:
            nb_char[single_char] = 1
    return nb_char

def sort_on(dict):
    return dict["nb"]

def print_report(book_path, nb_words, nb_char):
    list_chars = []
    print(f"--- Begin report of {book_path} ---\n{nb_words} words found in the document\n")
    for one_char in nb_char:
        if one_char.isalpha():
            list_chars.append({"char": one_char, "nb": nb_char[one_char]})

    list_chars.sort(reverse=True, key=sort_on)

    for i in range(len(list_chars)):
        print(f"The '{list_chars[i]["char"]}' character was found {list_chars[i]["nb"]} times")
    print("--- End report ---")

main()