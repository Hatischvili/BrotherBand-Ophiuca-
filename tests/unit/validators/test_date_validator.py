from datetime import datetime
from typing import Any

import pytest

from src.domain.validators import DateValidator


class TestDateValidator:
    def test_validate_date_validator_none_error(self):
        # Arrange
        test = None

        # Act
        with pytest.raises(Exception) as error:
            DateValidator.validate(test)   # type: ignore

        # Assert
        assert str(error.value) == "Date must not be of None type"


    @pytest.mark.parametrize(
        ("value", "error_msg"),
        [(0, f"Date must must be of date type. [value={0}]"),
         (1.618033988749895, f"Date must must be of date type. [value={1.618033988749895}]"),
         (True, "Date must must be of date type. [value=True]")]
    )
    def test_validate_date_validator_wrong_type_error(self, value: Any, error_msg: str):
        # Act
        with pytest.raises(Exception) as error:
            DateValidator.validate(value)

        # Assert
        assert str(error.value) == error_msg


    def test_validate_date_converted_from_string_ok(self):
        # Arrange
        string = "2022-12-22"
        date = datetime.strptime(string, "%Y-%m-%d")

        # Act
        DateValidator.validate(date)  

        # Assert
        assert True

    def test_validate_date_ok(self):
        # Arrange
        date = datetime.today()

        # Act
        DateValidator.validate(date)  

        # Assert
        assert True