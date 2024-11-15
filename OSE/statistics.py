from rolls import roll_dice


class Strength(object):
    def __init__(self):
        name_of_trait = "Siła"
        values_melee_modifiers = {3: -3, 4: -2, 5: -2, 6: -1, 7: -1, 8: -1,
                                  9: 0, 10: 0, 11: 0, 12: 0,
                                  13: 1, 14: 1, 15: 1, 16: 2, 17: 2, 18: 3}
        values_open_in_doors = {3: "1-in-6", 4: "1-in-6", 5: "1-in-6", 6: "1-in-6", 7: "1-in-6", 8: "1-in-6",
                                9: "2-in-6", 10: "2-in-6", 11: "2-in-6", 12: "2-in-6",
                                13: "3-in-6", 14: "3-in-6", 15: "3-in-6", 16: "4-in-6", 17: "4-in-6", 18: "5-in-6"}
        results = []
        for result in range(3):
            dice = roll_dice(1, 6)
            results.append(dice)
        self.name_of_trait = name_of_trait
        self.results = results
        self.value = sum(results)
        self.melee_modifier = values_melee_modifiers[self.value]
        self.values_open_in_doors = values_open_in_doors[self.value]

    def __str__(self):
        return (f"Wartość cechy {self.name_of_trait}: {self.value}, Wyniki rzutu koścmi {self.results}, "
                f"Modyfikator walki wręcz {self.melee_modifier}, "
                f"Otwieranie drzwi/krat: {self.values_open_in_doors}")


class Intelligence(object):
    def __init__(self):
        name_of_trait = "Inteligencja"
        values_literacy = {3: "Illiterate", 4: "Illiterate", 5: "Illiterate",
                           6: "Basic", 7: "Basic", 8: "Basic",
                           9: "Literate", 10: "Literate", 11: "Literate", 12: "Literate",
                           13: "Literate", 14: "Literate", 15: "Literate", 16: "Literate",
                           17: "Literate", 18: "Literate"}
        values_spoken_language = {3: "Native (Broken Speach)",
                                  4: "Native", 5: "Native", 6: "Native", 7: "Native", 8: "Native",
                                  9: "Native", 10: "Native", 11: "Native", 12: "Native",
                                  13: "Native +1 additional", 14: "Native +1 additional", 15: "Native +1 additional",
                                  16: "Native +2 additional", 17: "Native +2 additional", 18: "Native +3 additional"}
        results = []
        for result in range(3):
            dice = roll_dice(1, 6)
            results.append(dice)
        self.name_of_trait = name_of_trait
        self.results = results
        self.value = sum(results)
        self.modifier_literacy = values_literacy[self.value]
        self.values_spoken_language = values_spoken_language[self.value]

    def __str__(self):
        return (f"Wartość cechy {self.name_of_trait}: {self.value}, Wyniki rzutu koścmi {self.results},"
                f" Ilość znanych języków: {self.modifier_literacy},"
                f" Czytanie/Pisanie: {self.values_spoken_language}")


class Wisdom(object):
    def __init__(self):
        name_of_trait = "Mądrość"
        values_modifiers_magic_saves = {3: -3, 4: -2, 5: -2, 6: -1, 7: -1, 8: -1,
                                        9: 0, 10: 0, 11: 0, 12: 0,
                                        13: 1, 14: 1, 15: 1, 16: 2, 17: 2, 18: 3}
        results = []
        for result in range(3):
            dice = roll_dice(1, 6)
            results.append(dice)
        self.name_of_trait = name_of_trait
        self.results = results
        self.value = sum(results)
        self.modifier_magic_saves = values_modifiers_magic_saves[self.value]

    def __str__(self):
        return (f"Wartość cechy {self.name_of_trait}: {self.value}, Wyniki rzutu koścmi {self.results}, "
                f" Modyfikator rzutów obronnych {self.modifier_magic_saves} ")


