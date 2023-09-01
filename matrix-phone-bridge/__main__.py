from __future__ import annotations

from typing import Any
import asyncio

from mautrix.bridge import Bridge
from mautrix.types import RoomID, UserID

from type.user import User
from type.portal import Portal
from type.puppet import Puppet
from config import Config

class PhoneBridge(Bridge):
    module = "matrix_phone_bridge"
    name = "matrix-phone-bridge"
    beeper_service_name = "phone"
    beeper_network_name = "phone"
    command = "python -m matrix-phone-bridge"
    description = "A Matrix-Twitter DM puppeting bridge."
    repo_url = "https://github.com/imjoshin/matrix-phone-bridge"
    config_class = Config

    async def start(self) -> None:
        self.log.info("Starting...")
        await super().start()
        self.log.info("Started!")

    def prepare_stop(self) -> None:
        self.log.info("Stopping...")
        # TODO what we need to

        
    async def get_user(self, user_id: UserID, create: bool = True) -> User:
        return await User.get_by_mxid(user_id, create=create)

    async def get_portal(self, room_id: RoomID) -> Portal:
        return await Portal.get_by_mxid(room_id)

    async def get_puppet(self, user_id: UserID, create: bool = False) -> Puppet:
        return await Puppet.get_by_mxid(user_id, create=create)

    async def get_double_puppet(self, user_id: UserID) -> Puppet:
        return await Puppet.get_by_custom_mxid(user_id)

    def is_bridge_ghost(self, user_id: UserID) -> bool:
        return bool(Puppet.get_id_from_mxid(user_id))

    async def count_logged_in_users(self) -> int:
        return len([user for user in User.by_phone_id.values() if user.phone_id])


PhoneBridge().run()