from dataclasses import dataclass
from typing import List

from src.domain.exceptions.domain_validation_error import DomainValidationError


@dataclass
class ListLimiterValidator:
    @staticmethod
    def validate(list: List):
        DomainValidationError.when(len(list) > 5, "List must have only up to 5 items.")
