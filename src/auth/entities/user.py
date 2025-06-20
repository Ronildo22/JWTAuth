from dataclasses import dataclass, field


@dataclass
class User:
    login: str
    password: str
