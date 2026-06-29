from __future__ import annotations

import re
from typing import Optional

import discord

from whitelist_storage import ChannelWhitelistStore


ADD_CHANNEL_PATTERN = re.compile(r"^add_bot_to_channel\s+(.+)$", re.IGNORECASE)
REMOVE_CHANNEL_PATTERN = re.compile(r"^remove_bot_from_channel\s+(.+)$", re.IGNORECASE)


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


def _normalize_channel_argument(raw_value: str) -> str:
    requested_name = _remove_quotes(raw_value).strip()
    if requested_name.startswith("#!"):
        requested_name = requested_name[2:].strip()
    if requested_name.startswith("#"):
        requested_name = requested_name[1:].strip()
    return requested_name.lower()


def _is_supported_channel(channel: discord.abc.GuildChannel) -> bool:
    return not isinstance(channel, discord.CategoryChannel)


def _is_voice_channel(channel: discord.abc.GuildChannel) -> bool:
    return isinstance(channel, (discord.VoiceChannel, discord.StageChannel))


def _is_text_channel(channel: discord.abc.GuildChannel) -> bool:
    return isinstance(channel, (discord.TextChannel, discord.ForumChannel))


def _match_channel_type(raw_value: str, channel: discord.abc.GuildChannel) -> bool:
    stripped_value = raw_value.strip()
    if stripped_value.startswith("#!"):
        return _is_voice_channel(channel)
    if stripped_value.startswith("#"):
        return _is_text_channel(channel)
    return True


def _resolve_channel(raw_value: str, guild: discord.Guild) -> Optional[discord.abc.GuildChannel]:
    stripped_value = raw_value.strip()
    mention_match = re.fullmatch(r"<#(\d+)>", stripped_value)
    if mention_match:
        channel_id = int(mention_match.group(1))
        channel = guild.get_channel(channel_id)
        if channel is not None and _is_supported_channel(channel):
            return channel
        return None

    requested_name_lower = _normalize_channel_argument(raw_value)
    if not requested_name_lower:
        return None

    exact_matches = [
        channel
        for channel in guild.channels
        if _is_supported_channel(channel)
        and _match_channel_type(raw_value, channel)
        and getattr(channel, "name", "").strip().lower() == requested_name_lower
    ]
    if len(exact_matches) == 1:
        return exact_matches[0]

    for channel in exact_matches:
        if getattr(channel, "mention", None) == stripped_value:
            return channel

    if exact_matches:
        return exact_matches[0]

    for channel in guild.channels:
        if not _is_supported_channel(channel):
            continue
        if not _match_channel_type(raw_value, channel):
            continue
        if getattr(channel, "mention", None) == stripped_value:
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
    remove_channel_match = REMOVE_CHANNEL_PATTERN.fullmatch(mention_body)
    if add_channel_match is None and remove_channel_match is None:
        return None

    if msg.guild is None:
        return "Ta komenda dziala tylko na serwerze Discord (nie w DM)."

    if msg.author.id not in allowed_admin_user_ids:
        return "Nie masz uprawnien do zarzadzania whitelista kanalow."

    if add_channel_match is not None:
        channel_argument = add_channel_match.group(1).strip()
    else:
        if remove_channel_match is None:
            return None
        channel_argument = remove_channel_match.group(1).strip()
    if not channel_argument:
        if add_channel_match is not None:
            return "Uzycie: @bot Add_Bot_To_Channel #kanal_tekstowy lub @bot Add_Bot_To_Channel #!kanal_glosowy."
        return "Uzycie: @bot Remove_Bot_From_Channel #kanal_tekstowy lub @bot Remove_Bot_From_Channel #!kanal_glosowy."

    channel = _resolve_channel(channel_argument, msg.guild)
    if channel is None:
        return "Nie znaleziono kanalu. Uzyj #nazwa dla tekstowego albo #!nazwa dla glosowego."

    if remove_channel_match is not None:
        removed, reason = whitelist_store.remove_channel(channel.id, channel.name)
        if not removed and reason == "not_whitelisted":
            return f"Kanal #{channel.name} nie jest na whiteliscie."
        return f"Usunieto kanal #{channel.name} z whitelisty."

    added, reason = whitelist_store.add_channel(channel.id, channel.name)
    if not added and reason == "already_whitelisted":
        return f"Kanal #{channel.name} jest juz na whiteliscie."

    return f"Dodano kanal #{channel.name} do whitelisty."
