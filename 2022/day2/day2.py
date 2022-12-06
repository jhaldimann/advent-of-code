def calculate_points():
    ans_player = 'ABC'
    ans_opp = 'XYZ'
    rps_value = 0
    rps_res = 0
    i = []

    for e in open("data.txt","r").read().split('\n'):
        i.append(e.split(' '))

    for e in i:
        rps_value += ans_opp.rfind(e[1]) + 1
        answer_player = ans_player.rfind(e[0])
        answer_elf = ans_opp.rfind(e[1])
        if (answer_elf - answer_player) % 3 == 1:
            rps_res += 6
        elif (answer_elf - answer_player) % 3 == 0:
            rps_res += 3

    return rps_res + rps_value

print(calculate_points())

def calculate_point_2():
    res = 0
    i = []
    ans_player = 'ABC'

    for e in open('data.txt','r').read().split('\n'):
        i.append(e.split(' '))

    for e in i:
        el = str(e[1])
        first = ans_player.rfind(e[0]) + 1
        if el == "X":
            res += (first - 2) % 3
        elif el == "Y":
            res += first + 2
        elif el == "Z":
            res += (first % 3) + 6

        res += 1
    return res


print(calculate_point_2())