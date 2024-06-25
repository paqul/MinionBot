from random import randint as r
apologize_message = (
    "Bardzo mi przykro ale nie posiadam takiej kostki\n"
    "Po wiecej informacji i pomoc napisz komendę *help*"
)
dices = [2, 3, 4, 6, 8, 10, 12, 16, 20, 24, 30, 66, 100, 1000]
call_of_cthlu_penalty_bonus_dice = [100]
dnd_dis_advantage_dice = [20]

def diceroll(amount_of_rolls: int, dice: int) -> str:
    if dice not in dices:
        return apologize_message
    elif dice is 66:
        rolls = [r(1, dice) for _ in range(amount_of_rolls)]
    return (amount_of_rolls, dice, rolls,)