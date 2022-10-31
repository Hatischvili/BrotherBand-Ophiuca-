from typing import Any
import pytest
from src.domain.validators.mandatory_string_validator import MandatoryStringValidator
from src.config.config_atributes import NAME_MAX_LEN, NAME_MIN_LEN

class TestMandatoryStringValidator():

    field_name = 'String Validator'
    @pytest.mark.parametrize(
        ('name', 'msg_erro'), (
            (None, f"{field_name} isn't a string"),
            ("      ", f"{field_name} must not be empty"),
            ("", f"{field_name} must not be empty"),
        )
    )
    def test_validate_mandatorystringvalidator_error(self, name:Any, msg_erro: str):

        # Act
        with pytest.raises(Exception) as erro:
            MandatoryStringValidator.validate(name,self.field_name)

        # Assert
        assert str(erro.value) == msg_erro

    @pytest.mark.parametrize(
        ('value', 'msg_erro'), (
            ("1"*(NAME_MAX_LEN+1), f"{field_name} maximum size is - {NAME_MAX_LEN}"),
            ("1"*(NAME_MIN_LEN-1), f"{field_name} minimum size is - {NAME_MIN_LEN}")
            )
        )

    def test_validade_mandatory_string_validator_name_maximum_size_error(self, value:Any, msg_erro: str):

        field_name = 'String Validator'
        max_length = NAME_MAX_LEN
        min_length =NAME_MIN_LEN
        strigmax = MandatoryStringValidator()

        # Act
        with pytest.raises(Exception) as erro:
            strigmax.validate(value=value,field_name=field_name,max_length=max_length,min_length=min_length)

        # Assert
        assert str(erro.value) == msg_erro
        
    
    def test_validate_mandatory_stringv_alidator_ok(self):
        value = "Clarice"
        field_name = "Usernamme"

        # Act
        MandatoryStringValidator.validate(value=value,field_name=field_name,max_length=NAME_MAX_LEN,min_length=NAME_MIN_LEN)

        # Assert
        assert True

    
