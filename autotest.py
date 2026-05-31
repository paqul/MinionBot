from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass

import responses
from commands import (
    AdvantageDisadvantageRollCommand,
    CallOfCthulhuRollCommand,
    CommandRegistry,
    CopRollCommand,
    DndStatBlockCommand,
    ModifierRollCommand,
    MorkborgRollCommand,
    RegularRollCommand,
    DaggerHeartRollCommand
)
from rolls import apologize_message, sorry_response


@dataclass
class AutoTestCase:
    label: str
    command: str
    expect_sorry: bool = False
    expect_apologize: bool = False


@dataclass
class AutoTestResult:
    label: str
    command: str
    passed: bool
    details: str


def build_dynamic_test_cases() -> list[AutoTestCase]:
    registry = CommandRegistry()

    by_command_type: dict[str, list[AutoTestCase]] = {
        MorkborgRollCommand.__name__: [AutoTestCase("morkborg", "1d66")],
        AdvantageDisadvantageRollCommand.__name__: [
            AutoTestCase("advantage_d20", "1d20a"),
            AutoTestCase("advantage_mothership", "1d100a"),
            AutoTestCase("disadvantage_mothership", "1d100d"),
            AutoTestCase("disadvantage_modifier", "1d100d+5"),
        ],
        CallOfCthulhuRollCommand.__name__: [
            AutoTestCase("coc_bonus", "1d100p"),
            AutoTestCase("coc_double_penalty", "1d100kk"),
        ],
        CopRollCommand.__name__: [
            AutoTestCase("cop_basic", "gl"),
            AutoTestCase("cop_modifier_plus", "gl+5"),
            AutoTestCase("cop_modifier_minus", "gl-3"),
        ],
        DaggerHeartRollCommand.__name__: [
            AutoTestCase("daggerheart_basic", "dh"),
            AutoTestCase("daggerheart_modifier_plus", "dh+3"),
            AutoTestCase("daggerheart_modifier_expression", "dh+2-1"),
        ],
        ModifierRollCommand.__name__: [AutoTestCase("modifier", "2d20+2-5+3*2")],
        RegularRollCommand.__name__: [AutoTestCase("regular", "3d6")],
        DndStatBlockCommand.__name__: [AutoTestCase("dnd_stats", "statystyki_dnd")],
    }

    tests: list[AutoTestCase] = []
    for command in registry.commands:
        tests.extend(by_command_type.get(type(command).__name__, []))

    tests.extend(
        [
            AutoTestCase("help", "help"),
            AutoTestCase("too_many_rolls", "10000d20", expect_sorry=True),
            AutoTestCase("unknown_command", "to_nie_istnieje", expect_sorry=True),
            AutoTestCase("advantage_invalid_dice", "1d6a", expect_sorry=True),
            AutoTestCase("disadvantage_invalid_dice", "1d12d", expect_sorry=True),
            AutoTestCase("advantage_modifier_invalid", "1d8a+5", expect_sorry=True),
            AutoTestCase("regular_invalid_dice", "1d11", expect_apologize=True),
            AutoTestCase("coc_invalid_dice_p", "1d20p", expect_apologize=True),
            AutoTestCase("coc_invalid_dice_k", "1d20k", expect_apologize=True),
            AutoTestCase("coc_invalid_double_small_dice", "1d6pp", expect_apologize=True),
            AutoTestCase("coc_mixed_bonus_penalty", "1d100kp", expect_sorry=True),
            AutoTestCase("coc_mixed_penalty_bonus", "1d100pk", expect_sorry=True),
        ]
    )
    return tests


def _run_single_test_case(test_case: AutoTestCase, author) -> AutoTestResult:
    try:
        response = responses.handle_response(test_case.command, author, author.id)
    except Exception as exc:
        return AutoTestResult(
            label=test_case.label,
            command=test_case.command,
            passed=False,
            details=f"Wyjatek: {exc}",
        )

    if response is None:
        return AutoTestResult(
            label=test_case.label,
            command=test_case.command,
            passed=False,
            details="Brak odpowiedzi (None).",
        )

    got_sorry = response == sorry_response
    got_apologize = response == apologize_message

    if test_case.expect_sorry and not got_sorry:
        got_text = "otrzymano sorry_response" if got_sorry else "otrzymano odpowiedz"
        return AutoTestResult(
            label=test_case.label,
            command=test_case.command,
            passed=False,
            details=f"oczekiwano sorry_response, {got_text}",
        )
    if test_case.expect_apologize and not got_apologize:
        return AutoTestResult(
            label=test_case.label,
            command=test_case.command,
            passed=False,
            details=f"oczekiwano apologize_message, otrzymano: {response[:60]!r}",
        )
    if not test_case.expect_sorry and not test_case.expect_apologize and (got_sorry or got_apologize):
        got_text = "sorry_response" if got_sorry else "apologize_message"
        return AutoTestResult(
            label=test_case.label,
            command=test_case.command,
            passed=False,
            details=f"oczekiwano poprawnej odpowiedzi, otrzymano {got_text}",
        )

    return AutoTestResult(
        label=test_case.label,
        command=test_case.command,
        passed=True,
        details="OK",
    )


