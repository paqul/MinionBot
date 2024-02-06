from rolls import r


def roll_hit_points(dices_phrase: str):
    results = []
    hp = 0
    for result in range(int(dices_phrase[0])):
        dice = r(1, int(dices_phrase[-1]))
        results.append(dice)
        hp = sum(results)
    return hp


class Fighter(object):
    def __init__(self):
        """
        Requirements: None
        Prime requisite: STR
        HitDice: 1d8
        Maximum level: 14
        Armour: Any, including shields
        Weapons: Any
        Languages: Alignment, Common
        """

        """
        Fighter Level Progression
            Saving Throws
            Level XP HD THAC0 D W P B S
            1 0 1d8 19 [0] 12 13 14 15 16
            2 2,000 2d8 19 [0] 12 13 14 15 16
            3 4,000 3d8 19 [0] 12 13 14 15 16
            4 8,000 4d8 17 [+2] 10 11 12 13 14
            5 16,000 5d8 17 [+2] 10 11 12 13 14
            6 32,000 6d8 17 [+2] 10 11 12 13 14
            7 64,000 7d8 14 [+5] 8 9 10 10 12
            8 120,000 8d8 14 [+5] 8 9 10 10 12
            9 240,000 9d8 14 [+5] 8 9 10 10 12
            10 360,000 9d8+2* 12 [+7] 6 7 8 8 10
            11 480,000 9d8+4* 12 [+7] 6 7 8 8 10
            12 600,000 9d8+6* 12 [+7] 6 7 8 8 10
            13 720,000 9d8+8* 10 [+9] 4 5 6 5 8
            14 840,000 9d8+10* 10 [+9] 4 5 6 5 8
            """

        #Level XP HD THAC0 D W P B S
        fighter_statistics = {1:  [     0, "1d8", 0, 12, 13, 14, 15, 16],
                              2:  [  1200, "2d8", 0, 12, 13, 14, 15, 16],
                              3:  [  2400, "3d8", 0, 12, 13, 14, 15, 16],
                              4:  [  4800, "4d8", 2, 10, 11, 12, 13, 14],
                              5:  [  9600, "5d8", 2, 10, 11, 12, 13, 14],
                              6:  [ 20000, "6d8", 2, 10, 11, 12, 13, 14],
                              7:  [ 40000, "7d8", 5,  8,  9, 10, 11, 12],
                              8:  [ 80000, "8d8", 5,  8,  9, 10, 11, 12],
                              9:  [160000, "9d8", 5,  8,  9, 10, 11, 12],
                              10: [280000, "9d8", 7,  6,  7,  8,  8, 10],
                              11: [400000, "9d8", 7,  6,  7,  8,  8, 10],
                              12: [520000, "9d8", 7,  6,  7,  8,  8, 10],
                              13: [640000, "9d8", 9,  4,  5,  6,  5, 8],
                              14: [760000, "9d8", 9,  4,  5,  6,  5, 8]
                              }
        roll_hit_points(fighter_statistics[1][1])


x = Fighter()
print(x)