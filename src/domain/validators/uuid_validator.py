from dataclasses import dataclass
from uuid import UUID

from src.domain.exceptions import DomainValidationError


@dataclass
class UUIDValidator:
    @staticmethod
    def validate(value: str, field: str) -> None:
        DomainValidationError.when(value is None, f"Field {field} cannot be None.")
        try:
            _ = UUID(value)
        except ValueError as exc:
            raise DomainValidationError(f"Field {field} must be an UUID. [value={value}]") from exc
