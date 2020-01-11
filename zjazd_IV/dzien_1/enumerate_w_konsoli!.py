def my_enumerate(s):
    index = 0
    for element in s:
        yield (index, element)
        index += 1