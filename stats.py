def get_num_words(content):
    word_list = content.split()
    total = len(word_list)
    print(f"Found {total} total words")

def get_num_chars(content):
    chars = {}
    for t in content:
        lowercase_char = t.lower()
        if (lowercase_char in chars):
            chars[lowercase_char] += 1
        else: 
            chars[lowercase_char] = 1
    
    return chars

def get_book_report(char_count):
    formattedCharCounts = []
    for c in char_count:
        temp_dictonary = {}
        if c.isalpha():
            temp_dictonary["char"] = c
            temp_dictonary["num"] = char_count[c]
            formattedCharCounts.append(temp_dictonary)
    formattedCharCounts.sort(key=lambda x: x['num'], reverse=True)
    return formattedCharCounts
   

    