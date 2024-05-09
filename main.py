def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document\n")
    char_count = get_letter_count(text)
    sorted = get_sorted_char_list(char_count)
    char_list_printer(sorted)
    print("--- End report ---")


def get_letter_count(words):
    lowered = words.lower()
    count = {}
    for i in lowered:
        if i in count:
            count[i] = count[i] + 1
        else:
            count[i] = 1
    return count

def get_sorted_char_list(char_dict):
    li = []
    for char in char_dict:
        if char.isalpha():
            li.append({'char': char, 'num': char_dict[char]})
    li.sort(reverse=True, key=sort_on)
    return li


def sort_on(dict):
    return dict["num"]


def char_list_printer(char_list):
    for item in char_list:
        print(f"The '{item["char"]}' character was found {item["num"]} times")


def get_num_words(words):
    return len(words.split())


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
