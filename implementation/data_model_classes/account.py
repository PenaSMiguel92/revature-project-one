from dataclasses import dataclass

@dataclass
class Account():
    """
        This data class will be used to model accounts gathered by joining the accounts and roles table. 

        Normalization is upto 2F, since there are transient dependencies on this table.

        Information can be displayed to doctors and admins. 
    """
    accountID: int
    accountUsername: str
    accountPassword: str
    firstName: str
    lastName: str
    balance: float
    roleName: str
