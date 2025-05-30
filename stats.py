def word_count(text: str) -> int:
    '''
    Counts the number of words in a given text.
    '''
    return len(text.split())

def count_unique_chars(text: str) -> dict:
    '''
    Counts the occurrences of each character in the text. Treats upper and lower case
    letters as identical.

    Returns a dictionary with characters as keys and counts as values.
    '''
    char_counts = {}

    for character in text.lower():
        if (character in char_counts):
            char_counts[character] += 1
        else:
            char_counts[character] = 1
    
    return char_counts

def count_from_tuple(x: tuple) -> int:
    '''
    Helper function to get the count from a (char, count) tuple.
    Used as "key" for sorting.
    '''
    return x[1]

def sort_char_counts(char_counts: dict) -> list:
    '''
    Sorts a dict of characters and counts into a list of dicts,
    where the char and count are stored.

    The list has the dicts sorted by count in descending order.
    '''
    char_count_tuples = [(char, count) for char, count in char_counts.items()]

    char_count_tuples.sort(key=count_from_tuple, reverse=True)

    final_dict_list = [{"char": x[0], "num": x[1]} for x in char_count_tuples]
    return final_dict_list