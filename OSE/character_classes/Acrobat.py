from OSE.randomize_statistics import roll_dices, randomize_languages
from OSE.fantasy_names import randomize_fantasy_name
from OSE.statistics import PrimeRequisite
import OSE.statistics


class Acrobat(object):
    def __init__(self, strength: OSE.statistics.Strength, intelligence: OSE.statistics.Intelligence,
                 wisdom: OSE.statistics.Wisdom, dexterity: OSE.statistics.Dexterity,
                 constitution: OSE.statistics.Constitution, charisma: OSE.statistics.Charisma,
                 alignment: OSE.statistics.Alignment, debug: bool = False):
        """
        Requirements: None
        Prime requisite: DEX
        HitDice: 1d4
        Maximum level: 14
        Armour: Leather, no shields
        Weapons: Missiles weapon, dagger, sword, short sword, pole arm, spear, staff
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
        self.character_class = "Akrobata"
        self.level = 1
        self.hit_points = 0
        self.requirements = None
        self.prime_requisite = PrimeRequisite(self.DEX.value)
        self.max_lvl = 14
        self.languages = randomize_languages(self.INT.values_spoken_language)
        self.alignment = self.ALG

        #Level XP HD THAC0 D W P B S
        self.level_progression = {1:  [     0, "1d4", 0, 13, 14, 13, 16, 15],
                                  2:  [  1200, "2d4", 0, 13, 14, 13, 16, 15],
                                  3:  [  2400, "3d4", 0, 13, 14, 13, 16, 15],
                                  4:  [  4800, "4d4", 0, 13, 14, 13, 16, 15],
                                  5:  [  9600, "5d4", 2, 12, 13, 11, 14, 13],
                                  6:  [ 20000, "6d4", 2, 12, 13, 11, 14, 13],
                                  7:  [ 40000, "7d4", 2, 12, 13, 11, 14, 13],
                                  8:  [ 80000, "8d4", 2, 12, 13, 11, 14, 13],
                                  9:  [160000, "9d4", 5, 10, 11,  9, 12, 10],
                                  10: [280000, "9d4", 5, 10, 11,  9, 12, 10],
                                  11: [400000, "9d4", 5, 10, 11,  9, 12, 10],
                                  12: [520000, "9d4", 5, 10, 11,  9, 12, 10],
                                  13: [640000, "9d4", 7,  8,  9,  7, 10, 8],
                                  14: [760000, "9d4", 7,  8,  9,  7, 10, 8]
                                  }
        self.spells = None
        self.special_skills_names = ["Wspinaczka po pionowej powierzchni", "Spadanie", "Ukrycie w cieniu",
                                     "Ciche poruszanie", "Chodzenie po linie", "Uchylanie sie", "Skakanie",
                                     "Atak z przewrotem"]
        self.special_skills_description = ["Na każde 100 stóp wspinaczki wymagany jest jeden rzut."
                                           " Jeśli rzut się nie powiedzie, akrobata spada o połowe drogi,"
                                           " doznając obrażeń od upadku.",
                                           "Kiedy akrobaci są w stanie wykonać salto, nie odnoszą żadnych obrażeń od"
                                           " pierwszych 10 stóp upadku. Uszkodzenia spowodowane upadkiem z większej"
                                           " wysokości są zmniejszane o podany procent (zaokrąglając ułamki w dół)",
                                           "Akrobata musi być nieruchomy – "
                                           "atakowanie lub poruszanie się z ukrycia nie jest możliwe",
                                           "Akrobata może próbować przemknąć obok wrogów niezauważony",
                                           "Akrobaci mogą chodzić po linach, wąskich belkach i półkach skalnych"
                                           " z prędkością o połowę mniejszą niż zwykle. Wymagany jest rzut co 60 stóp."
                                           " Niepowodzenie oznacza, że akrobata upada i doznaje obrażeń od upadku."
                                           " Warunki środowiskowe mogą zmniejszyć szansę na sukces nawet do 20%."
                                           " Trzymanie drążka do równowagi zwiększa szansę na sukces o 10%.",
                                           "Podczas wycofywania się z walki wręcz umiejętność akrobaty do przewracania"
                                           " się niweluje zwykły bonus +2 do trafienia przeciwnika.",
                                           "Przy rozbiegu na 20 stóp akrobata może przeskoczyć dół lub przepaść "
                                           "o szerokości 10-stóp (lub 20-stopowy, gdy wspomaga go użycie tyczki)."
                                           " Również używając tyczki, akrobata może przeskoczyć 10-stopowy mur"
                                           " lub wskoczyć na 10-stopową półkę (np skalną). Odpowiednie tyczki do "
                                           "skoków to 10-stopowe tyczki, włócznie, kije.",
                                           "Używając umiejętności spadania lub skakania, akrobata może wykonać atak"
                                           " wręcz z przewrotem. Atak zadaje podwójne obrażenia, jeśli się powiedzie."
                                           " Przeciwko nieświadomemu przeciwnikowi akrobata zyskuje również"
                                           " +4 bouns do trafienia"]

        # Level | Climb sheer surface | Falling | Hide in shadows | Move silently | Tightrope walking
        # | Evasion | Jumping | Tumbling Attack
        self.special_skills = {1:  [87, 25, 10, 20, 60],
                               2:  [88, 25, 15, 25, 65],
                               3:  [89, 25, 20, 30, 70],
                               4:  [90, 33, 25, 35, 75],
                               5:  [91, 33, 30, 40, 80],
                               6:  [92, 33, 33, 43, 85],
                               7:  [93, 33, 36, 46, 90],
                               8:  [94, 50, 40, 50, 95],
                               9:  [95, 50, 43, 53, 99],
                               10: [96, 50, 46, 56, 99],
                               11: [97, 50, 50, 60, 99],
                               12: [98, 66, 53, 63, 99],
                               13: [99, 66, 56, 66, 99],
                               14: [99, 75, 60, 70, 99]
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
