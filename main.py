from stats import word_count, char_count, report_char_count
import sys

def get_book_text(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        return f.read()
    return ""


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")
    rpeort = report_char_count(char_count(get_book_text(sys.argv[1])))
    for item in rpeort:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()