from __future__ import annotations

import ast
from dataclasses import dataclass
from random import randint as r
from typing import Optional, Union

sorted_authors: list[str] = []
try:
    members = __import__("members")
    sorted_authors = getattr(members, "sorted_authors", [])
except ImportError:
    sorted_authors = []


dices = [2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 30, 66, 100, 1000]
call_of_cthlu_penalty_bonus_dice = [100]
dnd_dis_advantage_dice = [20, 100]
apologize_message = (
    "🎲 Nie mam takiej kostki. \n"
    "Wpisz *help*, żeby zobaczyć dostępne rzuty."
)

sorry_response = (
    "🤷 Nie znam tej komendy.\n"
    "Wpisz ***help***, żeby zobaczyć dostępne opcje."
)

help_response = (
    "Aby uzyskać wynik rzutu kością wpisz komendę ***<ilość kości>k<ilość ściań kości>*** (np. *1k100, 3k20, 2k10* itp.).\n"
    "Maksymalna <ilość kości> to ***9999***.\n"
    "Obecnie wspierane kości ***" + str(dices) + "***.\n"
    "Dostępne Funkcje dodatkowe:\n"
    "- Rzut z modyfikatorem: ***1k10+2-5*** dozwolone działania +,-,*. \n"
    "  Nie wszystkie funkcje obsługują równania, tylko te gdzie ma to sens w zasadach gry.\n"
    "  Nie zapominaj o kolejności wykonywania działań. 😏\n"
    "- Rzut Przewaga/Utrudnienie D&D 5e(d20) i Mothership(d100): ***1k20a*** lub ***1k20d***. Działa również z modyfikatorem.\n"
    "- Rzut Premiowy/Karny Call Of Cthulu: ***1k100p*** lub ***1k100k***.\n"
    "- Podwójny Rzut Premiowy/Karny Call Of Cthulu: ***1k100pp*** lub ***1k100kk***.\n"
    "- Rzut Specjalny k66 Mork Borg: ***1k66*** (rzut 2k6 gdzie jedna kość to dziesiątki a druga jedności).\n"
    "- Rzut Glina: ***gl*** (1d6 vs 2d10) lub z modyfikatorem ***gl+2, gl-3*** itp. Wyniki: Triumf, Fuks, Skucha.\n"
    "- Rzut DaggerHeart: ***dh*** (2k12 Hope/Fear), z modyfikatorem np. dh+2; Dublet na obu kościach = Krytyk.\n"
    "- Rzut na zestaw Statystyk D&D 3e & 5e: ***statystyki_dnd*** - generuje 6 rzutów wg zasady 4k6, odrzucająć najniższy.\n"
    "  Przerzuca cały zestaw jeżeli suma modyfikatorów wynosi 0 lub gdy najwyższy rzut to 13\n"
    "- Pomoc: komenda ***help***."
)

character_limit_response = (
    "**- ✂️ Wiadomość była za długa dla Discorda, uciąłem część rzutów.\n"
    "Spróbuj mniejszej liczby rzutów." + "**"
)

max_amountofrolls_message = (
    "⛔ Maksymalna liczba kości to 9999.\n"
    "Wpisz ***help*** po więcej info."
)

MAX_AMOUNT_OF_ROLLS = 9999


@dataclass
class RollResult:
    author_mention: str
    rolls: Union[list[int], str]
    total: Optional[Union[int, float]] = None
    dice: Optional[int] = None
    equation: Optional[str] = None
    dice_type: Optional[str] = None
    bonus: Optional[str] = None
    error: Optional[str] = None


