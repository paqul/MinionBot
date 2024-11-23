from OSE.randomize_statistics import generate_base_characteristic_to_class
from OSE.Fighter import Fighter
#ZROBIC BIBLIOTEKE DO PDF MOZE?!
dictionary_of_class_collection = {'acrobat': Fighter, 'assassin': Fighter, 'barbarian': Fighter,
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

    # print(hero.character_name)
    # print(hero.character_class)
    # print(hero.alignment)
    # print(hero.level)

    ############################# HERE START CHARACTER CLASS GOES TO TEXT FILE #########################################
    data = []
    data.append(f"Imie bohatera: {hero.character_name}")
    data.append(f"Klasa bohatera: {hero.character_class}")
    data.append(f"Charakter bohatera: {hero.alignment.alignment}")
    data.append(f"Poziom bohatera: {hero.level}\n")
    data.append("###################################\n")
    data.append(f"{hero.STR.name_of_trait}: {hero.STR.value}")
    data.append(f"{hero.INT.name_of_trait}: {hero.INT.value}")
    data.append(f"{hero.WIS.name_of_trait}: {hero.WIS.value}")
    data.append(f"{hero.DEX.name_of_trait}: {hero.DEX.value}")
    data.append(f"{hero.CON.name_of_trait}: {hero.CON.value}")
    data.append(f"{hero.CHA.name_of_trait}: {hero.CHA.value}\n")
    data.append("###################################\n")
    data.append("Rzuty obronne przeciw: ")
    data.append(f"Śmierci / Truciznom: {hero.death_poison}")
    data.append(f"Różdżką: {hero.magic_wands}")
    data.append(f"Paraliżowi / Petryfikacji: {hero.paralysis_petrify}")
    data.append(f"Zionięciu: {hero.breath_attacks}")
    data.append(f"Czarom / Kijom / Rózgą: {hero.spells_staves_rods}")
    data.append(f"Modyfikator do rzutów obronnych wynikający z Mądrości (wliczony): {hero.WIS.modifier_magic_saves}\n")
    data.append("###################################\n")
    data.append(f"Punkty Życia: {hero.hit_points}")
    data.append(f"Modyfikator punktów życia (wliczony): {hero.CON.modifier_hit_points}\n")
    data.append("###################################\n")
    data.append(f"Klasa Pancerza: {hero.armour_class}")
    data.append(f"Modyfikator Klasy Pancerza (wliczony): {hero.DEX.ac_modifier}\n")
    data.append("###################################\n")
    data.append(f"Bonus do trafienia wręcz (TRAK0 + modyfikator): {hero.melee}")
    data.append(f"Modyfikator do trafienia wręcz (wliczone): {hero.STR.melee_modifier}\n")
    data.append("###################################\n")
    data.append(f"Bonus do trafienia na dystans (TRAK0 + modyfikator): {hero.missile}")
    data.append(f"Modyfikator do trafienia na dystans (wliczone): {hero.DEX.missile_modifier}\n")
    data.append("###################################\n")
    data.append(f"Modyfikator do inicjatywy: {hero.initiative}")
    data.append(f"Modyfikator do reakcji NPCów: ??????????? DO SPRAWDZENIA, {hero.CHA.NPC_reactions}\n")
    data.append("###################################\n")
    data.append(f"Nasłuchiwanie przy drzwiach: {hero.listen_at_door}")
    data.append(f"Wywarzanie drzwi: {hero.open_door}")
    data.append(f"Znajdowanie sekretnytch drzwi: {hero.find_secret_door}")
    data.append(f"Wykrywanie Pułapek w pokojach:  {hero.find_room_trap}\n")
    data.append("###################################\n")
    data.append(f"Aktualne złoto: {hero.gold}")
    data.append(f"Znnane języki: {hero.languages}")

    ############################# HERE FINISH CHARACTER CLASS GOES TO TEXT FILE ########################################
    return data


generate_hero(True)
