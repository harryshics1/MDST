"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    if int(x) % 2 == 0:
        return False
    else:
        return True


def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    if word == word[::-1]:
        return True
    else:
        return False


def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    odd_list = list()
    for i in numlist:
        if is_odd(i) == False:
            odd_list.append(i)
    return odd_list



def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    word_count = dict()
    for word in text.split():
        word_count[word] = word_count.get(word.lower(), 0) + 1
    
    return word_count


# testing 
print(is_odd(0))
print(is_odd(9))
print(is_odd(1))
print(is_palindrome("civic"))
print(is_palindrome("harry"))
print(is_palindrome("level"))
print(only_odds([1, 2, 3, 4, 5, 6]))
print(count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?"))







