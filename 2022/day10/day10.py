def part1():
    x = 1
    s = 0
    counter = 0
    c = []

    for i in range(20, 260, 40):
        c.append(i)

    for l in open("data.txt","r").read().split('\n'):
        e = l.split(' ')
        if len(e) == 2:
            for i in range(2):
                counter = counter + 1
                if counter in c:
                    s = s + (x * counter)

            x += int(e[1])

        if e[0] == 'noop':
            counter = counter + 1
            if counter in c:
                s = s + (x * counter)

    return s

print(part1())