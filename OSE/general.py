from OSE.character_classes import Fighter


def generate_fighter():
    fighter_0 = Fighter()
    data = []
    data.append(fighter_0.character_name)
    data.append(fighter_0.STR)
    data.append(fighter_0.INT)
    data.append(fighter_0.WIS)
    data.append(fighter_0.DEX)
    data.append(fighter_0.CON)
    data.append(fighter_0.CHA)
    data.append(fighter_0.melee)
    data.append(fighter_0.missile)
    data.append(fighter_0.hit_points)
    data.append(fighter_0.languages)
    print(fighter_0.character_name)
    print(fighter_0.STR)
    print(fighter_0.INT)
    print(fighter_0.WIS)
    print(fighter_0.DEX)
    print(fighter_0.CON)
    print(fighter_0.CHA)
    print(fighter_0.melee)
    print(fighter_0.missile)
    print(fighter_0.hit_points)
    print(fighter_0.languages)
    return data
