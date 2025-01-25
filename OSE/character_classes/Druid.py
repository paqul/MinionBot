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
        # Level Divine Magic | 1 | 2 | 3 | 4 | 5
        self.spells = {1:  [1, 0, 0, 0, 0],
                       2:  [2, 0, 0, 0, 0],
                       3:  [2, 1, 0, 0, 0],
                       4:  [2, 2, 0, 0, 0],
                       5:  [2, 2, 1, 1, 0],
                       6:  [2, 2, 2, 1, 1],
                       7:  [3, 3, 2, 2, 1],
                       8:  [3, 3, 3, 2, 2],
                       9:  [4, 4, 3, 3, 2],
                       10: [4, 4, 4, 3, 3],
                       11: [5, 5, 4, 4, 3],
                       12: [5, 5, 5, 4, 4],
                       13: [6, 5, 5, 5, 4],
                       14: [6, 6, 5, 5, 5]
                       }
        self.special_skills_names = ["Niewrażliwość na urok", "Boska magia", "Używanie przedmiotów magicznych",
                                     "Magiczne badania", "Odporność na energie", "Identyfikacja", "Języki",
                                     "Przejście bez śladu", "Znajdowanie ścieżek ", "Zmiana kształtu"]
        self.special_skills_description = ["Druidzi 7. poziomu i wyżej są odporni na uroki wróżek i stworzeń leśnych"
                                           " (np. driad, rusałek)\n",
                                           "Niełaska bóstwa: Druidzi muszą być wierni zasadom swojego usposobienia i"
                                           " religii. Druidzi, którzy nie popadną w łaskę swojego bóstwa, mogą ponieść"
                                           " kary Rzucanie czarów: Druid może modlić się o otrzymanie czarów z natury."
                                           " Moc i liczba czarów dostępnych dla druida są określane przez poziom"
                                           " doświadczenia postaci. Lista czarów dostępnych dla druidów znajduje"
                                           " się na stronie 129. \n"
                                           "Druid musi nieść/posiadać święty symbol bóstwa - gałązka jemioły,"
                                           " którą postać musi zebrać\n",
                                           "Jako rzucający czary, druidzi mogą używać magicznych zwojów czarów ze"
                                           " swojej listy czarów. Mogą używać przedmiotów, których mogą używać jedynie"
                                           " osoby rzucające czary boskie (np. niektóre magiczne kostury), Druidzi"
                                           " nie mogą używać magicznych ksiąg ani tomów \n",
                                           "Druid dowolnego poziomu może poświęcić czas i pieniądze na badania"
                                           " magiczne. Pozwala im to tworzyć nowe zaklęcia lub inne magiczne efekty"
                                           " związane z ich bóstwem. Kiedy druid osiągnie 9. poziom, może również"
                                           " tworzyć magiczne przedmioty.\n",
                                           "Druidzi zyskują premię +2 do rzutów obronnych przeciwko"
                                           " elektryczności (błyskawicom) i ogniowi.\n",
                                           "Druidzi mogą identyfikować wszystkie rośliny i zwierzęta oraz potrafi"
                                           " rozpoznać/odróżnić czystą wodę\n",
                                           "Druidzi mówią tajemnym językiem znanym tylko ich sekcie. Na każdym poziomie"
                                           " powyżej 2 druid uczy się także języka używanego przez stworzenia"
                                           " lasów Sylvan (np. driady, zielone smoki, chochliki, treanty)\n",
                                           "Od 3 poziomu druid może przechodzić przez naturalne środowiska bez"
                                           " pozostawiania śladów. Postać jest również w stanie poruszać się przez"
                                           " zarośnięte obszary z normalną prędkością bez przeszkód.\n",
                                           "W drużynie z druidem szansa na zgubienie się w lesie wynosi tylko 1 do 6\n",
                                           "Na 7 poziomie druid zyskuje moc zmiany w formę gada, ptaka i ssaka"
                                           " (raz dziennie każde). Zwierzę może mieć dowolny rozmiar, do około"
                                           " dwukrotności wielkości normalnej formy druida. Jeśli druid stracił punkty"
                                           " życia, odzyskuje 1k4 punktów życia na poziom po zmianie w zwierzę."
                                           " Cały ekwipunek noszony przez druida zostaje wchłonięty do formy"
                                           " zwierzęcia i pojawia się ponownie, gdy druid zmienia się z powrotem."]

        # Level | x | x | x | x | x
        # | Charm Immunity | Divine Magic | Energy Resistance | Identification | Languages | Pass Without Trace |
        # Path-finding | Shape Change
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
