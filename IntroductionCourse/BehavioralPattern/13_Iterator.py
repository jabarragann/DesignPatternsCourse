def count_to(count):

    numbers_in_german = ['eins','zwei','drei','vier','funf']
    iterator = zip(range(count),numbers_in_german)

    for position, number in iterator:

        yield number


for numb in count_to(10):
    print(numb)