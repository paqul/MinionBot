from __future__ import annotations

import re
from typing import Optional

import discord

from whitelist_storage import ChannelWhitelistStore


ADD_CHANNEL_PATTERN = re.compile(r"^add_bot_to_channel\s+(.+)$", re.IGNORECASE)


def _extract_mention_body(message_content: str, bot_user_id: int) -> Optional[str]:
    prefixes = (f"<@{bot_user_id}>", f"<@!{bot_user_id}>")
    for prefix in prefixes:
        if message_content.startswith(prefix):
            return message_content[len(prefix):].strip()
    return None


def _remove_quotes(text: str) -> str:
    stripped = text.strip()
    if len(stripped) >= 2 and stripped[0] == stripped[-1] and stripped[0] in ('"', "'"):
        return stripped[1:-1].strip()
    return stripped


def _resolve_channel(raw_value: str, guild: discord.Guild) -> Optional[discord.abc.GuildChannel]:
    mention_match = re.fullmatch(r"<#(\d+)>", raw_value.strip())
    if mention_match:
        channel_id = int(mention_match.group(1))
        return guild.get_channel(channel_id)

    requested_name = _remove_quotes(raw_value)
    if not requested_name:
        return None

    # Accept either channel name (general) or hash-prefixed form (#general).
    if requested_name.startswith("#"):
        requested_name = requested_name[1:].strip()
        if not requested_name:
            return None

    requested_name_lower = requested_name.lower()
    for channel in guild.channels:
        if getattr(channel, "name", "").lower() == requested_name_lower:
            return channel
    return None


def handle_admin_mention_command(
    msg: discord.Message,
    bot_user_id: int,
    allowed_admin_user_ids: set[int],
    whitelist_store: ChannelWhitelistStore,
) -> Optional[str]:
    if msg.author.bot:
        return None

    mention_body = _extract_mention_body(msg.content, bot_user_id)
    if mention_body is None:
        return None

    add_channel_match = ADD_CHANNEL_PATTERN.fullmatch(mention_body)
    if add_channel_match is None:
        return None

    if msg.guild is None:
        return "Ta komenda dziala tylko na serwerze Discord (nie w DM)."

    if msg.author.id not in allowed_admin_user_ids:
        return "Nie masz uprawnien do zarzadzania whitelista kanalow."

    channel_argument = add_channel_match.group(1).strip()
    if not channel_argument:
        return "Uzycie: @bot Add_Bot_To_Channel <nazwa_kanalu_lub_mention_kanalu>."

    channel = _resolve_channel(channel_argument, msg.guild)
    if channel is None:
        return "Nie znaleziono kanalu. Podaj poprawna nazwe lub mention kanalu."

    added, reason = whitelist_store.add_channel(channel.id, channel.name)
    if not added and reason == "already_whitelisted":
        return f"Kanal #{channel.name} jest juz na whiteliscie."

    return f"Dodano kanal #{channel.name} do whitelisty."
