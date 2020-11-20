# The clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
# Your task is to make the 'past' function return the time converted to milliseconds.
# More examples in the test cases below.

def past(h, m, s):

    result = 0
    ms = 1000
    if h + m + s == 0:
        return result
    result = int(h) * 3600 * ms + int(m) * 60 * ms + int(s) * ms
    return result