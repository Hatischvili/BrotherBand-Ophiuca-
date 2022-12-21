from dataclasses import dataclass
from uuid import UUID, uuid4

@dataclass
class Bonds:
    request_id: UUID = uuid4()
