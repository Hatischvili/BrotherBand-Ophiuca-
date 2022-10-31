from dataclasses import dataclass
from typing import List

from src.domain.enums import MessageStatusEnum


@dataclass
class Message:
    sender: str = ""
    recipient: str = ""
    body: str = ""
    timestamp: str = ""
    read: MessageStatusEnum = MessageStatusEnum.EMPTY
    encryption = ""


@dataclass
class Conversation:
    messages: List[Message]
    encryption = ""


@dataclass
class Chats:
    lista: List[Conversation]
    encryption = ""
