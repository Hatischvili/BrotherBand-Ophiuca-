from dataclasses import dataclass
from typing import List
from uuid import UUID, uuid4
from .message import Message


@dataclass
class Chat:
    chat_id: UUID = uuid4()
    participant_1: UUID = uuid4()
    participant_2: UUID = uuid4()
    messages: List[Message] = []


