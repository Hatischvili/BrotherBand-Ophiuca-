from dataclasses import dataclass
from typing import List

from domain.validators import (ListLimiterValidator, MandatoryStringValidator,
                               PasswordValidator, UUIDValidator)


@dataclass
class User:
    id: str = ""
    user_name: str = ""
    password: str = ""
    date_of_birth: str = ""
    secret: str = ""
    interests: List = [str]
    registered_in: str = ""
    encryption: str = ""

    def validade(self):
        UUIDValidator.validate(self.id, "id")
        PasswordValidator.validate(self.password)
        ListLimiterValidator.validate(self.interests)
        MandatoryStringValidator.validate(self.user_name, "Username")
        MandatoryStringValidator.validate(self.secret, "Secret")
        MandatoryStringValidator.validate(self.date_of_birth, "Date of Birth")
        MandatoryStringValidator.validate(self.registered_in, "Registered in")
        

    def add_interst(self, interest):
        if interest <= 5:
            interest.append(interest)

    # def add_brothers(brother)
    #     brother.add()
