from OSE.randomize_statistics import roll_dices, randomize_languages
from OSE.fantasy_names import randomize_fantasy_name
from OSE.statistics import PrimeRequisite
import OSE.statistics


class Paladin(object):
    def __init__(self, strength: OSE.statistics.Strength, intelligence: OSE.statistics.Intelligence,
                 wisdom: OSE.statistics.Wisdom, dexterity: OSE.statistics.Dexterity,
                 constitution: OSE.statistics.Constitution, charisma: OSE.statistics.Charisma,
                 alignment: OSE.statistics.Alignment, debug: bool = False):
        """
        Requirements: Minimum CHA 9
        Prime requisite: STR and WIS
        HitDice: 1d8
        Maximum level: 14
        Armour: Any including shields
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
        self.character_class = "Paladyn"
        self.level = 1
        self.hit_points = 0
        self.requirements = None
        self.prime_requisite = PrimeRequisite(self.STR.value)
        self.max_lvl = 14
        self.languages = randomize_languages(self.INT.values_spoken_language)
        self.alignment = self.ALG

        #Level XP HD THAC0 D W P B S
        self.level_progression = {1:  [     0, "1d8", 0, 10, 11, 12, 13, 14],
                                  2:  [  2750, "2d8", 0, 10, 11, 12, 13, 14],
                                  3:  [  5500, "3d8", 0, 10, 11, 12, 13, 14],
                                  4:  [ 12000, "4d8", 2,  8,  9, 10, 11, 12],
                                  5:  [ 24000, "5d8", 2,  8,  9, 10, 11, 12],
                                  6:  [ 45000, "6d8", 2,  8,  9, 10, 11, 12],
                                  7:  [ 95000, "7d8", 5,  6,  7,  8,  8, 10],
                                  8:  [175000, "8d8", 5,  6,  7,  8,  8, 10],
                                  9:  [350000, "9d8", 5,  6,  7,  8,  8, 10],
                                  10: [500000, "9d8", 7,  4,  5,  6,  6,  8],
                                  11: [650000, "9d8", 7,  4,  5,  6,  6,  8],
                                  12: [800000, "9d8", 7,  4,  5,  6,  6,  8],
                                  13: [950000, "9d8", 9,  2,  3,  4,  3,  6],
                                  14: [1100000, "9d8", 9,  2,  3,  4,  3,  6]
                                  }
        self.special_skills = None
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
        self.listen_at_door = "1-to-6"
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
