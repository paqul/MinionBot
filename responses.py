from commands import CommandRegistry
from formatters import format_roll_result
from rolls import help_response, sorry_response, character_limit_response
import sys

registry = CommandRegistry()


def handle_response(msg, author, author_id) -> str:
    msg = msg.lower().strip()

    if msg == "help":
        return help_response

    result = registry.dispatch(msg, author.mention, author.name)
    if result is None:
        return sorry_response

    response = format_roll_result(result)
    if len(response) > 1999:
        return response[:1999 - len(character_limit_response)] + " " + character_limit_response

    return response


def handle_name_response(name_msg, bot_self_mention_string, author=None) -> str:
    if name_msg == bot_self_mention_string + " znikaj":
        sys.exit()
    return sorry_response
