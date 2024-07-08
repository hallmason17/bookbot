
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
    

def main():
    contents = read_book("books/frankenstein.txt")
    print(count_chars(contents))

if __name__=="__main__":
    main()