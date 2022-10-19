from dataclasses import dataclass
from typing import List

from src.domain.entities import Chat, Solicitations, Bonds


@dataclass
class User:
    id: str = ""
    password: str = ""
    date_of_birth: str = ""
    secret: str = ""
    interests: List = [str]
    encryption_user = ""
    brothers = Bonds
    chats = Chat
    solicitations = Solicitations
