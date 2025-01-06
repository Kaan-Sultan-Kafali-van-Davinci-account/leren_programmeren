def check_even_number(number:int) -> bool:
    return number % 2 == 0

def reverse_string_words(phrase:str) -> str:
    words = phrase.split()
    reversed = words[::-1]
    reversed_phrase = ' '.join(reversed)
    return reversed_phrase

def get_glyph_amount(string:str) -> int:
    string_set = set(string)
    string_len = len(string_set)
    return string_len

def get_average_words_length(string:str) -> float:
    split_string = string.split()
    
    count = 0
    for word in split_string:
        count += len(word)

    average_words_length = count / len(split_string)
    return average_words_length

def get_tafels(tafel:int, collumns:int=10) -> None:
    for collumn in range(1, collumns+1):
        answer = collumn * tafel
        print(f'{collumn} x {tafel} = {answer}')