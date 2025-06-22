import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    book_text = ""
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    print("----------- Word Count ----------")
    text = get_book_text(book_filepath)
    num_words = count_words(text)

    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    character_counts = count_characters(text)
    sorted_characters = sort_characters(character_counts)
    for entry in sorted_characters:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()