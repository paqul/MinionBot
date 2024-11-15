from OSE.statistics import *
from OSE.fantasy_names import *


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


# x = randomize_all_statistics()
# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])
# print(x[4])
# print(x[5])
# print(x[6])


