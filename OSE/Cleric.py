from OSE.randomize_statistics import randomize_all_statistics, roll_dices
from OSE.fantasy_names import randomize_fantasy_name
from OSE.statistics import PrimeRequisite


class Cleric(object):
    def __init__(self):
        """
        Requirements: None
        Prime requisite: WIS
        HitDice: 1d6
        Maximum level: 14
        Armour: Any, including shields
        Weapons: Any blunt weapon
        Languages: Alignment, Common
        """
        self.STR, self.INT, self.WIS, self.DEX, self.CON, self.CHA, self.ALG = randomize_all_statistics()

        self.character_name = randomize_fantasy_name()
        self.character_class = "Cleric"
        self.level = 1
        self.hit_points = 0
        self.requirements = None
        self.prime_requisite = PrimeRequisite(self.WIS.value)
        self.max_lvl = 14
        self.languages = "Common "+self.INT.values_spoken_language
        self.alignment = self.ALG

        #Level XP HD THAC0 D W P B S
        self.cleric_statistics = {1:  [     0, "1d6", 0, 11, 12, 14, 16, 15],
                                  2:  [  1200, "2d6", 0, 11, 12, 14, 16, 15],
                                  3:  [  2400, "3d6", 0, 11, 12, 14, 16, 15],
                                  4:  [  4800, "4d6", 0, 11, 12, 14, 16, 15],
                                  5:  [  9600, "5d6", 2,  9, 10, 12, 14, 12],
                                  6:  [ 20000, "6d6", 2,  9, 10, 12, 14, 12],
                                  7:  [ 40000, "7d6", 2,  9, 10, 12, 14, 12],
                                  8:  [ 80000, "8d6", 2,  9, 10, 12, 14, 12],
                                  9:  [160000, "9d6", 5,  6,  7,  9, 11,  9],
                                  10: [280000, "9d6", 5,  6,  7,  9, 11,  9],
                                  11: [400000, "9d6", 5,  6,  7,  9, 11,  9],
                                  12: [520000, "9d6", 5,  6,  7,  9, 11,  9],
                                  13: [640000, "9d6", 7,  3,  5,  7,  8,  7],
                                  14: [760000, "9d6", 7,  3,  5,  7,  8,  7]
                                  }

        self.experience = self.cleric_statistics[self.level][0]  # First level character
        self.roll_hp()
        self.thac0 = self.cleric_statistics[self.level][2]  # Method of Ascending AC
        self.armour_class = 10+self.DEX.ac_modifier
        self.death_poison = self.cleric_statistics[self.level][3]-self.WIS.modifier_magic_saves
        self.magic_wands = self.cleric_statistics[self.level][4]-self.WIS.modifier_magic_saves
        self.paralysis_petrify = self.cleric_statistics[self.level][5]-self.WIS.modifier_magic_saves
        self.breath_attacks = self.cleric_statistics[self.level][6]-self.WIS.modifier_magic_saves
        self.spells_staves_rods = self.cleric_statistics[self.level][7]-self.WIS.modifier_magic_saves
        self.melee = self.thac0+self.STR.melee_modifier
        self.missile = self.thac0+self.DEX.missile_modifier
        self.initiative = self.DEX.initiative_modifier
        self.listen_at_door = "1-to-6"
        self.open_door = self.STR.values_open_in_doors
        self.find_secret_door = "1-to-6"
        self.find_room_trap = "1-to-6"

        self.gold = roll_dices("3d6")  # roll for gold pieces
        self.armours = None
        self.weapons = None

    def roll_hp(self):
        while True:
            if self.hit_points <= 0:
                self.hit_points = roll_dices(
                    self.cleric_statistics[self.level][1]) + self.CON.modifier_hit_points  # roll for hitpoints +/- mods
            else:
                break