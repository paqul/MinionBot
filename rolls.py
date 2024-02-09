from random import randint as r
from members import sorted_authors

dices = [2, 3, 4, 6, 8, 10, 12, 16, 20, 100, 1000]
penalty_bonus_dices = [100]
penalty_bonus_dices_dnd = [20]
apologize_message = "Bardzo mi przykro ale nie posiadam takiej kostki"

def roll(author, amount_of_rolls: int, dice: int) -> str:
    if dice not in dices:
        return apologize_message
    rolls = [r(1, dice) for _ in range(amount_of_rolls)]
    if str(author.name) in sorted_authors:
        rolls.sort()
    total_sum = "" if amount_of_rolls == 1 else f" | Suma: {sum(rolls)}"
    return f"({author.mention} k{dice}): **{rolls}{total_sum}**"

def roll_with_modifier(author, amount_of_rolls: int, dice: int, operator: str, equation: str) -> str:
    if dice not in dices:
        return apologize_message
    rolls = [r(1, dice) for _ in range(amount_of_rolls)]
    total_sum = sum(rolls)
    modified_sum = eval(f"{total_sum} {operator} {equation}")
    return f"({author.mention} k{dice}): **{rolls} | Wynik: {modified_sum}**"

def roll_bonus_penalty(author: object, amount_of_rolls: int, dice: int, bonus: str, twice: bool = False) -> str:
    if bonus == "p":
        dice_type = "premiowa"
    elif bonus == "k":
        dice_type = "karna"
    else:
        dice_type = "Błąd typu kości"
    if dice in penalty_bonus_dices:
        lst = []
        penalty_bonus_dice_2 = None
        for _ in range(int(amount_of_rolls)):
            number = r(1, dice)
            str_number = str(number)
            if len(str_number) == 1: #0x
                str_number = "0"+str_number
            elif len(str_number) == 2: #xx
                ...
            else: #100
                str_number = "00"
            if twice:
                penalty_bonus_dice = r(0, 9)
                penalty_bonus_dice_2 = r(0, 9)
                str_penalty_bonus_dice_2 = str(penalty_bonus_dice_2) + str_number[1]
                penalty_bonus_dice_2 = int(str_penalty_bonus_dice_2)
                if penalty_bonus_dice_2 == 0:
                    penalty_bonus_dice_2 = 100
            else:
                penalty_bonus_dice = r(0, 9)
            str_penalty_bonus_dice = str(penalty_bonus_dice)+str_number[1]
            penalty_bonus_dice = int(str_penalty_bonus_dice)
            if penalty_bonus_dice == 0:
                penalty_bonus_dice = 100
            if twice:
                lst.append([number, penalty_bonus_dice, penalty_bonus_dice_2])
            else:
                lst.append([number, penalty_bonus_dice])
        if twice:
            return f"({author.mention} [k{dice}, {dice_type}, {dice_type}]): **" + str(lst) + "**"
        else:
            return f"({author.mention} [k{dice}, {dice_type}]): **" + str(lst) + "**"
    else:
        return apologize_message

def penalty_bonus_roll_dnd(author: object, amount_of_rolls: int, dice: int, bonus: str) -> str:
    if bonus not in ("a", "d") or dice not in penalty_bonus_dices_dnd:
        return apologize_message
    dice_type = "Ułatwienie / Advantage" if bonus == "a" else "Utrudnienie / Disadvantage"
    rolls = [[r(1, dice) for _ in range(2)] for _ in range(amount_of_rolls)]
    if bonus == "a":
        rolls.sort(reverse=True)
    else:
        rolls.sort()
    formatted_rolls = ", ".join(str(roll) for roll in rolls)
    return f"({author.mention} [k{dice}, {dice_type}]): **{formatted_rolls}**"
    
def roll_dnd_stat_block(author: object) -> str:
    lst_stats_final = [sum(sorted([r(1, 6) for _ in range(4)], reverse=True)[:3]) for _ in range(6)]
    formatted_stats = str(sorted(lst_stats_final, reverse=True))
    return f"({author.mention}, Rzuty na statystyki D&D): **{formatted_stats}**"
