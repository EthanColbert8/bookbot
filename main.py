import sys
import stats

def get_book_text(filepath : str) -> str:
    '''
    Reads the contents of a file (presumed to be text) and returns it as a string.
    '''
    with open(filepath, 'r') as f:
        text = f.read()
    return text

if (__name__ == "__main__"):
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    
    num_words = stats.word_count(book_text)
    char_counts = stats.count_unique_chars(book_text)
    sorted_char_counts = stats.sort_char_counts(char_counts)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_count in sorted_char_counts:
        if (char_count["char"].isalpha()):
            print(f"{char_count["char"]}: {char_count["num"]}")
    
    print("============= END ===============")