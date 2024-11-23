from OSE.randomize_statistics import generate_base_characteristic_to_class
from OSE.character_classes.Fighter import Fighter
from OSE.character_classes.Acrobat import Acrobat
from OSE.character_classes.Assassin import Assassin
from OSE.character_classes.Barbarian import Barbarian

#ZROBIC BIBLIOTEKE DO PDF MOZE?!
dictionary_of_class_collection = {'acrobat': Acrobat, 'assassin': Assassin, 'barbarian': Barbarian,
                                  'bard': Fighter, 'cleric': Fighter, 'drow': Fighter, 'druid': Fighter,
                                  'duergar': Fighter, 'dwarf': Fighter, 'elf': Fighter, 'fighter': Fighter,
                                  'gnome': Fighter, 'halfelf': Fighter, 'halfling': Fighter,
                                  'halforc': Fighter, 'illusionist': Fighter, 'knight': Fighter,
                                  'magicuser': Fighter, 'paladin': Fighter, 'ranger': Fighter,
                                  'svirfneblin': Fighter, 'thief': Fighter}


def generate_hero(debug: bool = False):
    if debug:
        flag = True
    else:
        flag = False
    name_of_class, strength, intelligence, wisdom, dexterity, constitution, charisma, alignment \
        = generate_base_characteristic_to_class(flag)
    if debug:
        print("KLASA BOHATERA", name_of_class)
        print("SILA:", strength.value)
        print("INTELIGENCJA:", intelligence.value)
        print("MĄDROŚĆ:", wisdom.value)
        print("ZRĘCZNOŚĆ", dexterity.value)
        print("BUDOWA CIAŁA", constitution.value)
        print("CHARYZMA", charisma.value)
        print("CHARAKTER", alignment.alignment)

    hero = (dictionary_of_class_collection[name_of_class])(strength, intelligence, wisdom, dexterity, constitution,
                                                           charisma, alignment, False)

    ############################# HERE START CHARACTER CLASS GOES TO TEXT FILE #########################################

    data = [f"Imie bohatera: {hero.character_name}", f"Klasa bohatera: {hero.character_class}",
            f"Charakter bohatera: {hero.alignment.alignment}", f"Poziom bohatera: {hero.level}\n",
            "###################################\n", f"{hero.STR.name_of_trait}: {hero.STR.value}",
            f"{hero.INT.name_of_trait}: {hero.INT.value}", f"{hero.WIS.name_of_trait}: {hero.WIS.value}",
            f"{hero.DEX.name_of_trait}: {hero.DEX.value}", f"{hero.CON.name_of_trait}: {hero.CON.value}",
            f"{hero.CHA.name_of_trait}: {hero.CHA.value}\n", "###################################\n",
            "Rzuty obronne przeciw: ", f"Śmierci / Truciznom: {hero.death_poison}", f"Różdżką: {hero.magic_wands}",
            f"Paraliżowi / Petryfikacji: {hero.paralysis_petrify}", f"Zionięciu: {hero.breath_attacks}",
            f"Czarom / Kijom / Rózgą: {hero.spells_staves_rods}",
            f"Modyfikator do rzutów obronnych wynikający z Mądrości (wliczony): {hero.WIS.modifier_magic_saves}\n",
            "###################################\n", f"Punkty Życia: {hero.hit_points}",
            f"Modyfikator punktów życia (wliczony): {hero.CON.modifier_hit_points}\n",
            "###################################\n", f"Klasa Pancerza: {hero.armour_class}",
            f"Modyfikator Klasy Pancerza (wliczony): {hero.DEX.ac_modifier}\n", "###################################\n",
            f"Bonus do trafienia wręcz (TRAK0 + modyfikator): {hero.melee}",
            f"Modyfikator do trafienia wręcz (wliczone): {hero.STR.melee_modifier}\n",
            "###################################\n",
            f"Bonus do trafienia na dystans (TRAK0 + modyfikator): {hero.missile}",
            f"Modyfikator do trafienia na dystans (wliczone): {hero.DEX.missile_modifier}\n",
            "###################################\n", f"Modyfikator do inicjatywy: {hero.initiative}",
            f"Modyfikator do reakcji NPCów: ??????????? DO SPRAWDZENIA, {hero.CHA.NPC_reactions}\n",
            "###################################\n", f"Nasłuchiwanie przy drzwiach: {hero.listen_at_door}",
            f"Wywarzanie drzwi: {hero.open_door}", f"Znajdowanie sekretnytch drzwi: {hero.find_secret_door}",
            f"Wykrywanie Pułapek w pokojach:  {hero.find_room_trap}\n", "###################################\n",
            f"Aktualne złoto: {hero.gold}", f"Znnane języki: {hero.languages}"]

    ############################# HERE FINISH CHARACTER CLASS GOES TO TEXT FILE ########################################
    return data


generate_hero(False)
