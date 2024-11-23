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
        Requirements: Minimum DEX 9
        Prime requisite: CON and STR
        HitDice: 1d8
        Maximum level: 14
        Armour: Leather, chainmail, shields
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
        self.character_class = "Barbarzyńca"
        self.level = 1
        self.hit_points = 0
        self.requirements = None
        self.prime_requisite = PrimeRequisite(self.STR.value)
        self.max_lvl = 14
        self.languages = randomize_languages(self.INT.values_spoken_language)
        self.alignment = self.ALG

        #Level XP HD THAC0 D W P B S
        self.martial_statistics = {1:  [     0, "1d8", 0, 10, 13, 12, 15, 16],
                                   2:  [  2500, "2d8", 0, 10, 13, 12, 15, 16],
                                   3:  [  5000, "3d8", 0, 10, 13, 12, 15, 16],
                                   4:  [ 10000, "4d8", 2,  8, 11, 10, 13, 13],
                                   5:  [ 18500, "5d8", 2,  8, 11, 10, 13, 13],
                                   6:  [ 37000, "6d8", 2,  8, 11, 10, 13, 13],
                                   7:  [ 85000, "7d8", 5,  6,  9,  8, 10, 10],
                                   8:  [140000, "8d8", 5,  6,  9,  8, 10, 10],
                                   9:  [270000, "9d8", 5,  6,  9,  8, 10, 10],
                                   10: [400000, "9d8", 7,  4,  7,  6,  8,  7],
                                   11: [530000, "9d8", 7,  4,  7,  6,  8,  7],
                                   12: [660000, "9d8", 7,  4,  7,  6,  8,  7],
                                   13: [790000, "9d8", 9,  3,  5,  4,  5,  5],
                                   14: [920000, "9d8", 9,  3,  5,  4,  5,  5]
                                   }
        self.special_skills = None
        self.experience = self.martial_statistics[self.level][0]  # First level character
        self.roll_hp()
        self.thac0 = self.martial_statistics[self.level][2]  # Method of Ascending AC
        self.armour_class = 10+self.DEX.ac_modifier
        self.death_poison = self.martial_statistics[self.level][3]-self.WIS.modifier_magic_saves
        self.magic_wands = self.martial_statistics[self.level][4]-self.WIS.modifier_magic_saves
        self.paralysis_petrify = self.martial_statistics[self.level][5]-self.WIS.modifier_magic_saves
        self.breath_attacks = self.martial_statistics[self.level][6]-self.WIS.modifier_magic_saves
        self.spells_staves_rods = self.martial_statistics[self.level][7]-self.WIS.modifier_magic_saves
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
                    self.martial_statistics[self.level][1]) + self.CON.modifier_hit_points
                # roll for hitpoints +/- mods
            else:
                break
