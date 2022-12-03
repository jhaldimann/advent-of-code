def calculate_points():
    # A -> Rock -> 0 B -> Paper -> 1 C -> Scissors -> 3
    ans_player = 'ABC'
    ans_opp = 'XYZ'
    rps_value = 0
    rps_res = 0
    i = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]
    for e in i:
        rps_value += ans_player.rfind(e[0]) + 1
        answer_player = ans_player.rfind(e[0])
        answer_elf = ans_opp.rfind(e[1])
        # Same answer
        if answer_player == answer_elf:
            rps_res += 3
        # Lose
        elif answer_player - answer_elf % 3 == 0:
            rps_res += 0
        # Win
        elif answer_player - answer_elf % 3 == 1:
            rps_res += 6
    return rps_res + rps_value

print(calculate_points())
