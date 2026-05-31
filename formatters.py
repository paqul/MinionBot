from __future__ import annotations

from typing import Union

from rolls import RollResult, apologize_message


def _ansi_yellow(text: str) -> str:
    return f"### **```ansi\n\u001b[33m{text}\u001b[0m\n```**"

def _ansi_yellow_total(label: str, total: str) -> str:
    return _ansi_yellow(f"{label} {total}")


def _format_number(value: Union[int, float]) -> str:
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def format_roll_result(result: RollResult) -> str:
    if result.error:
        return result.error

    if result.bonus == "dh":
        total_value = _format_number(result.total) if result.total is not None else "?"
        return f"({result.author_mention}): {_ansi_yellow_total('Wynik:', total_value)} **{result.dice_type}** | **{result.rolls}**"

    if result.total is not None:
        total_value = _format_number(result.total)
        if result.equation is not None:
            return f"({result.author_mention} k{result.dice}) | {_ansi_yellow_total('Wynik:', total_value)} | **Rzuty: {result.rolls}**"
        return f"({result.author_mention} k{result.dice}) | {_ansi_yellow_total('Suma:', total_value)} | **Rzuty: {result.rolls}**"

    if result.dice_type is not None:
        if result.bonus in ("p", "k"):
            return f"({result.author_mention} [k{result.dice}, *{result.dice_type}*]): **{result.rolls}**"
        return f"({result.author_mention} [*{result.dice_type}*]): **{result.rolls}**"

    if result.dice is not None:
        return f"({result.author_mention} k{result.dice}): **{result.rolls}**"

    return apologize_message
