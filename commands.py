from __future__ import annotations

import re
from abc import ABC, abstractmethod
from typing import Optional

from rolls import (
    RollResult,
    dis_advantage_dnd_roll,
    max_amountofrolls_message,
    morkborg_roll,
    bonus_penalty_callofcthulu_roll,
    cop_roll,
    dagger_heart_roll,
    roll_regular,
    roll_with_modifier,
    roll_dnd_stat_block,
)


class RollCommand(ABC):
    pattern: re.Pattern

    def matches(self, msg: str) -> Optional[re.Match[str]]:
        return self.pattern.fullmatch(msg)

    @abstractmethod
    def execute(self, author_mention: str, author_name: str, match: re.Match[str]) -> RollResult:
        raise NotImplementedError


class MorkborgRollCommand(RollCommand):
    pattern = re.compile(r"^(\d+)[kd](66)$")

    def execute(self, author_mention: str, author_name: str, match: re.Match[str]) -> RollResult:
        amount_of_rolls = int(match.group(1))
        if amount_of_rolls > 9999:
            raise ValueError(max_amountofrolls_message)
        dice = int(match.group(2))
        return morkborg_roll(author_mention, author_name, amount_of_rolls, dice)


class AdvantageDisadvantageRollCommand(RollCommand):
    pattern = re.compile(r"^(\d+)[kd](20|100)([ad])(?:([\+\-\*\/])(.*))?$")

    def execute(self, author_mention: str, author_name: str, match: re.Match[str]) -> RollResult:
        amount_of_rolls = int(match.group(1))
        if amount_of_rolls > 9999:
            raise ValueError(max_amountofrolls_message)
        dice = int(match.group(2))
        bonus = match.group(3)
        operator = match.group(4) if match.group(4) else None
        equation = match.group(5) if match.group(5) else None
        return dis_advantage_dnd_roll(author_mention, amount_of_rolls, dice, bonus, operator, equation)


class CallOfCthulhuRollCommand(RollCommand):
    pattern = re.compile(r"^(\d+)([kd])(\d+)([kp])([kp]?)$")

    def execute(self, author_mention: str, author_name: str, match: re.Match[str]) -> RollResult:
        amount_of_rolls = int(match.group(1))
        if amount_of_rolls > 9999:
            raise ValueError(max_amountofrolls_message)
        dice = int(match.group(3))
        bonus_or_penalty = match.group(4)
        double_bonus_or_penalty = match.group(5)
        twice = bool(double_bonus_or_penalty)
        if bonus_or_penalty == double_bonus_or_penalty and twice:
            return bonus_penalty_callofcthulu_roll(author_mention, amount_of_rolls, dice, bonus_or_penalty, twice)
        if not twice:
            return bonus_penalty_callofcthulu_roll(author_mention, amount_of_rolls, dice, bonus_or_penalty, twice)
        raise ValueError("Invalid Call of Cthulhu roll format")


class ModifierRollCommand(RollCommand):
    pattern = re.compile(r"^(\d+)[kd](\d+)([\+\-\*\/])(.*)$")

    def execute(self, author_mention: str, author_name: str, match: re.Match[str]) -> RollResult:
        amount_of_rolls = int(match.group(1))
        if amount_of_rolls > 9999:
            raise ValueError(max_amountofrolls_message)
        dice = int(match.group(2))
        operator = match.group(3)
        equation = match.group(4)
        return roll_with_modifier(author_mention, author_name, amount_of_rolls, dice, operator, equation)


class RegularRollCommand(RollCommand):
    pattern = re.compile(r"^(\d+)[kd](\d+)$")

    def execute(self, author_mention: str, author_name: str, match: re.Match[str]) -> RollResult:
        amount_of_rolls = int(match.group(1))
        if amount_of_rolls > 9999:
            raise ValueError(max_amountofrolls_message)
        dice = int(match.group(2))
        return roll_regular(author_mention, author_name, amount_of_rolls, dice)


class DndStatBlockCommand(RollCommand):
    pattern = re.compile(r"^statystyki_dnd$")

    def execute(self, author_mention: str, author_name: str, match: re.Match[str]) -> RollResult:
        return roll_dnd_stat_block(author_mention)


class CopRollCommand(RollCommand):
    pattern = re.compile(r"^gl(?:([\+\-\*\/])(.*))? *$")

    def execute(self, author_mention: str, author_name: str, match: re.Match[str]) -> RollResult:
        operator = match.group(1) if match.group(1) else None
        equation = match.group(2) if match.group(2) else None
        return cop_roll(author_mention, author_name, True, operator, equation)

class DaggerHeartRollCommand(RollCommand):
    pattern = re.compile(r"^dh(?:([\+\-\*\/])(.*))? *$")

    def execute(self, author_mention: str, author_name: str, match: re.Match[str]) -> RollResult:
        operator = match.group(1) if match.group(1) else None
        equation = match.group(2) if match.group(2) else None
        return dagger_heart_roll(author_mention, author_name, True, operator, equation)


class CommandRegistry:
    def __init__(self) -> None:
        self.commands = [
            MorkborgRollCommand(),
            AdvantageDisadvantageRollCommand(),
            CallOfCthulhuRollCommand(),
            CopRollCommand(),
            DaggerHeartRollCommand(),
            ModifierRollCommand(),
            RegularRollCommand(),
            DndStatBlockCommand(),
        ]

    def dispatch(self, msg: str, author_mention: str, author_name: str) -> Optional[RollResult]:
        for command in self.commands:
            match = command.matches(msg)
            if match:
                try:
                    return command.execute(author_mention, author_name, match)
                except ValueError:
                    return None
        return None

