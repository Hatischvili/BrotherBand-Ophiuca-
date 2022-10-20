from dataclasses import dataclass
from typing import List
from domain.validators import PasswordValidator
from domain.validators import UUIDValidator

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
    
    def validade(self):
        UUIDValidator.validate(self.id, "id")
        PasswordValidator.validate(self.password)
        