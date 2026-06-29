from __future__ import annotations

import json
import subprocess
import threading
from pathlib import Path
from typing import Iterable


class ChannelWhitelistStore:
    """Persistent channel whitelist backed by a JSON file."""

    def __init__(self, file_path: Path, seed_channel_names: Iterable[str]):
        self.file_path = file_path
        self._lock = threading.Lock()
        self._channel_ids: set[int] = set()
        self._channel_names: set[str] = set()
        self._seed_channel_names = list(seed_channel_names)
        self._load_or_seed()

    @staticmethod
    def _normalize_name(name: str) -> str:
        return name.strip().lower()

    def _load_or_seed(self) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.file_path.exists():
            self._channel_names = {
                self._normalize_name(name)
                for name in self._seed_channel_names
                if isinstance(name, str) and name.strip()
            }
            self._save_unlocked()
            return

        try:
            with self.file_path.open("r", encoding="utf-8") as file_handle:
                data = json.load(file_handle)
        except (json.JSONDecodeError, OSError):
            data = {}

        channel_ids = data.get("channel_ids", [])
        channel_names = data.get("channel_names", [])

        self._channel_ids = {
            int(channel_id)
            for channel_id in channel_ids
            if isinstance(channel_id, (int, str)) and str(channel_id).isdigit()
        }
        self._channel_names = {
            self._normalize_name(name)
            for name in channel_names
            if isinstance(name, str) and name.strip()
        }

        if not self._channel_ids and not self._channel_names:
            self._channel_names = {
                self._normalize_name(name)
                for name in self._seed_channel_names
                if isinstance(name, str) and name.strip()
            }
            self._save_unlocked()

    def _save_unlocked(self) -> None:
        payload = {
            "channel_ids": sorted(self._channel_ids),
            "channel_names": sorted(self._channel_names),
        }
        with self.file_path.open("w", encoding="utf-8") as file_handle:
            json.dump(payload, file_handle, ensure_ascii=False, indent=2)

    def is_allowed(self, channel_id: int, channel_name: str) -> bool:
        normalized_name = self._normalize_name(channel_name)
        with self._lock:
            return channel_id in self._channel_ids or normalized_name in self._channel_names

    def _git_commit_whitelist(self, channel_name: str, action: str) -> None:
        repo_root = Path(__file__).resolve().parent
        commit_message = f"whitelist: {action} channel #{channel_name}"
        try:
            subprocess.run(
                ["git", "add", str(self.file_path)],
                cwd=repo_root,
                check=True,
                capture_output=True,
            )
            subprocess.run(
                ["git", "commit", "-m", commit_message],
                cwd=repo_root,
                check=True,
                capture_output=True,
            )
            print(f"Git commit: {commit_message}")
        except subprocess.CalledProcessError as exc:
            stderr = exc.stderr.decode(errors="replace").strip() if exc.stderr else ""
            print(f"Git commit failed: {stderr}")

    def add_channel(self, channel_id: int, channel_name: str) -> tuple[bool, str]:
        normalized_name = self._normalize_name(channel_name)
        with self._lock:
            if channel_id in self._channel_ids or normalized_name in self._channel_names:
                return False, "already_whitelisted"

            self._channel_ids.add(channel_id)
            self._channel_names.add(normalized_name)
            self._save_unlocked()

        self._git_commit_whitelist(channel_name, "add")
        return True, "added"

    def remove_channel(self, channel_id: int, channel_name: str) -> tuple[bool, str]:
        normalized_name = self._normalize_name(channel_name)
        with self._lock:
            has_channel_id = channel_id in self._channel_ids
            has_channel_name = normalized_name in self._channel_names

            if not has_channel_id and not has_channel_name:
                return False, "not_whitelisted"

            if has_channel_id:
                self._channel_ids.remove(channel_id)
            if has_channel_name:
                self._channel_names.remove(normalized_name)
            self._save_unlocked()

        self._git_commit_whitelist(channel_name, "remove")
        return True, "removed"
