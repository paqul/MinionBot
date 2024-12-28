from OSE.randomize_statistics import roll_dices, randomize_languages
from OSE.fantasy_names import randomize_fantasy_name
from OSE.statistics import PrimeRequisite
import OSE.statistics


class Assassin(object):
    def __init__(self, strength: OSE.statistics.Strength, intelligence: OSE.statistics.Intelligence,
                 wisdom: OSE.statistics.Wisdom, dexterity: OSE.statistics.Dexterity,
                 constitution: OSE.statistics.Constitution, charisma: OSE.statistics.Charisma,
                 alignment: OSE.statistics.Alignment, debug: bool = False):
        """
        Requirements: None
        Prime requisite: DEX
        HitDice: 1d4
        Maximum level: 14
        Armour: Leather, shields
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
        self.character_class = "Skrytobójca"
        self.level = 1
        self.hit_points = 0
        self.requirements = None
        self.prime_requisite = PrimeRequisite(self.DEX.value)
        self.max_lvl = 14
        self.languages = randomize_languages(self.INT.values_spoken_language)
        self.alignment = self.ALG

        #Level XP HD THAC0 D W P B S
        self.level_progression = {1:  [     0, "1d4", 0, 13, 14, 13, 16, 15],
                                  2:  [  1500, "2d4", 0, 13, 14, 13, 16, 15],
                                  3:  [  3000, "3d4", 0, 13, 14, 13, 16, 15],
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
        self.special_skills_names = ["Skrytobójstwo", "Wspinaczka po pionowej powierzchni", "Nasłuchiwanie",
                                     "Ukrycie w Cieniu", "Ciche poruszanie", "Przebieranie się", "Najemnicy",
                                     "Zatruwanie"]
        self.special_skills_description = ["Podczas ataku na nieświadomego humanoida od tyłu, skrytobójca otrzymuje"
                                           " premię +4 do trafienia. Jeśli atak się powiedzie, ofiara musi wykonać rzut"
                                           " obronny przeciwko śmierci z karą zależną od poziomu skrytobójcy. Jeśli"
                                           " rzut obronny się nie powiedzie, ofiara zostaje natychmiast zabita,"
                                           " w przeciwnym razie atak skrytobójcy zadaje normalne obrażenia."
                                           "Kto może zostać zamordowany? - ludzie / półludzie każdego poziomu oraz"
                                           " humanoidalne potwory o maksymalnej wartości "
                                           "HD 4+1 (istoty nieożywione są odporne).",
                                           "Na każde 100 stóp wspinaczki wymagany jest jeden rzut."
                                           " Jeśli rzut się nie powiedzie, skrytobójca spada o połowe drogi,"
                                           " doznając obrażeń od upadku.",
                                           "W cichym otoczeniu (np. poza walką) skrytobójca może próbować podsłuchiwać"
                                           " przy drzwiach lub słyszeć dźwięki czegoś zbliżającego się"
                                           " (np. wędrującego potwora).",
                                           "Skrytobójca musi być nieruchomy – "
                                           "atakowanie lub poruszanie się z ukrycia nie jest możliwe",
                                           "Skrytobójca może próbować przemknąć obok wrogów niezauważony",
                                           "Postacie dowolnej klasy mogą się przebierać, ale skrytobójcy są mistrzami"
                                           " w tej sztuce - potrafią tworzyć przebrania, które przechodzą nawet przez"
                                           " wnikliwą kontrolę. Szansa na wykrycie: Każdy, kogo skrytobójca spotka,"
                                           " ma 2% szansy na zauważenie przebrania. Ten rzut powtarza się raz na każdy"
                                           " kolejny dzień spotkania. Pozowanie jako inna klasa, rasa lub płeć: "
                                           "Zwiększa szansę na wykrycie o 2% za każdą zmianę. Wzrost i waga: Przebranie"
                                           " może zmieniać wzrost (do 3 stóp niższy lub 5 stóp wyższy) lub wagę"
                                           " (nieco szczuplejszy, znacznie bardziej masywny)",
                                           "Skrytobójcy 1-3 poziomu nie mogą zatrudniać wasali, najemników ani "
                                           "specjalistów. Od 4 poziomu skrytobójca może zatrudniać innych skrytobójców"
                                           " niższego poziomu. Od 8 poziomu skrytobójca może zatrudniać złodziei,"
                                           " a od 12 poziomu dowolny typ postaci.",
                                           "Ofiary otrucia przez skrytobójce otrzymują karę -2 do rzutu obronnego."
                                           ]

        # Level | Assassination | Climb sheer surface | Hear noise | Hide in shadows | Move silently
        # | Disguise | Hirelings | Poison
        self.special_skills = {1:  [ 0, 87, "2-in-6", 10, 20],
                               2:  [ 0, 88, "2-in-6", 15, 25],
                               3:  [ 0, 89, "3-in-6", 20, 30],
                               4:  [-1, 90, "3-in-6", 25, 35],
                               5:  [-1, 91, "3-in-6", 30, 40],
                               6:  [-2, 92, "3-in-6", 33, 43],
                               7:  [-2, 93, "4-in-6", 36, 46],
                               8:  [-3, 94, "4-in-6", 40, 50],
                               9:  [-3, 95, "4-in-6", 43, 53],
                               10: [-4, 96, "4-in-6", 46, 56],
                               11: [-4, 97, "5-in-6", 50, 60],
                               12: [-5, 98, "5-in-6", 53, 63],
                               13: [-5, 99, "5-in-6", 56, 66],
                               14: [-6, 99, "5-in-6", 60, 70]
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
        self.listen_at_door = self.special_skills[self.level][2]
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
