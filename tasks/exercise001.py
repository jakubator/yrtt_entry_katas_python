# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. 
# Your task will be to return the sum of the numbers that occur only once.
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15.
# More examples in the test cases below.

# Good luck!

from collections import defaultdict as dd


def repeats(arr):
    numbers_dict = dd(int)
    total_sum = 0
    for n in arr:
        numbers_dict[n] += 1

    for k, v in numbers_dict.items():
        if v == 1:
            total_sum += k

    return total_sum