def get_highest_calorie_elf():
    pos = 0
    calories = [[]]
    sums = []
    for e in open("data.txt","r").read().split('\n'):
        if e == '':
            pos = pos + 1
            calories.append([])
        else:
            calories[pos].append(int(e))

    for calorie in calories:
        sums.append(sum(calorie))

    return max(sums)


print(get_highest_calorie_elf())