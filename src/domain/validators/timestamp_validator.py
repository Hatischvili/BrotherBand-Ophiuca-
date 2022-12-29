import re
from typing import Any
from src.domain.exceptions.domain_validation_error import DomainValidationError

class TimestampValidator:
    @staticmethod
    def validate(value: Any):
        DomainValidationError.when(value is None, f"Timestamp must not be of None type. [value={value}]")
        DomainValidationError.when(not isinstance(value, str), f"Invalid timestamp. [value={value}] must be a string",)

        value = value.strip()
        timestamp_regex = re.compile(r'([0-9]{4})-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([0-9]{2}):([0-9]{2}):([0-9]{2}).([0-9]{6})')
        timestamp_validator = timestamp_regex.findall(value)

        DomainValidationError.when(value not in timestamp_validator, f"Invalid format. Timestamp must be in format YYYY-MM-DD YY:MM:SS.μμμμμμ, [value={value}]")