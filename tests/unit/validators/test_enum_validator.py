from typing import Any

import pytest

from src.domain.enums import MessageStatusEnum
from src.domain.validators.enum_validator import EnumValidator


class TestEnumValidator:

    field_name = "Generic Enum"

    @pytest.mark.parametrize(
        ('value', 'error_msg'),
        [(None, f'Field {field_name} must not be of None type'),
         ('', f'Field {field_name} must not be empty')])
    def test_validate_enum_validator_empty_error(self, value: Any, error_msg: str):
        # Act
        with pytest.raises(Exception) as error:
            EnumValidator.validate(value=value, field_name=self.field_name, enum_class=MessageStatusEnum)

        # Assert
        assert str(error.value) == error_msg


    @pytest.mark.parametrize(
        ('value'),
        [(MessageStatusEnum.EMPTY),
         (MessageStatusEnum.READ),
         (MessageStatusEnum.RECIEVED),
         (MessageStatusEnum.SENT)])
    def test_validate_enum_validator_wrong_type_error(self, value: Any):
        # Act
        EnumValidator.validate(value=value, field_name=self.field_name, enum_class=MessageStatusEnum)

        # Assert
        assert True
