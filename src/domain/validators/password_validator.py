import re
from dataclasses import dataclass

from src.domain.exceptions import DomainValidationError


@dataclass
class PasswordValidator:
    @staticmethod
    def validate(value: str) -> None:
        DomainValidationError.when(value is None, "Password must not be of None type")
        DomainValidationError.when(not isinstance(value, str), f"Invalid password. [value={value}] must be a string")

        value = value.strip()

        DomainValidationError.when(value == '', "Password must not be empty")

        regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*]).{12,}$")
        validator = regex.findall(value)

        DomainValidationError.when(value not in validator,f"Invalid password. [value={value}] Your password: • Must contain at least a capital letter • Must contain at least a small letter • Must contain at least a number • Must contain at least a special character • Must be at least 12 characters long")
