import re
from typing import Any

from src.domain.exceptions import DomainValidationError


class EmailValidator:
    @staticmethod
    def validate(value: Any):
        DomainValidationError.when(value is None, f"E-mail must not be of None type. [value={value}]")
        DomainValidationError.when(not isinstance(value, str), f"Invalid E-mail. [value={value}] must be a string")

        value = value.strip()
        email_regex = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
        email_validator = email_regex.findall(value)

        DomainValidationError.when(value not in email_validator, f"Invalid format. E-mail must be in format [User@Domain.com.br[br=Optional]. [value={value}]")
