import re
from collections import deque

def part1():
    a, b = open("data.txt","r").read().split('\n\n')

    stacks = [
        ['T', 'R', 'G', 'W', 'Q', 'M', 'F', 'P'],
        ['R', 'F', 'H'],
        ['D', 'S', 'H', 'G', 'V', 'R', 'Z', 'P'],
        ['G', 'W', 'F', 'B', 'P', 'H', 'Q'],
        ['H', 'J', 'M', 'S', 'P'],
        ['L', 'P', 'R', 'S', 'H', 'T', 'Z', 'M'],
        ['L', 'M', 'N', 'H', 'T', 'P'],
        ['R', 'Q', 'D', 'F'],
        ['H', 'P', 'L', 'N', 'C', 'S', 'D']
    ]

    for e in b.split('\n'):
        el = e.split(" ")
        number_of_el = int(el[1])
        origin = int(el[3]) - 1
        destination = int(el[5]) - 1
        for i in range(0, number_of_el):
            stacks[destination].append(stacks[origin][0])
            stacks[origin].pop(0)

    res = []
    for e in stacks:
        res.append(e[0])

    print(res)
part1()
