from interface.data_access_object_interface import DataAccessObjectInterface
from data_model_classes.account import Account

class AccountDAO(DataAccessObjectInterface):
    """
        This class is meant for retrieving, updating, creating, or deleting accounts from the accounts table.
    """
    def __init__(self):
        self.accounts: list[Account] = []

    def get_all_accounts(self) -> bool:
        """
            This method will cache all accounts from the accounts table to a list.
            
            This method should only be accessible by an admin, and run only once per session.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        pass

    def get_account_by_username(self, username: str) -> Account:
        """
            This method will return account associated with provided username. 

            This method should be accessible when logging in. 

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        pass

    def create_account(self, account: Account) -> bool:
        """
            This method will insert specified account into accounts table for saving.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        pass

    def update_account(self, account: Account) -> bool:
        """
            This method will update the specified account in the accounts table.

            This method can be used to update an account's role.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        pass

    def delete_account_by_username(self, username: str) -> bool:
        """
            This method will delete an account with the specified username.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        pass

             