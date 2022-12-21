from dataclasses import dataclass
from typing import List
from uuid import UUID, uuid4
from src.domain.enums.brotherband_solicitation_enum import BrotherbandSolicitationEnum


@dataclass
class Solicitation:
    solicitation_id: UUID = uuid4()
    sender_id: UUID = uuid4()
    recipient_id: UUID = uuid4()
    status: BrotherbandSolicitationEnum = BrotherbandSolicitationEnum.EMPTY