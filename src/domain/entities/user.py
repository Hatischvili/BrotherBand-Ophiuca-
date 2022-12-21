from dataclasses import dataclass
from datetime import datetime
from typing import List
from uuid import UUID, uuid4



@dataclass
class User:
    id: UUID = uuid4()
    user_name: str = ""
    password: str = ""
    date_of_birth: datetime = datetime.now()
    secret: str = ""
    interests: List[str] = []
    registered_in: datetime = datetime.now()