from dataclasses import dataclass
from uuid import UUID, uuid4
from domain.enums import BrotherbandRequestEnum

@dataclass
class Request:
    request_id: UUID = uuid4()
    sender_id: UUID = uuid4()
    recipient_id: UUID = uuid4()
    status: BrotherbandRequestEnum = BrotherbandRequestEnum.EMPTY