class Dexterity(object):
    def __init__(self):
        name_of_trait = "Zręczność"
        values_ac_missile = {3: -3, 4: -2, 5: -2, 6: -1, 7: -1, 8: -1,
                             9: 0, 10: 0, 11: 0, 12: 0,
                             13: 1, 14: 1, 15: 1, 16: 2, 17: 2, 18: 3}
        values_initiative = {3: -2, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1,
                             9: 0, 10: 0, 11: 0, 12: 0,
                             13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 2}
        results = []
        for result in range(3):
            dice = roll_dice(1, 6)
            results.append(dice)
        self.name_of_trait = name_of_trait
        self.results = results
        self.value = sum(results)
        self.missile_modifier = values_ac_missile[self.value]
        self.ac_modifier = values_ac_missile[self.value]
        self.initiative_modifier = values_initiative[self.value]

    def __str__(self):
        return (f"Wartość cechy {self.name_of_trait}: {self.value}, Wyniki rzutu koścmi {self.results}, "
                f"Modyfikator klasy pancerza: {self.ac_modifier}, "
                f"Modyfikator ataku dystansowego: {self.missile_modifier}, "
                f"Nodyfikator inicjatywy: {self.initiative_modifier}")


class Constitution(object):
    def __init__(self):
        name_of_trait = "Kondycja"
        values_modifiers_hit_points = {3: -3, 4: -2, 5: -2, 6: -1, 7: -1, 8: -1,
                                       9: 0, 10: 0, 11: 0, 12: 0,
                                       13: 1, 14: 1, 15: 1, 16: 2, 17: 2, 18: 3}
        results = []
        for result in range(3):
            dice = roll_dice(1, 6)
            results.append(dice)
        self.name_of_trait = name_of_trait
        self.results = results
        self.value = sum(results)
        self.modifier_hit_points = values_modifiers_hit_points[self.value]

    def __str__(self):
        return (f"Wartość cechy {self.name_of_trait}: {self.value}, Wyniki rzutu koścmi {self.results}, "
                f" Modyfikator punktów życia {self.modifier_hit_points} ")


class Charisma(object):
    def __init__(self):
        name_of_trait = "Charyzma"
        values_retainers_max = {3: 1, 4: 2, 5: 2, 6: 3, 7: 3, 8: 3,
                                9: 4, 10: 4, 11: 4, 12: 4,
                                13: 5, 14: 5, 15: 5, 16: 6, 17: 6, 18: 7}
        values_retainers_loyalty = {3: 4, 4: 5, 5: 5, 6: 6, 7: 6, 8: 6,
                                    9: 7, 10: 7, 11: 7, 12: 7,
                                    13: 8, 14: 8, 15: 8, 16: 9, 17: 9, 18: 10}
        values_npc_reactions = {3: -2, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1,
                                9: 0, 10: 0, 11: 0, 12: 0,
                                13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 2}
        results = []
        for result in range(3):
            dice = roll_dice(1, 6)
            results.append(dice)
        self.name_of_trait = name_of_trait
        self.results = results
        self.value = sum(results)
        self.retainers_max = values_retainers_max[self.value]
        self.retainers_loyalty = values_retainers_loyalty[self.value]
        self.NPC_reactions = values_npc_reactions[self.value]

    def __str__(self):
        return (f"Wartość cechy {self.name_of_trait}: {self.value}, Wyniki rzutu koścmi {self.results}, "
                f"Maksymalna ilosc podwładnych: {self.retainers_max}, "
                f"Lojalność podwładnych: {self.retainers_loyalty}, "
                f"Reakcje NPC: {self.NPC_reactions}")


class PrimeRequisite(object):
    def __init__(self, input_value: int):
        self.name_of_trait = "Modyfikator XP"
        values_xp_modifiers = {3: -0.2, 4: -0.2, 5: -0.2, 6: -0.1, 7: -0.1, 8: -0.1,
                               9: 0, 10: 0, 11: 0, 12: 0,
                               13: 0.05, 14: 0.05, 15: 0.05, 16: 0.1, 17: 0.1, 18: 0.1}
        self.value = input_value
        self.modifier_xp_modifiers = values_xp_modifiers[self.value]

    def __str__(self):
        return (f"{self.name_of_trait} dla wartośći {self.value}, "
                f" Mnożnik punktów doświadczenia {self.modifier_xp_modifiers} ")


class Alignment(object):
    def __init__(self):
        self.name_of_trait = "Charakter"
        # alignment = ["Law", "Neutral", "Chaotic"]
        alignment = ["Praworządny", "Neutralny", "Chaotyczny"]
        alignment_selected = roll_dice(0, 2)
        self.alignment = alignment[alignment_selected]

    def __str__(self):
        return f"{self.name_of_trait}: {self.alignment}."
