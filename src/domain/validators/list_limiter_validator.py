from dataclasses import dataclass
from typing import List

from src.domain.exceptions import DomainValidationError


@dataclass
class ListLimiterValidator:
    @staticmethod
    def validate(list: List, field_name: str) -> None:
        DomainValidationError.when(len(list) > 6, f"{field_name} must have only up to 6 items")
