from OSE.randomize_statistics import roll_dices, randomize_languages
from OSE.fantasy_names import randomize_fantasy_name
from OSE.statistics import PrimeRequisite
import OSE.statistics


class Druid(object):
    def __init__(self, strength: OSE.statistics.Strength, intelligence: OSE.statistics.Intelligence,
                 wisdom: OSE.statistics.Wisdom, dexterity: OSE.statistics.Dexterity,
                 constitution: OSE.statistics.Constitution, charisma: OSE.statistics.Charisma,
                 alignment: OSE.statistics.Alignment, debug: bool = False):
        """
        Requirements: None
        Prime requisite: WIS
        HitDice: 1d6
        Maximum level: 14
        Armour: Leather, wooden shield
        Weapons: Club, dagger, sling, spear, staff
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
        self.character_class = "Druid"
        self.level = 1
        self.hit_points = 0
        self.requirements = None
        self.prime_requisite = PrimeRequisite(self.WIS.value)
        self.max_lvl = 14
        self.languages = randomize_languages(self.INT.values_spoken_language)
        self.alignment = self.ALG

        #Level XP HD THAC0 D W P B S
        self.level_progression = {1:  [     0, "1d6", 0, 11, 12, 14, 16, 15],
                                  2:  [  2000, "2d6", 0, 11, 12, 14, 16, 15],
                                  3:  [  4000, "3d6", 0, 11, 12, 14, 16, 15],
                                  4:  [  7500, "4d6", 0, 11, 12, 14, 16, 15],
                                  5:  [ 12500, "5d6", 2,  9, 10, 12, 14, 12],
                                  6:  [ 20000, "6d6", 2,  9, 10, 12, 14, 12],
                                  7:  [ 35000, "7d6", 2,  9, 10, 12, 14, 12],
                                  8:  [ 60000, "8d6", 2,  9, 10, 12, 14, 12],
                                  9:  [ 90000, "9d6", 5,  6,  7,  9, 11,  9],
                                  10: [125000, "9d6", 5,  6,  7,  9, 11,  9],
                                  11: [200000, "9d6", 5,  6,  7,  9, 11,  9],
                                  12: [300000, "9d6", 5,  6,  7,  9, 11,  9],
                                  13: [750000, "9d6", 7,  3,  5,  7,  8,  7],
                                  14: [1500000, "9d6", 7,  3,  5,  7,  8,  7]
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
