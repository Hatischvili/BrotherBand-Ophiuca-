from dataclasses import dataclass
from typing import List

from src.domain.entities import Chat, Solicitations, Bonds


@dataclass
class User:
    user_id: str = ""
    password: str = ""
    date_of_birth: str = ""
    secret: str = ""
    interests: List = []
    encryption_user = ""
    brothers = Bonds
    chats = Chat
    solicitations = Solicitations
