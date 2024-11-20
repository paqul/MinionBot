from OSE.randomize_statistics import generate_base_characteristic_to_class
from OSE.Fighter import Fighter

dictionary_of_class_collection = {'acrobat': Fighter, 'assassin': Fighter, 'barbarian': Fighter,
                                  'bard': Fighter, 'cleric': Fighter, 'drow': Fighter, 'druid': Fighter,
                                  'duergar': Fighter, 'dwarf': Fighter, 'elf': Fighter, 'fighter': Fighter,
                                  'gnome': Fighter, 'halfelf': Fighter, 'halfling': Fighter,
                                  'halforc': Fighter, 'illusionist': Fighter, 'knight': Fighter,
                                  'magicuser': Fighter, 'paladin': Fighter, 'ranger': Fighter,
                                  'svirfneblin': Fighter, 'thief': Fighter}

klasa_bohatera = generate_base_characteristic_to_class()
print("KLASA BOHATERA", klasa_bohatera)
hero = (dictionary_of_class_collection[klasa_bohatera])()
print(hero)


def generate_hero():
    hero = []
    data = []
    hero = Fighter()
    # if character_class == "fighter":
    #     hero = Fighter()
    # elif character_class == "cleric":
    #     hero = Cleric()
    # elif character_class == "thief":
    #     hero = Thief()
    # elif character_class == "magic_user":
    #     hero = MaticUser()
    data.append(hero.character_name)
    data.append(hero.character_class)
    data.append(hero.alignment)
    data.append(hero.level)
    data.append("###################################")
    # data.append(hero.STR.value)
    # data.append(hero.INT.value)
    # data.append(hero.WIS.value)
    # data.append(hero.DEX.value)
    # data.append(hero.CON.value)
    # data.append(hero.CHA.value)
    data.append(str(hero.STR))
    data.append(str(hero.INT))
    data.append(str(hero.WIS))
    data.append(str(hero.DEX))
    data.append(str(hero.CON))
    data.append(str(hero.CHA))
    data.append("###################################")
    data.append(hero.death_poison)
    data.append(hero.magic_wands)
    data.append(hero.paralysis_petrify)
    data.append(hero.breath_attacks)
    data.append(hero.spells_staves_rods)
    data.append(hero.WIS.modifier_magic_saves)
    data.append("###################################")
    data.append(hero.hit_points)
    data.append(hero.CON.modifier_hit_points)
    data.append("###################################")
    data.append(hero.armour_class)
    data.append(hero.DEX.ac_modifier)
    data.append("###################################")
    data.append(hero.melee)
    data.append(hero.STR.melee_modifier)
    data.append("###################################")
    data.append(hero.missile)
    data.append(hero.DEX.missile_modifier)
    data.append("###################################")
    data.append(hero.initiative)
    data.append(hero.CHA.NPC_reactions)
    data.append("###################################")
    data.append(hero.listen_at_door)
    data.append(hero.open_door)
    data.append(hero.find_secret_door)
    data.append(hero.find_room_trap)
    data.append("###################################")
    data.append(hero.gold)
    data.append(hero.languages)
    # print(hero.character_name)
    # print(hero.STR)
    # print(hero.INT)
    # print(hero.WIS)
    # print(hero.DEX)
    # print(hero.CON)
    # print(hero.CHA)
    # print(hero.melee)
    # print(hero.missile)
    # print(hero.hit_points)
    # print(hero.languages)
    return data
