def get_duplicate_series():
    res = 0
    res2 = 0

    for e in open("data.txt", "r").read().split('\n'):
        first = []
        second = []
        counter = 1

        for a in e.rstrip().split(","):
            counter += 1
            el = a.split('-')
            numbers = set(range(int(el[0]), int(el[1]) + 1))
            if counter % 2 == 0:
                second = numbers
            else:
                first = numbers

        if first.issubset(second) or second.issubset(first):
            res += 1

        if not first.isdisjoint(second):
            res2 += 1

    return [res, res2]

print(get_duplicate_series()) #475