def run_summary_autotest(author) -> tuple[list[AutoTestResult], float]:
    started_at = time.perf_counter()
    test_cases = build_dynamic_test_cases()
    results = [_run_single_test_case(test_case, author) for test_case in test_cases]
    duration_seconds = time.perf_counter() - started_at
    return results, duration_seconds


def build_summary_message(results: list[AutoTestResult], duration_seconds: float) -> str:
    total = len(results)
    passed = sum(1 for result in results if result.passed)
    failed_results = [result for result in results if not result.passed]
    failed = len(failed_results)

    lines = [
        "# ***Podsumowanie Autotestu***",
        f"- Testow lacznie: {total}",
        f"- Zaliczone: {passed}",
        f"- Nieudane: {failed}",
        f"- Czas wykonania: {0.01 + duration_seconds:.2f}s",
    ]

    if failed_results:
        lines.append("- Bledne przypadki:")
        for result in failed_results[:10]:
            lines.append(f"  - [{result.label}] `{result.command}` -> {result.details}")
        if failed > 10:
            lines.append(f"  - ... i jeszcze {failed - 10}.")
    else:
        lines.append("- Wszystkie przypadki przeszly poprawnie.")

    return "\n".join(lines)


async def _send_commands(msg, commands: list[str]) -> None:
    for command in commands:
        await msg.channel.send(command)
        response = responses.handle_response(command, msg.author, msg.author.id)
        if response:
            await msg.channel.send(response)
        await asyncio.sleep(1.0)


async def run_legacy_autotest(msg) -> None:
    rolls = [1, 10, 1000, 99999]

    await msg.channel.send("# ***Startuje Autotest - Widoczny.***")

    ## Positive Tests
    await msg.channel.send("## Positive Tests")

    # Regular rolls
    await msg.channel.send("### Regular Rolls")
    regular_dice = ["2", "3", "4", "6", "8", "10", "12", "16", "20", "24", "30", "100", "1000"]
    await _send_commands(msg, [f"{roll}d{die}" for roll in rolls for die in regular_dice])

    # Mork Borg k66
    await msg.channel.send("### Mork Borg k66")
    await _send_commands(msg, [f"{roll}d66" for roll in rolls])

    # Advantage / Disadvantage
    await msg.channel.send("### Advantage / Disadvantage")
    adv_dis_dice = ["20a", "20d", "100a", "100d", "20a+100", "20d+100"]
    await _send_commands(msg, [f"{roll}d{die}" for roll in rolls for die in adv_dis_dice])

    # Call of Cthulhu
    await msg.channel.send("### Call of Cthulhu")
    coc_dice = ["100kk", "100pp", "100k", "100p"]
    await _send_commands(msg, [f"{roll}d{die}" for roll in rolls for die in coc_dice])

    # Modifier Rolls
    await msg.channel.send("### Modifier Rolls")
    modifier_dice = ["20*2", "20+2", "20-2", "10+2+2+5-3*2"]
    await _send_commands(msg, [f"{roll}d{die}" for roll in rolls for die in modifier_dice])

    # Statystyki D&D i Help
    await msg.channel.send("### Statystyki D&D & Help")
    await _send_commands(msg, ["statystyki_dnd", "help"])

    # COP RPG
    await msg.channel.send("### COP RPG Rolls")
    await _send_commands(msg, ["gl", "gl+5", "gl-3", "gl+2", "gl-1"])

    # DaggerHeart
    await msg.channel.send("### DaggerHeart Rolls")
    await _send_commands(msg, ["dh", "dh+3", "dh-2", "dh+2-1"])
    
    # Negative Tests
    await msg.channel.send("## Negative Tests")

    # Negative Tests - Regular Rolls
    await msg.channel.send("### Invalid Regular Rolls")
    invalid_regular = ["1d11", "1d7", "1d9"]
    for invalid_cmd in invalid_regular:
        await msg.channel.send(f"**(Oczekiwany Fail)** {invalid_cmd}")
        response = responses.handle_response(invalid_cmd, msg.author, msg.author.id)
        if response:
            await msg.channel.send(response)
        await asyncio.sleep(1.0)

    # Negative Tests - Advantage/Disadvantage
    await msg.channel.send("### Invalid Advantage/Disadvantage")
    invalid_adv_dis = ["1d6a", "1d12d", "1d8a+5", "1d4d-2"]
    for invalid_cmd in invalid_adv_dis:
        await msg.channel.send(f"**(Oczekiwany Fail)** {invalid_cmd}")
        response = responses.handle_response(invalid_cmd, msg.author, msg.author.id)
        if response:
            await msg.channel.send(response)
        await asyncio.sleep(1.0)

    # Negative Tests - Call of Cthulhu
    await msg.channel.send("### Invalid Call of Cthulhu")
    invalid_coc = ["1d20p", "1d20k", "1d6pp", "1d100kp", "1d100pk"]
    for invalid_cmd in invalid_coc:
        await msg.channel.send(f"**(Oczekiwany Fail)** {invalid_cmd}")
        response = responses.handle_response(invalid_cmd, msg.author, msg.author.id)
        if response:
            await msg.channel.send(response)
        await asyncio.sleep(1.0)

    await msg.channel.send("# ***Zakonczono Autotest - Widoczny.***")
