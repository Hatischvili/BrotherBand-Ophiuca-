import re
from typing import Any

from src.domain.exceptions import DomainValidationError


class DateValidator:
    @staticmethod
    def validate(value: Any):
        DomainValidationError.when(value is None, f"Date must not be of None type. [value={value}]")
        DomainValidationError.when(not isinstance(value, str), f"Invalid date. [value={value}] must be a string")

        value = value.strip()
        date_regex = re.compile(r"([0-9]{4})-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])")
        date_validator = date_regex.findall(value)

        DomainValidationError.when(value not in date_validator, f"Invalid format. Timestamp must be in format YYYY-MM-DD [value={value}]")
