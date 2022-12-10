def part1():
    input = open("data.txt","r").read().split('\n')
    res = []
    stacks = [
        ['T', 'R', 'G', 'W', 'Q', 'M', 'F', 'P'][::-1],
        ['R', 'F', 'H'][::-1],
        ['D', 'S', 'H', 'G', 'V', 'R', 'Z', 'P'][::-1],
        ['G', 'W', 'F', 'B', 'P', 'H', 'Q'][::-1],
        ['H', 'J', 'M', 'S', 'P'][::-1],
        ['L', 'P', 'R', 'S', 'H', 'T', 'Z', 'M'][::-1],
        ['L', 'M', 'N', 'H', 'T', 'P'][::-1],
        ['R', 'Q', 'D', 'F'][::-1],
        ['H', 'P', 'L', 'N', 'C', 'S', 'D'][::-1]
    ]

    for e in input:
        el = e.split(" ")
        for i in range(int(el[1])):
            stacks[int(el[5]) - 1].append(stacks[int(el[3]) - 1].pop())

    for i in stacks:
        res.append(i[-1])

    return res

print(part1())

def part2():
    input = open("data.txt","r").read().split('\n')
    res = []
    stacks = [
        ['T', 'R', 'G', 'W', 'Q', 'M', 'F', 'P'][::-1],
        ['R', 'F', 'H'][::-1],
        ['D', 'S', 'H', 'G', 'V', 'R', 'Z', 'P'][::-1],
        ['G', 'W', 'F', 'B', 'P', 'H', 'Q'][::-1],
        ['H', 'J', 'M', 'S', 'P'][::-1],
        ['L', 'P', 'R', 'S', 'H', 'T', 'Z', 'M'][::-1],
        ['L', 'M', 'N', 'H', 'T', 'P'][::-1],
        ['R', 'Q', 'D', 'F'][::-1],
        ['H', 'P', 'L', 'N', 'C', 'S', 'D'][::-1]
    ]

    for e in input:
        el = e.split(" ")

        tmp = stacks[int(el[3]) - 1]

        stacks[int(el[3]) - 1] = tmp[:-int(el[1])]
        stacks[int(el[5]) - 1].extend(tmp[-int(el[1]):])

    for i in stacks:
        res.append(i[-1])

    return res

print(part2())