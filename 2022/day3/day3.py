def get_duplicate_values():
    c = []
    d = []
    a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = 0
    res2 = 0

    for e in open("data.txt","r").read().split('\n'):
        c.append(e.split('\n')[0])

    for x in c:
        first_part = set(x[0:int(len(x)/2)])
        second_part = set(x[int(len(x)/2):len(x)])

        for i in first_part.intersection(second_part):
            res += a.rfind(i) + 1


    d.extend(c[i:i+3] for i in range(0, len(c), 3))
    for el in d:

        e = set(el[0])
        f = set(el[1])
        g = set(el[2])

        for z in e.intersection(f).intersection(g):
            res2 += a.rfind(z) + 1

    return [res, res2]

print(get_duplicate_values())



