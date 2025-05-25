from stats import get_num_words,get_char_count,get_sorted_dict
from sys import argv, exit

def main():
    if len(argv) == 2:
        book_path = argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        char_count = get_char_count(text)
        sorted_list = get_sorted_dict(char_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for d in sorted_list:
            if d["char"].isalpha() == False:
                pass
            else:
                print(f"{d["char"]}: {d["num"]}")
        print("============= END ===============")
    else:
        raise Exception("Usage: python3 main.py <path_to_book>")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

try:
    main()
except Exception as e:
    print(e)
    exit(1)

