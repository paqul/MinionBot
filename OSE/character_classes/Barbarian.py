from OSE.randomize_statistics import roll_dices, randomize_languages
from OSE.fantasy_names import randomize_fantasy_name
from OSE.statistics import PrimeRequisite
import OSE.statistics


class Barbarian(object):
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
        self.level_progression = {1:  [     0, "1d8", 0, 10, 13, 12, 15, 16],
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
        self.spells = None
        self.special_skills_names = ["Zwinna walka", "Wspinaczka po pionowej powierzchni", "Ukrywanie się w zaroślach",
                                     "Ciche poruszanie", "Leczenie trucizn", "Strach przed magią",
                                     "Zbieractwo i łowiectwo", "Uderzenie w niezniszczalne potwory"]

        self.special_skills_description = ["Po uzyskaniu 4 poziomu, barbarzyńca dostaje bonus +1 do Klasy Pancerza."
                                           " Dostaje bonus +2 do Klasy Pancerza na poziomie 6,"
                                           " bonus +3 do Klasy Pancerza na poziomie 8 i"
                                           " bonus +4 do Klasy Pancerza na poziomie 10",
                                           "Dotyczy tylko powierzchni naturalnych (np. pnie drzew, naturalne clify), "
                                           "Na każde 100 stóp wspinaczki wymagany jest jeden rzut."
                                           " Jeśli rzut się nie powiedzie, skrytobójca spada o połowe drogi,"
                                           " doznając obrażeń od upadku.",
                                           "Barbarzyńca musi być nieruchomy – "
                                           "atakowanie lub poruszanie się z ukrycia nie jest możliwe"
                                           "Barbarzyńca może próbować przemknąć obok wrogów niezauważony",
                                           "Na pustkowiu barbarzyńca może zbierać zioła, aby sporządzić odtrutkę na"
                                           " naturalne trucizny. Wyleczenie zajmuje jedną turę na postać."
                                           " Każdy podmiot może wykonać drugi rzut obronny przeciwko truciźnie,"
                                           " aby zakończyć efekty.",
                                           "Barbarzyńcy nie ufają magii i odmawiają świadomego używania lub poddawania"
                                           " się wpływowi zaklęć lub magicznych przedmiotów. Barbarzyńcy akceptują"
                                           " boską magię związaną z religią plemienną.",
                                           "Drużyna z barbarzyńcą odnosi sukces w zbieractwie z szansą 2 na 6 i"
                                           " znajduje ofiarę podczas polowania z szansą 5 na 6",
                                           "Barbarzyńca 4. poziomu lub wyższego jest w stanie uderzyć potwory,"
                                           " które normalnie można zranić tylko magią"]

        # Level | Agile Fighting | Climb sheer surface | Hide in undergrowth | Move silently
        # | Cure Poison | Fear of Magic | Foraging and Hunting | Strike Invulnerable Monsters
        self.special_skills = {1:  [0, 87, 10, 20],
                               2:  [0, 88, 15, 25],
                               3:  [0, 89, 20, 30],
                               4:  [1, 90, 25, 35],
                               5:  [1, 91, 30, 37],
                               6:  [2, 92, 33, 40],
                               7:  [2, 93, 36, 42],
                               8:  [3, 94, 40, 44],
                               9:  [3, 95, 43, 46],
                               10: [4, 96, 46, 48],
                               11: [4, 97, 50, 50],
                               12: [4, 98, 53, 50],
                               13: [4, 99, 56, 50],
                               14: [4, 99, 60, 50]
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
