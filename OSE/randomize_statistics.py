import OSE.statistics
from OSE.fantasy_names import *
from OSE.minimum_class_requirement import MinRequirements


def roll_dices(dices_phrase: str):
    """

    :param dices_phrase: e.g. 3d6 or 2d12 or 1d6
    :return:
    """
    results = []
    hp = 0
    for result in range(int(dices_phrase[0])):
        dice = roll_dice(1, int(dices_phrase[-1]))
        results.append(dice)
        hp = sum(results)
    return hp


def generate_all_features():
    str_ = OSE.statistics.Strength()
    int_ = OSE.statistics.Intelligence()
    wis_ = OSE.statistics.Wisdom()
    dex_ = OSE.statistics.Dexterity()
    con_ = OSE.statistics.Constitution()
    cha_ = OSE.statistics.Charisma()
    # pr_ = PrimeRequisite()
    alg_ = OSE.statistics.Alignment()
    return str_, int_, wis_, dex_, con_, cha_, alg_#, pr_


def class_minimal_req_check(strength: OSE.statistics.Strength, intelligence: OSE.statistics.Intelligence,
                            wisdom: OSE.statistics.Wisdom, dexterity: OSE.statistics.Dexterity,
                            constitution: OSE.statistics.Constitution, charisma: OSE.statistics.Charisma,
                            debug: bool = False):
    if debug:
        print(strength.name_of_trait, strength.value)
        print(intelligence.name_of_trait, intelligence.value)
        print(wisdom.name_of_trait, wisdom.value)
        print(dexterity.name_of_trait, dexterity.value)
        print(constitution.name_of_trait, constitution.value)
        print(charisma.name_of_trait, charisma.value)
    list_of_available_class = []
    for char_class in dir(MinRequirements):
        if callable(getattr(MinRequirements, char_class)) and not char_class.startswith("_") and len(char_class) != 3:
            if debug:
                print(char_class)
            getattr(MinRequirements, char_class)()
            if strength.value >= MinRequirements.str and intelligence.value >= MinRequirements.int and\
                    wisdom.value >= MinRequirements.wis and dexterity.value >= MinRequirements.dex and\
                    constitution.value >= MinRequirements.con and charisma.value >= MinRequirements.cha:
                if debug:
                    print("Accepted Character")
                list_of_available_class.append(str(char_class))
            else:
                if debug:
                    print("Fail - NON available character")
    if debug:
        print(list_of_available_class)
    return list_of_available_class


def check_maximal_feature(strength: OSE.statistics.Strength, intelligence: OSE.statistics.Intelligence,
                          wisdom: OSE.statistics.Wisdom, dexterity: OSE.statistics.Dexterity,
                          constitution: OSE.statistics.Constitution, charisma: OSE.statistics.Charisma,
                          debug: bool = False):
    all_features = [(strength.name_of_trait, strength.value), (intelligence.name_of_trait, intelligence.value),
                    (wisdom.name_of_trait, wisdom.value), (dexterity.name_of_trait, dexterity.value),
                    (constitution.name_of_trait, constitution.value), (charisma.name_of_trait, charisma.value)]
    sorted_all_feature = sorted(all_features, key=lambda feature: feature[1], reverse=True)

    if debug:
        print(all_features)
        print(sorted_all_feature)
    #     print(all_features)
    #     print(type(max_feature), max_feature)

    # return max_feature


def generate_full_character():
    strength, intelligence, wisdom, dexterity, constitution, charisma, alignment = generate_all_features()
    list_of_available_class = class_minimal_req_check(strength, intelligence, wisdom, dexterity, constitution, charisma, False)
    prequste = check_maximal_feature(strength, intelligence, wisdom, dexterity, constitution, charisma, True)
    print(list_of_available_class)


generate_full_character()
# x = randomize_all_statistics()
# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])
# print(x[4])
# print(x[5])
# print(x[6])


