from typing import Any

import pytest

from src.config.config_atributes import NAME_MAX_LEN, NAME_MIN_LEN
from src.domain.validators import MandatoryStringValidator


class TestMandatoryStringValidator:

    field_name = 'String Validator'

    @pytest.mark.parametrize(
        ('value', 'error_msg'),
        [(None, "String Validator must not be of None type"),
         ("      ", f"{field_name} must not be empty"),
         ("", f"{field_name} must not be empty")])
    def test_validate_mandatory_string_validator_error(self, value: Any, error_msg: str):

        # Act
        with pytest.raises(Exception) as error:
            MandatoryStringValidator.validate(value, self.field_name)

        # Assert
        assert str(error.value) == error_msg

    @pytest.mark.parametrize(
        ('value', 'error_msg'),
        [("1" * (NAME_MAX_LEN + 1), f"{field_name}'s maximum size is: {NAME_MAX_LEN} characters long"),
         ("1" * (NAME_MIN_LEN - 1), f"{field_name}'s minimum size is: {NAME_MIN_LEN} characters long")])
    def test_validate_mandatory_string_validator_name_maximum_and_minum_size_error(self, value: Any, error_msg: str):
        # Arrange
        field_name = 'String Validator'
        max_length = NAME_MAX_LEN
        min_length = NAME_MIN_LEN

        # Act
        with pytest.raises(Exception) as erro:
            MandatoryStringValidator.validate(value=value, field_name=field_name, max_length=max_length, min_length=min_length)

        # Assert
        assert str(erro.value) == error_msg


    def test_validate_mandatory_string_validator_name_exact_size_error(self):
        # Arrange
        field_name = 'String Validator'
        value = "Hello World"

        # Act
        with pytest.raises(Exception) as error:
            MandatoryStringValidator.validate(value=value, field_name=field_name, exact_length=5)

        # Assert
        assert str(error.value) == f"{field_name}'s size must be exactly: 5 characters long"


    def test_validate_mandatory_string_validator_ok(self):
        # Arrange
        value = "Hoshikawa"
        field_name = "Username"

        # Act
        MandatoryStringValidator.validate(value=value, field_name=field_name, max_length=NAME_MAX_LEN, min_length=NAME_MIN_LEN)

        # Assert
        assert True
