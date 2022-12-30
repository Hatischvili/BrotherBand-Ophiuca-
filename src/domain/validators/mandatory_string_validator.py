from dataclasses import dataclass

from src.domain.exceptions import DomainValidationError


@dataclass
class MandatoryStringValidator:
    @staticmethod
    def validate(value: str, field_name: str, exact_length: int = 0, min_length: int = 0, max_length: int = 0) -> None:
        DomainValidationError.when(value is None, f"{field_name} must not be of None type")
        DomainValidationError.when(isinstance(value, str) is False, f"{field_name} must be a string")

        value = value.strip()

        DomainValidationError.when(value == '', f"{field_name} must not be empty")

        if exact_length > 0:
            DomainValidationError.when(len(value) != exact_length, f"{field_name}'s size must be exactly: {exact_length} characters long")
        else:
            DomainValidationError.when(min_length > 0 and len(value) < min_length, f"{field_name}'s minimum size is: {min_length} characters long")
            DomainValidationError.when(max_length > 0 and len(value) > max_length, f"{field_name}'s maximum size is: {max_length} characters long")
