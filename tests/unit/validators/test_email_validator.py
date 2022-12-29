from typing import Any
import pytest

from src.domain.validators.email_validator import EmailValidator


class TestEmailValidator:
    
    def test_email_validator_none_error(self):
        # Arrange
        test = None

        # Act
        with pytest.raises(Exception) as error:
            EmailValidator.validate(test)   # type: ignore

        # Assert
        assert str(error.value) == f"E-mail must not be of None type. [value={test}]"
        
        
    @pytest.mark.parametrize(
    ("value", "error_msg"),
    [(0, "Invalid E-mail. [value=0] must be a string"),
    (1.618033988749895, "Invalid E-mail. [value=1.618033988749895] must be a string"),
    (True, "Invalid E-mail. [value=True] must be a string")])
    
    def test_email_validator_wrong_type_error(self, value: Any, error_msg: str):
        # Act
        with pytest.raises(Exception) as error:
            EmailValidator.validate(value)

        # Assert
        assert str(error.value) == error_msg
        
    @pytest.mark.parametrize(
    ("value", "error_msg"),
    [("test", "Invalid format. E-mail must be in format [User@Domain.com.br[br=Optional], [value=test]"),
    ("test@", "Invalid format. E-mail must be in format [User@Domain.com.br[br=Optional], [value=test@]"),
    ("test@test", "Invalid format. E-mail must be in format [User@Domain.com.br[br=Optional], [value=test@test]"),
    ("@test", "Invalid format. E-mail must be in format [User@Domain.com.br[br=Optional], [value=@test]"),
    ("@test.com", "Invalid format. E-mail must be in format [User@Domain.com.br[br=Optional], [value=@test.com]"),
    ("@test.br", "Invalid format. E-mail must be in format [User@Domain.com.br[br=Optional], [value=@test.br]"),
    ("@test.com.br", "Invalid format. E-mail must be in format [User@Domain.com.br[br=Optional], [value=@test.com.br]"),
    ("test.com", "Invalid format. E-mail must be in format [User@Domain.com.br[br=Optional], [value=test.com]"),
    ("test.br", "Invalid format. E-mail must be in format [User@Domain.com.br[br=Optional], [value=test.br]"),
    ("test.com.br", "Invalid format. E-mail must be in format [User@Domain.com.br[br=Optional], [value=test.com.br]")])
    
    def test_email_validator_wrong_format_error(self, value: Any, error_msg: str):
        # Act
        with pytest.raises(Exception) as error:
            EmailValidator.validate(value)

        # Assert
        assert str(error.value) == error_msg
        
    @pytest.mark.parametrize(
        ("value"),
        [("  test@test.com"),
         ("test@test.com.br  "),
         ("  test@test.br  ")])
    
    def test_email_validator_trailing_leading_and_both_whitespaces_strip_valid_format_ok(self, value: Any):
        # Act
        EmailValidator.validate(value)

        # Assert
        assert True