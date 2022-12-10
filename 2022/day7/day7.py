from collections import defaultdict
from pathlib import Path
import re

def part1():
    home = Path("/")
    d = defaultdict(int)
    res = 0
    ts = 70000000
    fs = 30000000

    regex = '^[0-9]+$'
    for l in open("data.txt","r").read().split('\n'):
        i = l.split()
        if len(i) == 3:
            home = (home / i[2]).resolve()
        else:
            if re.search(regex, i[0]):
                s = int(i[0])
                for path in [home, *home.parents]:
                    d[path] = d[path] + s

    for a in d.values():
        if a < 100000:
            res += a

    needed_space = fs - (ts - max(d.values()))
    res2 = []
    for a in d.values():
        if a > needed_space:
            res2.append(a)

    print(res, min(res2))

part1()