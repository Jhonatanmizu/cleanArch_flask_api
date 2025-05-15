from datetime import datetime


class Users:
    def __init__(self, _id: int, first_name: str, last_name: str, birthdate: datetime) -> None:
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate

    def __str__(self) -> str:
        fullname = f'{self.first_name} {self.last_name}'
        return f"User(id={self.id!r}, fullname={fullname!r})"
