from OSE.statistics import *
from OSE.fantasy_names import *
from OSE.minimum_class_requirement import MinRequirements


def roll_dices(dices_phrase: str):
    results = []
    hp = 0
    for result in range(int(dices_phrase[0])):
        dice = roll_dice(1, int(dices_phrase[-1]))
        results.append(dice)
        hp = sum(results)
    return hp


def randomize_all_statistics():
    str_ = Strength()
    int_ = Intelligence()
    wis_ = Wisdom()
    dex_ = Dexterity()
    con_ = Constitution()
    cha_ = Charisma()
    # pr_ = PrimeRequisite()
    alg_ = Alignment()
    return str_, int_, wis_, dex_, con_, cha_, alg_#, pr_


def class_selection_based_on_stats(debug: bool = False):
    STR, INT, WIS, DEX, CON, CHA, ALG = randomize_all_statistics()
    if debug:
        print(STR.name_of_trait, STR.value)
        print(INT.name_of_trait, INT.value)
        print(WIS.name_of_trait, WIS.value)
        print(DEX.name_of_trait, DEX.value)
        print(CON.name_of_trait, CON.value)
        print(CHA.name_of_trait, CHA.value)
    list_of_available_class = []
    for i in dir(MinRequirements):
        if callable(getattr(MinRequirements, i)) and not i.startswith("_") and len(i) != 3:
            if debug:
                print(i)
            getattr(MinRequirements, i)()
            if STR.value >= MinRequirements.str and INT.value >= MinRequirements.int and\
                    WIS.value >= MinRequirements.wis and DEX.value >= MinRequirements.dex and\
                    CON.value >= MinRequirements.con and CHA.value >= MinRequirements.cha:
                if debug:
                    print("PASS - moze byc ten char")
                list_of_available_class.append(str(i))
            else:
                if debug:
                    print("FAIL - ten char nie moze byc")

    print(list_of_available_class)


class_selection_based_on_stats(True)
# x = randomize_all_statistics()
# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])
# print(x[4])
# print(x[5])
# print(x[6])


