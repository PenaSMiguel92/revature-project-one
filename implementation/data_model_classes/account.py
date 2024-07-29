from dataclasses import dataclass

@dataclass
class Account():
    """
        Class for keeping track of account data
    """
    account_id: int
    first_name: str
    last_name: str
    username: str
    password: str
    roleName: str
