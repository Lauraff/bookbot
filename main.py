def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        words = counts(text)
        print(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def counts(file_contents):
    words = file_contents.split()
    return len(words)

main()