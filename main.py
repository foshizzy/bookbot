import sys
from stats import words_in_book
from stats import letters_in_book
from stats import sort_letters

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        book_text = get_book_text(sys.argv[1])
        num_words = words_in_book(book_text)
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        letter_list = letters_in_book(book_text)
        srt_chars = sort_letters(letter_list)
        for char in srt_chars:
           if char["letter"].isalpha() == True:
              print(f"{char["letter"]}: {char["count"]}")
    print("============= END ===============")

main()
