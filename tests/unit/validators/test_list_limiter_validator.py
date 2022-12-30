import pytest

from src.domain.validators import ListLimiterValidator


class TestListLimiterValidator:

    def test_list_limiter_validator_validate_over_limit_error(self):
        # Arrange
        list = [1, 2, 3, 4, 5, 6, 7]
        field_name = "Brothers"

        # Act
        with pytest.raises(Exception) as error:
            ListLimiterValidator.validate(list, field_name)

        # Assert
        assert str(error.value) == f"{field_name} must have only up to 6 items"


    def test_list_limiter_validator_validate_ok(self):
        # Arrange
        list = [1, 2, 3, 4, 5, 6]
        field_name = "Brothers"

        # Act
        ListLimiterValidator.validate(list, field_name)

        # Assert
        assert True