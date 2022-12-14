from typing import Any
from uuid import uuid4

import pytest

from src.domain.validators import UUIDValidator


class TestUUIDValidador:
    field = 'UUID Field'
    default_error_message = f"Field {field} must be an UUID."

    @pytest.mark.parametrize(
        ('uuid', 'msg_error'),
        [(None, f"Field {field} must not be of None type."),
         ("      ", f"{default_error_message} [value=      ]"),
         ("", f"{default_error_message} [value=]"),
         ("123sdsd", f"{default_error_message} [value=123sdsd]"),
         ("32005609-d7fe-4621-8e05-01dedef8335", f"{default_error_message} [value=32005609-d7fe-4621-8e05-01dedef8335]")])
    def test_validate_uuid_validator_error(self, uuid: Any, msg_error: str):
        # Act
        with pytest.raises(Exception) as error:
            UUIDValidator.validate(uuid, self.field)

        # Assert
        assert str(error.value) == msg_error

    def test_validate_uuid_validator_ok(self):
        # Arrange
        uuid = str(uuid4())

        # Act
        UUIDValidator.validate(uuid, self.field)

        # Assert
        assert True
