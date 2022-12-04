def get_duplicate_series():
    res = 0
    for e in open("input.txt","r").read().split('\n'):
        first = []
        second = []
        counter = 0
        for a in e.split(','):
            counter += 1
            el = a.split('-')
            numbers = list(range(int(el[0]), int(el[1]) + 1))
            if counter % 2 == 0:
                first = numbers
            else:
                second = numbers

        if str(first).strip('[]') in str(second) or str(second).strip('[]') in str(first):
            res = res + 1
    return res

print(get_duplicate_series())