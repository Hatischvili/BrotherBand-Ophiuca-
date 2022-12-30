from datetime import datetime
from typing import Any

from src.domain.exceptions import DomainValidationError


class TimestampValidator:
    @staticmethod
    def validate(value: Any) -> None:
        DomainValidationError.when(value is None, "Timestamp must not be of None type")
        DomainValidationError.when(isinstance(value, datetime) is False, f"Timestamp must must be of datetime type. [value={value}]")
