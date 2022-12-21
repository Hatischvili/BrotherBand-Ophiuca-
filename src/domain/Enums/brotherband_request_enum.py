from enum import IntEnum


class BrotherbandRequestEnum(IntEnum):
    EMPTY = 0
    SENT = 1
    RECIEVED = 2
    ACCEPTED = 3
    DECLINED = 4
    DELETED = 5
