from OSE.randomize_statistics import roll_dices, randomize_languages
from OSE.fantasy_names import randomize_fantasy_name
from OSE.statistics import PrimeRequisite
import OSE.statistics


class Fighter(object):
    def __init__(self, strength: OSE.statistics.Strength, intelligence: OSE.statistics.Intelligence,
                 wisdom: OSE.statistics.Wisdom, dexterity: OSE.statistics.Dexterity,
                 constitution: OSE.statistics.Constitution, charisma: OSE.statistics.Charisma,
                 alignment: OSE.statistics.Alignment, debug: bool = False):
        """
        Requirements: None
        Prime requisite: STR
        HitDice: 1d8
        Maximum level: 14
        Armour: Any, including shields
        Weapons: Any
        Languages: Alignment, Common
        """
        self.STR = strength
        self.INT = intelligence
        self.WIS = wisdom
        self.DEX = dexterity
        self.CON = constitution
        self.CHA = charisma
        self.ALG = alignment
        self.character_name = randomize_fantasy_name()
        self.character_class = "Wojownik"
        self.level = 1
        self.hit_points = 0
        self.requirements = None
        self.prime_requisite = PrimeRequisite(self.STR.value)
        self.max_lvl = 14
        self.languages = randomize_languages(self.INT.values_spoken_language)
        self.alignment = self.ALG

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
        self.armour_class = 10+self.DEX.ac_modifier
        self.death_poison = self.fighter_statistics[self.level][3]-self.WIS.modifier_magic_saves
        self.magic_wands = self.fighter_statistics[self.level][4]-self.WIS.modifier_magic_saves
        self.paralysis_petrify = self.fighter_statistics[self.level][5]-self.WIS.modifier_magic_saves
        self.breath_attacks = self.fighter_statistics[self.level][6]-self.WIS.modifier_magic_saves
        self.spells_staves_rods = self.fighter_statistics[self.level][7]-self.WIS.modifier_magic_saves
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
                    self.fighter_statistics[self.level][1]) + self.CON.modifier_hit_points
                # roll for hitpoints +/- mods
            else:
                break
