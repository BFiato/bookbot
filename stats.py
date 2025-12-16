def get_num_words(file_contents): 
    num_of_words = len(file_contents.split())
    return num_of_words
def get_num_chars(file_contents):
    num_chars = {}
    contents_lower = file_contents.lower()
    for letter in contents_lower:
        if letter in num_chars:
            num_chars[letter] +=1
        else:
            num_chars[letter] =1
    return num_chars
def sort_on(items):
    return items["num"]
def sort_chars(num_chars):
    dicts_list = []
    for key, value in num_chars.items():
        dicts_list.append({"char": key, "num": value}) 
    dicts_list.sort(reverse=True, key=sort_on)
    return dicts_list
