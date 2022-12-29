import re
from dataclasses import dataclass

from src.domain.exceptions import DomainValidationError


@dataclass
class PasswordValidator:
    @staticmethod
    def validate(password: str) -> None:
        DomainValidationError.when(password is None, "Empty password. [password=]")
        DomainValidationError.when(not isinstance(password, str), f"Invalid password.[password={password}] must be a string")
        password = password.strip()
        regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*]).{10,}$")
        validator = regex.findall(password)
        DomainValidationError.when(password not in validator,f"""
                                   Invalid password. [password={password}].
                                             Your password:
                                   • Should contain at least a capital letter
                                   • Should contain at least a small letter
                                   • Should contain at least a number
                                   • Should contain at least a special character
                                   • Should have at least 10 characters of length""",
        )
