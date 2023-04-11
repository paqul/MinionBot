from random import randint as r
from members import sorted_authors

dices = [2, 3, 4, 6, 8, 10, 12, 16, 20, 100, 1000]
penalty_bonus_dices = [100]
penalty_bonus_dices_dnd = [20]
apologize_message = "Bardzo mi przykro ale nie posiadam takiej kostki"


def roll(author, amount_of_rolls: int, dice: int) -> str:
    if dice in dices:
        lst = []
        for _ in range(int(amount_of_rolls)):
            number = r(1, dice)
            lst.append(number)
        if str(author.name) in sorted_authors:
            lst = sorted(lst)
        return f"({author.mention} k{dice}): **" + str(lst) + "**"
    else:
        return apologize_message


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

def penalty_bonus_roll_dnd(author: object, amount_of_rolls: int, dice: int, bonus: str, ) -> str:
    if bonus == "a":
        dice_type = "Ułatwienie / Advantage"
    elif bonus == "d":
        dice_type = "Utrudnienie / Disadvantage"
    else:
        dice_type = "Błąd typu kości"
    if dice in penalty_bonus_dices_dnd:
        diceresults = []
        for _ in range(int(amount_of_rolls)):
            combinedrolls = []
            roll0 = r(1, dice)
            combinedrolls.append(roll0)
            roll1 = r(1, dice)
            combinedrolls.append(roll1)
            if bonus == "d":
                diceresults.append("(" + str(sorted(combinedrolls)) + ")")
            elif bonus == "a":
                diceresults.append("(" + str(sorted(combinedrolls, reverse=True)) + ")")
            else: 
                continue
        if bonus == "d":
            return f"({author.mention} [k{dice}, {dice_type}]): " + str(diceresults)
        if bonus == "a":
            return f"({author.mention} [k{dice}, {dice_type}]): " + str(diceresults)
    else:
        return apologize_message
        
