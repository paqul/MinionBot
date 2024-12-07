from OSE.randomize_statistics import roll_dices, randomize_languages
from OSE.fantasy_names import randomize_fantasy_name
from OSE.statistics import PrimeRequisite
import OSE.statistics


class Drow(object):
    def __init__(self, strength: OSE.statistics.Strength, intelligence: OSE.statistics.Intelligence,
                 wisdom: OSE.statistics.Wisdom, dexterity: OSE.statistics.Dexterity,
                 constitution: OSE.statistics.Constitution, charisma: OSE.statistics.Charisma,
                 alignment: OSE.statistics.Alignment, debug: bool = False):
        """
        Requirements: Minimum INT 9
        Prime requisite: STR and WIS
        HitDice: 1d6
        Maximum level: 10
        Armour: Any including shields
        Weapons: Any
        Languages: Alignment, Common, Deepcommon, Elvish, Gnomish, the secret language of spiders
        """
        self.STR = strength
        self.INT = intelligence
        self.WIS = wisdom
        self.DEX = dexterity
        self.CON = constitution
        self.CHA = charisma
        self.ALG = alignment
        self.character_name = randomize_fantasy_name()
        self.character_class = "Drow"
        self.level = 1
        self.hit_points = 0
        self.requirements = None
        self.prime_requisite = PrimeRequisite(self.WIS.value)
        self.max_lvl = 10
        self.languages = randomize_languages(self.INT.values_spoken_language)
        self.alignment = self.ALG

        #Level XP HD THAC0 D W P B S
        self.level_progression = {1:  [     0, "1d6", 0, 12, 13, 13, 15, 12],
                                  2:  [  4000, "2d6", 0, 12, 13, 13, 15, 12],
                                  3:  [  8000, "3d6", 0, 12, 13, 13, 15, 12],
                                  4:  [ 16000, "4d6", 2, 10, 11, 11, 13, 10],
                                  5:  [ 32000, "5d6", 2, 10, 11, 11, 13, 10],
                                  6:  [ 64000, "6d6", 2, 10, 11, 11, 13, 10],
                                  7:  [120000, "7d6", 5,  8,  9,  9, 10,  8],
                                  8:  [250000, "8d6", 5,  8,  9,  9, 10,  8],
                                  9:  [400000, "9d6", 5,  8,  9,  9, 10,  8],
                                  10: [600000, "9d6", 7,  6,  7,  8,  8,  6],
                                  }
        self.spells = None
        self.special_skills_names = ["", "", "", "", "", "", "", ""]
        self.special_skills_description = ["", "", "", "", "", "", "", ""]

        # Level | x | x | x | x | x
        # | x | x | x
        self.special_skills = {1: [10, 10, 10, 10, 10],
                               2: [10, 10, 10, 10, 10],
                               3: [10, 10, 10, 10, 10],
                               4: [10, 10, 10, 10, 10],
                               5: [10, 10, 10, 10, 10],
                               6: [10, 10, 10, 10, 10],
                               7: [10, 10, 10, 10, 10],
                               8: [10, 10, 10, 10, 10],
                               9: [10, 10, 10, 10, 10],
                               10: [10, 10, 10, 10, 10],
                               11: [10, 10, 10, 10, 10],
                               12: [10, 10, 10, 10, 10],
                               13: [10, 10, 10, 10, 10],
                               14: [10, 10, 10, 10, 10]
                               }
        self.experience = self.level_progression[self.level][0]  # First level character
        self.roll_hp()
        self.thac0 = self.level_progression[self.level][2]  # Method of Ascending AC
        self.armour_class = 10+self.DEX.ac_modifier
        self.death_poison = self.level_progression[self.level][3]-self.WIS.modifier_magic_saves
        self.magic_wands = self.level_progression[self.level][4]-self.WIS.modifier_magic_saves
        self.paralysis_petrify = self.level_progression[self.level][5]-self.WIS.modifier_magic_saves
        self.breath_attacks = self.level_progression[self.level][6]-self.WIS.modifier_magic_saves
        self.spells_staves_rods = self.level_progression[self.level][7]-self.WIS.modifier_magic_saves
        self.melee = self.thac0+self.STR.melee_modifier
        self.missile = self.thac0+self.DEX.missile_modifier
        self.initiative = self.DEX.initiative_modifier
        self.listen_at_door = "2-to-6"
        self.open_door = self.STR.values_open_in_doors
        self.find_secret_door = "1-to-6"
        self.find_room_trap = "1-to-6"

        self.gold = roll_dices("3d6")  # roll for gold pieces
        self.armours = None
        self.weapons = None
        self.encumbrance = 0
        self.max_encumbrance = 1600

    def roll_hp(self):
        while True:
            if self.hit_points <= 0:
                self.hit_points = roll_dices(
                    self.level_progression[self.level][1]) + self.CON.modifier_hit_points
                # roll for hitpoints +/- mods
            else:
                break
