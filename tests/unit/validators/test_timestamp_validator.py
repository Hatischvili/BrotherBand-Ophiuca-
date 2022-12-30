from datetime import datetime
from typing import Any

import pytest

from src.domain.validators import TimestampValidator


class TestTimestampValidator:
    def test_validate_date_validator_none_error(self):
        # Arrange
        test = None

        # Act
        with pytest.raises(Exception) as error:
            TimestampValidator.validate(test)   # type: ignore

        # Assert
        assert str(error.value) == "Timestamp must not be of None type"


    @pytest.mark.parametrize(
        ("value", "error_msg"),
        [(0, f"Timestamp must must be of datetime type. [value={0}]"),
         (1.618033988749895, f"Timestamp must must be of datetime type. [value={1.618033988749895}]"),
         (True, "Timestamp must must be of datetime type. [value=True]")]
    )
    def test_validate_timestamp_validator_wrong_type_error(self, value: Any, error_msg: str):
        # Act
        with pytest.raises(Exception) as error:
            TimestampValidator.validate(value)

        # Assert
        assert str(error.value) == error_msg

    def test_validate_timestamp_converted_from_string_ok(self):
        # Arrange
        string = "2022-12-30 16:28:46.711900"
        date = datetime.strptime(string, "%Y-%m-%d %H:%M:%S.%f")

        # Act
        TimestampValidator.validate(date)  

        # Assert
        assert True

    def test_validate_date_ok(self):
        # Arrange
        date = datetime.now()

        # Act
        TimestampValidator.validate(date)  

        # Assert
        assert True