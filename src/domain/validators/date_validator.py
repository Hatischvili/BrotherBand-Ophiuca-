from datetime import date
from typing import Any

from src.domain.exceptions import DomainValidationError


class DateValidator:
    @staticmethod
    def validate(value: Any) -> None:
        DomainValidationError.when(value is None, "Date must not be of None type")
        DomainValidationError.when(isinstance(value, date) is False, f"Date must must be of date type. [value={value}]")
