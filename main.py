import sys
from stats import get_word_count, get_char_count, print_dictionary

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    content = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    count = get_word_count(content)
    print(f"Found {count} total words")
    print("----------- Character Count ----------")
    char_count = get_char_count(content)
    list_of_items = print_dictionary(char_count)
    for item in list_of_items:
        print(f"{item['char']}: {item['count']}")
    print("============ END ============")

main()