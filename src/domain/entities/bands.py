from dataclasses import dataclass
from typing import List
from src.domain.enums.brotherband_solicitation_enum import BrotherbandSolicitationEnum

@dataclass
class Bonds:
    sent_solicitations: List = [str]
    received_solicitations: List = [str]
    status: BrotherbandSolicitationEnum = BrotherbandSolicitationEnum.EMPTY
    encryption = ""


@dataclass
class Bands:
    bonds = Bonds
    bands: List = [str]
    encryption: str = ""

