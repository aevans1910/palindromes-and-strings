#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    half_1 = 0
    if len(text) > 0:
        half_2 = len(text)-1
    else:
        half_2 = len(text)
    
    while half_1 < half_2:
        while text[half_1] not in string.ascii_letters:
            half_1 += 1
        while text[half_2] not in string.ascii_letters:
            half_2 -= 1
        
        temp1 = text[half_2].lower()
        temp2 = text[half_1].lower()

        if temp1 != temp2:
            return False
        half_1 += 1
        half_2 -= 1
    
    return True

def is_palindrome_recursive(text, half_1=None, half_2=None):
    if half_1 == None and half_2 == None:
        half_1 = 0
        if len(text) > 0:
            half_2 = len(text)-1
        else:
            half_2 = len(text)
    if half_1 < half_2:
        while text[half_1] not in string.ascii_letters:
            half_1 += 1
        while text[half_2] not in string.ascii_letters:
            half_2 -= 1
        
        temp1 = text[half_1].lower()
        temp2 = text[half_2].lower()
        if temp1 != temp2:
            return False
        half_1 += 1
        half_2 -= 1
        return is_palindrome_recursive(text, half_1, half_2)
        
    return True

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()