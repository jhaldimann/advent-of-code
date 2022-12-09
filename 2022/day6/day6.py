def part1():
    l = 4
    i = open('data.txt','r').read()
    for c, _ in enumerate(i):
        s = i[c-l:c]
        if len(set(s)) == l:
            print(c)
            return


def part2():
    l = 14
    i = open('data.txt','r').read()
    for c, _ in enumerate(i):
        s = i[c-l:c]
        if len(set(s)) == l:
            print(c)
            return

part1()
part2()