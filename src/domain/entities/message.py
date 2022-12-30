from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4

from src.domain.enums import MessageStatusEnum


@dataclass
class Message:
    message_id: UUID = uuid4()
    sender_id: UUID = uuid4()
    recipient_id: UUID = uuid4()
    body: str = ''
    timestamp: datetime = datetime.now()
    status: MessageStatusEnum = MessageStatusEnum.EMPTY
