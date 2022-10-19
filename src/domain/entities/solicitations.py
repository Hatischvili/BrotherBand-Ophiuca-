from dataclasses import dataclass
from typing import List


@dataclass
class Solicitations:
    sent: List = [str]
    received: List = [str]
    encryption_solicitations = ""
