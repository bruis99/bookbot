def main():
    book_path = "books/frankenstein.txt"
    file_contents = book_text(book_path)
    num_words = get_num_words(file_contents)
    chars_count = count_char(file_contents)
    sort_rep = sorted_report(chars_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the doucment\n")
    for char_dict in sort_rep:
        print(f"The {char_dict["char"]} character was found {char_dict["num"]} times")
    print("--- End report ---")
def book_text(book_path):    
    with open(book_path) as f:
        contents = f.read()
        print(contents)
        return contents
    
def get_num_words(file_contents):
        words = file_contents.split()
        return len(words)    

def count_char(file_contents):
    chars = {}
    for c in file_contents:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def sort_on(chars_count):
    return chars_count["num"]

def sorted_report(chars_count):
    char_list = []
    for char, count in chars_count.items():
            char_dict = {"char" : char, "num": count}
            char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

main()