def _evaluate_ast(node: ast.AST) -> Union[int, float]:
    if isinstance(node, ast.BinOp):
        left = _evaluate_ast(node.left)
        right = _evaluate_ast(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            if right == 0:
                raise ValueError("⚠️ Nie można dzielić przez 0 ;)")
            return left / right
        raise ValueError("⚠️ Niepoprawna operacja arytmetyczna")
    if isinstance(node, ast.UnaryOp):
        operand = _evaluate_ast(node.operand)
        if isinstance(node.op, ast.UAdd):
            return +operand
        if isinstance(node.op, ast.USub):
            return -operand
        raise ValueError("⚠️ Niepoprawny operator")
    if isinstance(node, ast.Constant):
        value = node.value
        if not isinstance(value, (int, float)):
            raise ValueError("⚠️ Niepoprawna liczba w wyrażeniu")
        return value
    raise ValueError("⚠️ Nieobsługiwany element wyrażenia")


def safe_eval(expression: str) -> Union[int, float]:
    try:
        node = ast.parse(expression.strip(), mode="eval").body
        return _evaluate_ast(node)
    except (SyntaxError, ValueError) as exc:
        raise ValueError("⚠️ Niepoprawne wyrażenie modyfikatora") from exc


def _normalize_rolls(rolls: list[int], sort_rolls: bool, author_name: str) -> list[int]:
    return rolls


def roll_regular(
    author_mention: str,
    author_name: str,
    amount_of_rolls: int,
    dice: int,
    sort_rolls: bool = False,
) -> RollResult:
    if amount_of_rolls > MAX_AMOUNT_OF_ROLLS:
        return RollResult(author_mention=author_mention, rolls="", error=max_amountofrolls_message)
    if dice not in dices:
        return RollResult(author_mention=author_mention, rolls="", error=apologize_message)

    rolls = _normalize_rolls([r(1, dice) for _ in range(amount_of_rolls)], sort_rolls, author_name)
    total_sum = None if amount_of_rolls == 1 else sum(rolls)
    return RollResult(
        author_mention=author_mention,
        rolls=rolls,
        total=total_sum,
        dice=dice,
    )


def roll_with_modifier(
    author_mention: str,
    author_name: str,
    amount_of_rolls: int,
    dice: int,
    operator: str,
    equation: str,
    sort_rolls: bool = False,
) -> RollResult:
    if amount_of_rolls > MAX_AMOUNT_OF_ROLLS:
        return RollResult(author_mention=author_mention, rolls="", error=max_amountofrolls_message)
    if dice not in dices:
        return RollResult(author_mention=author_mention, rolls="", error=apologize_message)

    rolls = _normalize_rolls([r(1, dice) for _ in range(amount_of_rolls)], sort_rolls, author_name)
    total_sum = sum(rolls)

    try:
        modified_sum = safe_eval(f"{total_sum}{operator}{equation}")
    except ValueError as exc:
        return RollResult(author_mention=author_mention, rolls=rolls, error=str(exc))

    return RollResult(
        author_mention=author_mention,
        rolls=rolls,
        total=modified_sum,
        dice=dice,
        equation=equation,
    )


def dis_advantage_dnd_roll(
    author_mention: str,
    amount_of_rolls: int,
    dice: int,
    bonus: str,
    operator: Optional[str],
    equation: Optional[str],
) -> RollResult:
    dice_type = "Ułatwienie / Advantage" if bonus == "a" else "Utrudnienie / Disadvantage"
    internal_rolls = [[r(1, dice) for _ in range(2)] for _ in range(amount_of_rolls)]

    if operator and equation:
        try:
            evaluated_rolls = [
                [safe_eval(f"{roll}{operator}{equation}") for roll in sublist]
                for sublist in internal_rolls
            ]
        except ValueError as exc:
            return RollResult(author_mention=author_mention, rolls="", error=str(exc))
    else:
        evaluated_rolls = internal_rolls

    for sublist in evaluated_rolls:
        sublist.sort(reverse=(bonus == "a"))

    rolls_text = ", ".join(str(sublist) for sublist in evaluated_rolls)
    
    return RollResult(
        author_mention=author_mention,
        rolls=rolls_text,
        dice=dice,
        dice_type=dice_type,
        bonus=bonus,
    )


def morkborg_roll(
    author_mention: str,
    author_name: str,
    amount_of_rolls: int,
    dice: int,
    sort_rolls: bool = False,
) -> RollResult:
    if amount_of_rolls > MAX_AMOUNT_OF_ROLLS:
        return RollResult(author_mention=author_mention, rolls="", error=max_amountofrolls_message)
    if dice not in dices:
        return RollResult(author_mention=author_mention, rolls="", error=apologize_message)

    rolls = []
    for _ in range(amount_of_rolls):
        roll1 = r(1, 6)
        roll2 = r(1, 6)
        rolls.append(int(f"{roll1}{roll2}"))

    if sort_rolls and str(author_name) in sorted_authors:
        rolls.sort()

    total_sum = sum(rolls) if amount_of_rolls > 1 else None
    return RollResult(
        author_mention=author_mention,
        rolls=rolls,
        total=total_sum,
        dice=dice,
    )


def roll_dnd_stat_block(author_mention: str) -> RollResult:
    while True:
        rolls = sorted(
            [
                sum(sorted([r(1, 6) for _ in range(4)], reverse=True)[:3])
                for _ in range(6)
            ],
            reverse=True,
        )
        if max(rolls) == 13 or sum(rolls) <= 60:
            print("Dokonano Rerollu bo statystyki nie spełniały minimalnych wymagań")
            continue
        break

    return RollResult(
        author_mention=author_mention,
        rolls=rolls,
        dice_type="Rzuty na statystyki D&D",
    )


def cop_roll(
    author_mention: str,
    author_name: str,
    amount_of_rolls: bool,
    operator: Optional[str],
    equation: Optional[str],
) -> RollResult:
    """
    COP RPG Roll: 1d6 base (with optional modifier) vs 2d10
    Outcomes: Triumf (success), Fuks (critical), Skucha (failure)
    """
    rolls = []

    d6_base = r(1, 6)

    # Apply modifier if provided
    if operator and equation:
        try:
            d6_modified = safe_eval(f"{d6_base}{operator}{equation}")
            # Clamp to [1, 10]
            d6_modified = max(1, min(10, int(d6_modified)))
        except ValueError:
            return RollResult(author_mention=author_mention, rolls="", error="Niepoprawny modyfikator")
    else:
        d6_modified = d6_base

    # Roll 2d10
    d10_rolls = [r(1, 10), r(1, 10)]

    rolls.append(d6_modified)
    rolls.extend(d10_rolls)

    # Determine outcome
    if d6_modified > d10_rolls[0] and d6_modified > d10_rolls[1]:
        dice_type = "Triumf"
    elif d10_rolls[0] < d6_modified <= d10_rolls[1]:
        dice_type = "Fuks - pierwszy"
    elif d10_rolls[1] < d6_modified <= d10_rolls[0]:
        dice_type = "Fuks - drugi"
    else:
        dice_type = "Skucha"

    return RollResult(
        author_mention=author_mention,
        rolls=rolls,
        dice_type=dice_type,
        bonus="gl",
    )


def bonus_penalty_callofcthulu_roll(
    author_mention: str,
    amount_of_rolls: int,
    dice: int,
    bonus: str,
    twice: bool,
) -> RollResult:
    if amount_of_rolls > MAX_AMOUNT_OF_ROLLS:
        return RollResult(author_mention=author_mention, rolls="", error=max_amountofrolls_message)
    if dice not in call_of_cthlu_penalty_bonus_dice:
        return RollResult(author_mention=author_mention, rolls="", error=apologize_message)

    dice_type_initial = "Premiowa" if bonus == "p" else "Karna"
    dice_type = f"{dice_type_initial}, {dice_type_initial}" if twice else dice_type_initial

    list_of_internal_rolls = []
    for _ in range(amount_of_rolls):
        starting_regular_roll = r(1, dice)
        internal_rolls = [starting_regular_roll]
        units_digit_of_starting_roll = starting_regular_roll % 10

        for _ in range(2 if twice else 1):
            tens_digit_of_bonus_penalty_roll = r(0, 9)
            compound_penalty_bonus_roll = int(
                f"{tens_digit_of_bonus_penalty_roll}{units_digit_of_starting_roll}"
            )
            if compound_penalty_bonus_roll == 0:
                compound_penalty_bonus_roll = 100
            internal_rolls.append(compound_penalty_bonus_roll)

        if bonus == "p":
            internal_rolls[1:] = sorted(internal_rolls[1:], reverse=True)
        else:
            internal_rolls[1:] = sorted(internal_rolls[1:])

        list_of_internal_rolls.append(internal_rolls)

    rolls_text = ", ".join(str(element) for element in list_of_internal_rolls)
    return RollResult(
        author_mention=author_mention,
        rolls=rolls_text,
        dice=dice,
        dice_type=dice_type,
        bonus=bonus,
    )


def dagger_heart_roll(
    author_mention: str,
    author_name: str,
    amount_of_rolls: bool,
    operator: Optional[str],
    equation: Optional[str],
) -> RollResult:
    hope = r(1, 12)
    fear = r(1, 12)
    total = hope + fear

    if operator and equation:
        try:
            total = safe_eval(f"{total}{operator}{equation}")
        except ValueError:
            return RollResult(author_mention=author_mention, rolls="", error="Niepoprawny modyfikator")

    if hope == fear:
        dice_type = "❗Krytyk"
    elif hope > fear:
        dice_type = "👼Hope"
    else:
        dice_type = "😱Fear"

    return RollResult(
        author_mention=author_mention,
        rolls=f"H: {hope}, F: {fear}",
        total=total,
        dice_type=dice_type,
        bonus="dh",
        equation=equation if operator and equation else None,
    )
