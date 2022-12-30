from dataclasses import dataclass
from typing import Any

from src.domain.exceptions import DomainValidationError


@dataclass
class EnumValidator:
    @staticmethod
    def validate(value: Any, field_name: str, enum_class: Any) -> None:
        DomainValidationError.when(value is None, f"Field {field_name} must not be of None type")
        DomainValidationError.when(value == '', f"Field {field_name} must not be empty")

        DomainValidationError.when(value not in list(enum_class), f"{field_name} must be in {enum_class}. [value={value}]")
