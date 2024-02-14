from random import randint as r
# from members import sorted_authors

dices = [2, 3, 4, 6, 8, 10, 12, 16, 20, 24, 30, 66, 100, 1000]
call_of_cthlu_penalty_bonus_dice = [100]
dnd_dis_advantage_dice = [20]
apologize_message = (
    "Bardzo mi przykro ale nie posiadam takiej kostki\n"
    "Po wiecej informacji i pomoc napisz komendę *help*"
)


def format_response_msg(author, rolls, total_sum=None, dice=None, equation=None, bonus=None, dice_type=None):
    if total_sum is not None:
        # If total sum exists and there is an equation - Rolls with modifiers
        if equation is not None:
            return f"({author.mention} k{dice}): **{rolls} | Wynik: {total_sum}**"
        # If total sum exists and there is no equation - Rolls with modifiers
        else:
            return f"({author.mention} k{dice}): **{rolls} | Suma: {total_sum}**"
    elif dice_type is not None:
        if bonus in ("p", "k"):
            return f"({author.mention} [k{dice}, {dice_type}]): **{rolls}**"
        else:
            # Default format for other cases of dice_type
            return f"({author.mention} [{dice_type}]): **{rolls}**"
    # Default format for regular rolls
    elif dice is not None:
        return f"({author.mention} k{dice}): **{rolls}**"
    # If error:
    else:
        return apologize_message


def roll(author, amount_of_rolls: int, dice: int) -> str:
    if dice not in dices:
        return apologize_message
    rolls = [r(1, dice) for _ in range(amount_of_rolls)]
    # if str(author.name) in sorted_authors:
    #    rolls.sort()
    total_sum = None if amount_of_rolls == 1 else f"{sum(rolls)}"
    return format_response_msg(author, rolls, total_sum, dice=dice)


def roll_with_modifier(author, amount_of_rolls: int, dice: int, operator: str, equation: str) -> str:
    if dice not in dices:
        return apologize_message
    if dice == 66:
        rolls, total_sum = morkborg_roll(author, amount_of_rolls, dice)
    else:
        rolls = [r(1, dice) for _ in range(amount_of_rolls)]
        total_sum = sum(rolls)
    modified_sum = eval(f"{total_sum} {operator} {equation}")
    return format_response_msg(author, rolls, modified_sum, dice=dice, equation=equation)


def dis_advantage_dnd_roll(author: object, amount_of_rolls: int, dice: int, bonus: str) -> str:
    if bonus not in ("a", "d") or dice not in dnd_dis_advantage_dice:
        return apologize_message
    dice_type = "Ułatwienie / Advantage" if bonus == "a" else "Utrudnienie / Disadvantage"
    internal_rolls = [[r(1, dice) for _ in range(2)]
                      for _ in range(amount_of_rolls)]
    if bonus == "a":
        for sublist in internal_rolls:
            sublist.sort(reverse=True)
    else:
        for sublist in internal_rolls:
            sublist.sort()
    rolls = ", ".join(str(roll) for roll in internal_rolls)
    return format_response_msg(author, rolls=rolls, dice_type=dice_type)


def morkborg_roll(author, amount_of_rolls: int, dice: int) -> str:
    if dice not in dices:
        return apologize_message
    rolls = []
    total_sum = None
    for _ in range(amount_of_rolls):
        roll1 = r(1, 6)
        roll2 = r(1, 6)
        rolls.append(int(str(roll1) + str(roll2)))
    if amount_of_rolls > 1:
        total_sum = sum(rolls)
    return (rolls, total_sum) if total_sum is not None else format_response_msg(author, rolls=rolls, total_sum=total_sum, dice=dice)


def roll_dnd_stat_block(author: object) -> str:
    rolls = sorted([sum(sorted([r(1, 6) for _ in range(4)], reverse=True)[:3])
                   for _ in range(6)], reverse=True)
    dice_type = "Rzuty na statystyki D&D"
    return format_response_msg(author, rolls=rolls, dice_type=dice_type)


def bonus_penalty_callofcthulu_roll(author: object, amount_of_rolls: int, dice: int, bonus: str, twice: bool) -> str:
    if dice not in call_of_cthlu_penalty_bonus_dice:
        return apologize_message
    dice_type_initial = "Premiowa" if bonus == "p" else "Karna"
    rolls = []
    for _ in range(int(amount_of_rolls)):
        initial_roll = r(1, dice)
        units_str = str(initial_roll % 10)
        penalty_bonus_dice_tens = r(0, 9)
        if twice:
            dice_type = f"{dice_type_initial}, {dice_type_initial}"
            penalty_bonus_dice_2_tens = r(0, 9)
            second_penalty_bonus_roll = int(f"{penalty_bonus_dice_2_tens}{units_str}")
            if second_penalty_bonus_roll == 0 :
                second_penalty_bonus_roll = 100
            rolls.append(initial_roll, penalty_bonus_dice_tens, second_penalty_bonus_roll)
        else:
            dice_type = f"{dice_type_initial}"
            first_penalty_bonus_roll = int(f"{penalty_bonus_dice_2_tens}{units_str}")
            if first_penalty_bonus_roll == 0:
                first_penalty_bonus_roll = 100
            rolls.append(initial_roll, first_penalty_bonus_roll)
        return format_response_msg(author, rolls=rolls, dice=dice, dice_type=dice_type, bonus=bonus)
