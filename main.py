def read_book(path_to_book):
    with open(path_to_book) as f:
        contents = f.read()
        return contents

def count_words(string):
    return len(string.split())

def count_chars(book):
    dict = {}
    for char in book:
        lowered = char.lower()
        if lowered in dict:
            dict[lowered] += 1
        else:
            dict[lowered] = 1
    return dict
    
def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(dict):
    dict_list = []
    for char in dict:
        dict_list.append({"char": char, "num": dict[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def print_report(path, word_count, char_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    dict_list = dict_to_sorted_list(char_dict)
    for item in dict_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def main():
    path = "books/frankenstein.txt"
    contents = read_book(path)
    print(count_words(contents))
    print(count_chars(contents))
    print_report(path, count_words(contents), count_chars(contents))

if __name__=="__main__":
    main()