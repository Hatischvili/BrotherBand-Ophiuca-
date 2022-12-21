from dataclasses import dataclass
from datetime import datetime
from typing import List
from uuid import UUID, uuid4

@dataclass
class User:
    id: UUID = uuid4()
    user_name: str = ""
    user_email: str = ""
    password: str = ""
    secret: str = ""
    interests: List[str] = []
    date_of_birth: datetime = datetime.now()
    registered_in: datetime = datetime.now()