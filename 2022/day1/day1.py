def get_highest_calorie_elf():
    pos = 0
    calories = [[]]
    sums = []
    top_three = 0
    for e in open("data.txt","r").read().split('\n'):
        if e == '':
            pos = pos + 1
            calories.append([])
        else:
            calories[pos].append(int(e))

    for calorie in calories:
        sums.append(sum(calorie))

    for x in range(3):
        top_three += max(sums)
        sums.remove(max(sums))