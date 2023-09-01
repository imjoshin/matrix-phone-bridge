from mautrix.types import SerializableAttrs
from typing import Optional
from attr import dataclass


@dataclass
class Puppet(SerializableAttrs):
    id: int
    id_str: str
    name: str
    profile_image_url: Optional[str]
    profile_image_url_https: Optional[str]
    description: str