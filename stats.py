#Takes a filepath and returns the contents of the file as a string.
def get_book_text(filepath):
    #print(filepath.read())
    return filepath.read()

#Accepts text from a string, returns number of words in the string
def num_words(book):
    count = 0
    #print(book)
    list = book.split()
    for word in list:
        count += 1
    return (f'{count} total words')

#Returns count per character instead of total word count
def match(char, list):
    count = 0
    for i in list:
        if i == char:
            count += 1
    print(count)
    return count

#Accepts text from book as a string, returns number of times each character appears
#Includes symbols and spaces
def total_chars(book):
    char_count = {}

    for char in book:
        char_lower = char.lower()
        if char_lower in char_count: #char_lower is the key | the value on the right side of '=' will be the value associated with the key
            char_count[char_lower] += 1
        else:
            char_count[char_lower] = 1

    return char_count


#Display the result
def sort_dict(dict):
    #Get the value of the count for sorting
    def value_fetch(dict):
        return dict["count"]

    characters = []
    for key in dict:
        if key == ' ':
            continue
        characters.append({"char": key, "count": dict[key]})

    characters.sort(reverse=True, key=value_fetch)
    return characters

#Prettier formatting for the printout, no special characters.
def print_report(path, word_count, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Loop through your sorted list of character dictionaries
    for char_dict in char_list:
        # Only print if the character is alphabetical
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")
    
    print("============= END ===============")