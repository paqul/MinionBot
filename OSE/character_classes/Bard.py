from OSE.randomize_statistics import roll_dices, randomize_languages
from OSE.fantasy_names import randomize_fantasy_name
from OSE.statistics import PrimeRequisite
import OSE.statistics


class Bard(object):
    def __init__(self, strength: OSE.statistics.Strength, intelligence: OSE.statistics.Intelligence,
                 wisdom: OSE.statistics.Wisdom, dexterity: OSE.statistics.Dexterity,
                 constitution: OSE.statistics.Constitution, charisma: OSE.statistics.Charisma,
                 alignment: OSE.statistics.Alignment, debug: bool = False):
        """
        Requirements: Minimum DEX 9, Minimum INT 9
        Prime requisite: CHA
        HitDice: 1d6
        Maximum level: 14
        Armour: Leather, chainmail, no shields
        Weapons: Missiles weapon, one-handed melee weapon
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
        self.character_class = "Bard"
        self.level = 1
        self.hit_points = 0
        self.requirements = None
        self.prime_requisite = PrimeRequisite(self.CHA.value)
        self.max_lvl = 14
        self.languages = randomize_languages(self.INT.values_spoken_language)
        self.alignment = self.ALG

        #Level XP HD THAC0 D W P B S
        self.level_progression = {1:  [     0, "1d6", 0, 13, 14, 13, 16, 15],
                                  2:  [  2000, "2d6", 0, 13, 14, 13, 16, 15],
                                  3:  [  4000, "3d6", 0, 13, 14, 13, 16, 15],
                                  4:  [  8000, "4d6", 0, 13, 14, 13, 16, 15],
                                  5:  [ 16000, "5d6", 2, 12, 13, 11, 14, 13],
                                  6:  [ 32000, "6d6", 2, 12, 13, 11, 14, 13],
                                  7:  [ 64000, "7d6", 2, 12, 13, 11, 14, 13],
                                  8:  [120000, "8d6", 2, 12, 13, 11, 14, 13],
                                  9:  [240000, "9d6", 5, 10, 11,  9, 12, 10],
                                  10: [360000, "9d6", 5, 10, 11,  9, 12, 10],
                                  11: [480000, "9d6", 5, 10, 11,  9, 12, 10],
                                  12: [600000, "9d6", 5, 10, 11,  9, 12, 10],
                                  13: [720000, "9d6", 7,  8,  9,  7, 10, 8],
                                  14: [840000, "9d6", 7,  8,  9,  7, 10, 8]
                                  }

        # Level Divine Magic | 1 | 2 | 3 | 4 |
        self.spells = {1:  [0, 0, 0, 0],
                       2:  [1, 0, 0, 0],
                       3:  [2, 0, 0, 0],
                       4:  [3, 0, 0, 0],
                       5:  [3, 1, 0, 0],
                       6:  [3, 2, 0, 0],
                       7:  [3, 3, 0, 0],
                       8:  [3, 3, 1, 0],
                       9:  [3, 3, 2, 0],
                       10: [3, 3, 3, 0],
                       11: [3, 3, 3, 1],
                       12: [3, 3, 3, 2],
                       13: [3, 3, 3, 3],
                       14: [4, 4, 3, 3]
                       }
        self.special_skills_names = ["Anty urok", "Boska magia", "Używanie przedmiotów magicznych", "Zachwyt", "Języki",
                                     "Wiedza"]
        self.special_skills_description = ["Podczas gdy bard gra muzykę i śpiewa, sojusznicy w promieniu 30 stóp są"
                                           " odporni na magiczne efekty pieśni i zwodnicze moce leśnych stworzeń"
                                           " lub wróżek. Sojusznicy, którzy są już pod wpływem takiej magii,"
                                           " mogą wykonać kolejny rzut obronny z premią +4",
                                           "Niełaska bóstwa: Bardowie muszą być wierni zasadom swojego usposobienia i"
                                           " religii. Bardowie, którzy nie popadną w łaskę swojego bóstwa, mogą ponieść"
                                           " kary Rzucanie czarów: Gdy bard udowodni swoją wiarę (od 2. poziomu),"
                                           " postać może modlić się o otrzymanie czarów. Moc i liczba czarów dostępnych"
                                           " dla barda są określane przez poziom doświadczenia. Lista czarów dostępnych"
                                           " dla bardów jest taka sama jak dla druidów.",
                                           "Jako rzucający czary, bardowie mogą używać magicznych zwojów czarów ze"
                                           " swojej listy czarów. Mogą również używać dowolnych przedmiotów,"
                                           " których mogą używać tylko druidzi.",
                                           "Grając muzykę i śpiewając, bard może fascynować poddanych w promieniu"
                                           " 30 stóp. Ta umiejętność nie działa w walce. Liczba poddanych: "
                                           "Do 2HD stworzeń na poziom barda jest dotkniętych. Bard może wybrać"
                                           " konkretną osobę lub grupę (w takim przypadku dotknięte osoby są określane"
                                           " losowo)\nRodzaje poddanych: Na 1. poziomie bard może fascynować osoby. "
                                           "Na 4. poziomie zwierzęta również mogą być dotknięte. Na 7. poziomie potwory"
                                           " mogą być dotknięte. \nEfekt: Każdy poddany musi rzucić rzut obronny"
                                           " przeciwko czarom lub zostanie zafascynowany, w następujący sposób: "
                                           "\nPochłonięty: Uwaga zafascynowanych poddanych jest w pełni skupiona"
                                           " na występie barda, dopóki trwa on. \nPodążanie: Bard może chodzić podczas"
                                           " gry. Zafascynowane poddane będą podążać za nim. \nPrzerwania: Jeśli występ"
                                           " zostanie przerwany (np. przez głośny hałas lub przemoc), fascynacja"
                                           " natychmiast się kończy. \nZaczarowane Poddane: Jeśli bard występuje przez"
                                           " co najmniej jedną turę i występ kończy się bez przerwy, zafascynowane"
                                           " poddane mogą zostać objęte głębszym urokiem. Każdy Poddany musi wykonać"
                                           " kolejny rzut obronny przeciwko czarom (z premią +2) lub zostać zaczarowany"
                                           " przez jedną turę na każdy poziom u Barda: \nPrzyjaźń: Oczarowani poddani"
                                           " uważają Barda za zaufanego przyjaciela i sojusznika i staną w jego obronie"
                                           "\nRozkazy: Jeśli dzielą ten sam język, zaczarowane Poddane będą wykonywać"
                                           " polecenia Barda. \nCharakter: Polecenia, które są sprzeczne z naturą"
                                           " lub charakterem zaczarowanego stworzenia, mogą zostać zignorowane. \n"
                                           "Rozkazy samobójcze: Zaczarowane Poddane nigdy nie wykonują rozkazów"
                                           " samobójczych lub ewidentnie szkodliwych.",
                                           "Bardowie uczą się nowych języków w miarę awansu na kolejne poziomy. Na"
                                           " każdym parzystym poziomie powyżej 3. (tj. 4., 6., 8. itd.) gracz może"
                                           " wybrać dodatkowy język. W ten sposób bardowie mogą nauczyć się tajnego"
                                           " języka druidów.",
                                           "Od 2. poziomu bard ma 2-do-6 szans na poznanie wiedzy o potworach,"
                                           " magicznych przedmiotach lub bohaterach baśni ludowych lub legend."
                                           " Ta umiejętność może być używana do identyfikacji natury i"
                                           " mocy magicznych przedmiotów"]

        # Level | x | x | x | x | x
        # | Anti-Charm | Divine Magic | Using Magic Items | Enchantment | Languages | Lore
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
