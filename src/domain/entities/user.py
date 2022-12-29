from dataclasses import dataclass
from datetime import date, datetime
from typing import List
from uuid import UUID, uuid4


@dataclass
class User:
    id: UUID = uuid4()
    user_name: str = ""
    full_name: str = ""
    user_email: str = ""
    password: str = ""
    secret: str = ""
    interests: List[str] = []
    birthday: date = date.today()
    registered_in: datetime = datetime.now()

    @property
    def user_age(self):
        return (date.today() - self.birthday) / 365

    def validade(self):
        pass
