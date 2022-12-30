from typing import Any

import pytest

from src.domain.validators import PasswordValidator


class TestPasswordValidator:


    @pytest.mark.parametrize(
        ('value', 'error_msg'),
        [(None, "Password must not be of None type"),
         (0, "Invalid password. [value=0] must be a string"),
         (True, "Invalid password. [value=True] must be a string"),
         (1.618033988749895, "Invalid password. [value=1.618033988749895] must be a string")])
    def test_password_validator_validate_none(self, value: Any, error_msg: str):
        # Act
        with pytest.raises(Exception) as error:
            PasswordValidator.validate(value=value)  # type: ignore

        # Assert
        assert str(error.value) == error_msg


    @pytest.mark.parametrize(
        ('value', 'error_msg'),
        [('', "Password must not be empty"),
         (' ', "Password must not be empty"),
         ('     ', "Password must not be empty")])
    def test_password_validator_validate_strip_ok_and_empty_error(self, value: Any, error_msg: str):
        # Act
        with pytest.raises(Exception) as error:
            PasswordValidator.validate(value=value)  # type: ignore

        # Assert
        assert str(error.value) == error_msg

    @pytest.mark.parametrize(
        ('value', 'error_msg'),
        [('Tr@nscode3', "Invalid password. [value=Tr@nscode3] Your password: • Must contain at least a capital letter • Must contain at least a small letter • Must contain at least a number • Must contain at least a special character • Must be at least 12 characters long"),
         ('Transcode03', "Invalid password. [value=Transcode03] Your password: • Must contain at least a capital letter • Must contain at least a small letter • Must contain at least a number • Must contain at least a special character • Must be at least 12 characters long"),
         ('Transcodeee', "Invalid password. [value=Transcodeee] Your password: • Must contain at least a capital letter • Must contain at least a small letter • Must contain at least a number • Must contain at least a special character • Must be at least 12 characters long"),
         ('transcodeee', "Invalid password. [value=transcodeee] Your password: • Must contain at least a capital letter • Must contain at least a small letter • Must contain at least a number • Must contain at least a special character • Must be at least 12 characters long"),
         ('transcode03', "Invalid password. [value=transcode03] Your password: • Must contain at least a capital letter • Must contain at least a small letter • Must contain at least a number • Must contain at least a special character • Must be at least 12 characters long"),
         ('TRANSCODEE', "Invalid password. [value=TRANSCODEE] Your password: • Must contain at least a capital letter • Must contain at least a small letter • Must contain at least a number • Must contain at least a special character • Must be at least 12 characters long"),
         ('TR@NSCODEE', "Invalid password. [value=TR@NSCODEE] Your password: • Must contain at least a capital letter • Must contain at least a small letter • Must contain at least a number • Must contain at least a special character • Must be at least 12 characters long"),
         ('tr@nscodee', "Invalid password. [value=tr@nscodee] Your password: • Must contain at least a capital letter • Must contain at least a small letter • Must contain at least a number • Must contain at least a special character • Must be at least 12 characters long"),
         ('123456789012', "Invalid password. [value=123456789012] Your password: • Must contain at least a capital letter • Must contain at least a small letter • Must contain at least a number • Must contain at least a special character • Must be at least 12 characters long"),
         ('!@#$%&*()+_@', "Invalid password. [value=!@#$%&*()+_@] Your password: • Must contain at least a capital letter • Must contain at least a small letter • Must contain at least a number • Must contain at least a special character • Must be at least 12 characters long"),
         ('!@#$%&*()+_1', "Invalid password. [value=!@#$%&*()+_1] Your password: • Must contain at least a capital letter • Must contain at least a small letter • Must contain at least a number • Must contain at least a special character • Must be at least 12 characters long"),
         ('transcode0!', "Invalid password. [value=transcode0!] Your password: • Must contain at least a capital letter • Must contain at least a small letter • Must contain at least a number • Must contain at least a special character • Must be at least 12 characters long"),
         ])
    def test_password_validator_regex_invalid_error(self, value: Any, error_msg: str):
        # Act
        with pytest.raises(Exception) as error:
            PasswordValidator.validate(value=value)  # type: ignore

        # Assert
        assert str(error.value) == error_msg

    def test_password_validator_regex_ok(self):
        # Arrange
        value = "Tr@nscode003!"

        # Act
        PasswordValidator.validate(value=value)

        # Assert
        assert True