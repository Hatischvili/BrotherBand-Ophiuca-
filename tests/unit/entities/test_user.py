from uuid import uuid4
from src.domain.entities import User
from src.domain.validators import PasswordValidator, UUIDValidator


class TestUser:
    def test_mock_validate_all_fields_ok(self, mocker):
        # Arrange
        user = User(id=str(uuid4()), azure_id=str(uuid4()), status=StatusEnum.ACTIVE)
        mocker.patch.object(EmailValidator, 'validate')
        mocker.patch.object(UUIDValidator, 'validate')
        mocker.patch.object(EnumValidator, 'validate')
        calls = [
                mocker.call(user.user_id, "user_id"),
                mocker.call(user.azure_id, "azure_id"),
                ]

        # Act
        user.validate()

        # Assert
        EmailValidator.validate.assert_called_once_with(user.user_email)
        UUIDValidator.validate.assert_has_calls(calls)
        EnumValidator.validate.assert_called_once_with(user.status, "status", StatusEnum)