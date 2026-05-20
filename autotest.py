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
)
from rolls import sorry_response


@dataclass
class AutoTestCase:
    label: str
    command: str
    expect_sorry: bool = False


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
    if got_sorry != test_case.expect_sorry:
        expected_text = "oczekiwano sorry_response" if test_case.expect_sorry else "oczekiwano poprawnej odpowiedzi"
        got_text = "otrzymano sorry_response" if got_sorry else "otrzymano odpowiedz"
        return AutoTestResult(
            label=test_case.label,
            command=test_case.command,
            passed=False,
            details=f"{expected_text}, {got_text}",
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


async def run_legacy_autotest(msg) -> None:
    rolls = [1, 10, 1000, 99999]
    dice = [
        "2",
        "3",
        "4",
        "6",
        "8",
        "10",
        "11",
        "12",
        "16",
        "20",
        "24",
        "30",
        "66",
        "100",
        "1000",
        "20a",
        "20d",
        "100a",
        "100d",
        "100kk",
        "100pp",
        "100kp",
        "100pk",
        "100k",
        "100p",
        "20*2",
        "20+2",
        "20-2",
        "10+2+2+5-3*2",
        "20a+100",
        "20d+100",
    ]

    await msg.channel.send("# ***Startuje Autotest Legacy.***")
    for roll in rolls:
        for die in dice:
            command = f"{roll}d{die}"
            await msg.channel.send(command)
            response = responses.handle_response(command, msg.author, msg.author.id)
            if response:
                await msg.channel.send(response)
            await asyncio.sleep(1.0)

    for command in ["statystyki_dnd", "help"]:
        await msg.channel.send(command)
        response = responses.handle_response(command, msg.author, msg.author.id)
        if response:
            await msg.channel.send(response)
        await asyncio.sleep(1.0)

    # Test COP RPG rolls
    await msg.channel.send("### COP RPG Rolls")
    cop_commands = ["gl", "gl+5", "gl-3", "gl+2", "gl-1"]
    for cop_command in cop_commands:
        await msg.channel.send(cop_command)
        response = responses.handle_response(cop_command, msg.author, msg.author.id)
        if response:
            await msg.channel.send(response)
        await asyncio.sleep(1.0)

    # Test negative cases for advantage/disadvantage
    await msg.channel.send("### Negative Tests - Invalid Advantage/Disadvantage")
    invalid_adv_dis = ["1d6a", "1d12d", "1d8a+5", "1d4d-2"]
    for invalid_cmd in invalid_adv_dis:
        await msg.channel.send(f"(POWINNO FAILNAC) {invalid_cmd}")
        response = responses.handle_response(invalid_cmd, msg.author, msg.author.id)
        if response:
            await msg.channel.send(response)
        await asyncio.sleep(1.0)

    await msg.channel.send("# ***Zakonczono Autotest Legacy.***")
