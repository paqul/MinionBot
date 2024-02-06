from statistics import *


def roll_hit_points(dices_phrase: str):
    results = []
    hp = 0
    for result in range(int(dices_phrase[0])):
        dice = r(1, int(dices_phrase[-1]))
        results.append(dice)
        hp = sum(results)
    return hp


def randomize_all_statistics():
    STR = Strength()
    INT = Intelligence()
    DEX = Dexterity()
    CHA = Charisma()
    WIS = Wisdom()
    CON = Constitution()
    return STR, INT, DEX, CHA, WIS, CON


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
        self.STR, self.INT, self.DEX, self.CHA, self.WIS, self.CON = randomize_all_statistics()

        self.requirements = None
        self.prime_requisite = "STR"
        self.hit_dice = "1d8"
        self.max_lvl = 14
        self.armours = None
        self.weapons = None
        self.languages = "Alignment", "Common"

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
print(x.STR.value)
print(x.WIS.value)