from __future__ import annotations

from typing import Any
import asyncio

from mautrix.bridge import Bridge
from mautrix.types import RoomID, UserID
from mautrix.util import background_task

from . import commands

class TwitterBridge(Bridge):
    module = "matrix_phone_bridge"
    name = "matrix-phone-bridge"
    beeper_service_name = "phone"
    beeper_network_name = "phone"
    command = "python -m matrix-phone-bridge"
    description = "A Matrix-Twitter DM puppeting bridge."
    repo_url = "https://github.com/imjoshin/matrix-phone-bridge"

    def prepare_db(self) -> None:
        super().prepare_db()
        init_db(self.db)

