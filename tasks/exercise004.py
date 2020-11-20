# Move the first letter of each word to the end of it, then add "ay" 
# to the end of the word. Leave punctuation marks untouched.

import string as s


def pig_it(text):

    suffix = "ay"
    sentence = []
    list_of_words = text.split(' ')

    for word in list_of_words:
        idx = -1
        while word[idx] in s.punctuation:
            idx -= 1
        idx = len(word) + idx + 1
        sentence.append(word[1:idx] + word[0] + suffix + word[idx:])

    result = ' '.join(sentence)
    return result
