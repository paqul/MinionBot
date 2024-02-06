from statistics import *
from fantasy_names import *


def roll_dice(dices_phrase: str):
    results = []
    hp = 0
    for result in range(int(dices_phrase[0])):
        dice = r(1, int(dices_phrase[-1]))
        results.append(dice)
        hp = sum(results)
    return hp


def roll_alignment():
    # alignment = ["Law", "Neutral", "Chaotic"]
    alignment = ["Praworządny", "Neutralny", "Chaotyczny"]
    alignment_selected = r(0, 2)
    return alignment[alignment_selected]


def randomize_all_statistics():
    str_ = Strength()
    int_ = Intelligence()
    wis_ = Wisdom()
    dex_ = Dexterity()
    con_ = Constitution()
    cha_ = Charisma()
    return str_, int_, wis_, dex_, con_, cha_


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
        self.STR, self.INT, self.WIS, self.DEX, self.CON, self.CHA = randomize_all_statistics()

        self.character_name = randomize_fantasy_name()
        self.level = 1
        self.hit_points = 0
        self.requirements = None
        self.prime_requisite = PrimeRequisite(self.STR.value)
        self.max_lvl = 14
        self.languages = "Common "+self.INT.values_spoken_language
        self.alignment = roll_alignment()

        #Level XP HD THAC0 D W P B S
        self.fighter_statistics = {1:  [     0, "1d8", 0, 12, 13, 14, 15, 16],
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

        self.experience = self.fighter_statistics[self.level][0]  # First level character
        self.roll_hp()
        self.thac0 = self.fighter_statistics[self.level][2]  # Method of Ascending AC
        self.death_poison = self.fighter_statistics[self.level][3]-self.WIS.modifier_magic_saves
        self.magic_wands = self.fighter_statistics[self.level][4]-self.WIS.modifier_magic_saves
        self.paralysis_petrify = self.fighter_statistics[self.level][5]-self.WIS.modifier_magic_saves
        self.breath_attacks = self.fighter_statistics[self.level][6]-self.WIS.modifier_magic_saves
        self.spells_staves_rods = self.fighter_statistics[self.level][7]-self.WIS.modifier_magic_saves
        self.melee = self.thac0+self.STR.melee_modifier
        self.missile = self.thac0+self.DEX.missile_modifier
        self.initiative = self.DEX.initiative_modifier

        self.gold = roll_dice("3d6")  # roll for gold pieces
        self.armours = None
        self.weapons = None

    def roll_hp(self):
        while True:
            if self.hit_points <= 0:
                self.hit_points = roll_dice(
                    self.fighter_statistics[self.level][1]) + self.CON.modifier_hit_points  # roll for hitpoints +/- mods
            else:
                break


# fighter_0 = Fighter()
# print(fighter_0)
# print(fighter_0.STR)
# print(fighter_0.INT)
# print(fighter_0.WIS)
# print(fighter_0.DEX)
# print(fighter_0.CON)
# print(fighter_0.CHA)
# print(fighter_0.prime_requisite)
# print(fighter_0.alignment)
# print(fighter_0.experience)
# print(fighter_0.hit_points)
# print(fighter_0.thac0)
# print(fighter_0.death_poison)
# print(fighter_0.magic_wands)
# print(fighter_0.paralysis_petrify)
# print(fighter_0.breath_attacks)
# print(fighter_0.spells_staves_rods)
# print(fighter_0.melee)
# print(fighter_0.missile)
# print(fighter_0.initiative)
# print(fighter_0.gold)