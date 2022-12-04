def get_duplicate_values():
    c = [
        'vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw'
    ]
    a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dl = set()
    res = 0

    for x in c:
        first_part = x[0:int(len(x)/2)]
        second_part = x[int(len(x)/2):len(x)]
        for letter in first_part:
            if letter in second_part:
                dl.add(letter)

    for e in dl:
        res += a.rfind(e) + 1

    return res

print(get_duplicate_values())
