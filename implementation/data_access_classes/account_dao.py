from interface.data_access_object_interface import DataAccessObjectInterface
from implementation.data_model_classes.account import Account
import logging
import mysql.connector
from mysql.connector.cursor import MySQLCursor



class AccountDAO(DataAccessObjectInterface):
    """
        This class is meant for retrieving, updating, creating, or deleting accounts from the accounts table.
    """
    def __init__(self):
        logging.basicConfig(filename="logs/rxbuddy_database.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')

    def get_all_accounts(self) -> list[Account]:
        """
            This method will cache all accounts from the accounts table to a list.
            
            This method should only be accessible by an admin, and run only once per session.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        cursor: MySQLCursor = super().get_cursor() 
        query = 'SELECT a.accountID, a.accountUsername, a.accountPassword, a.firstName, a.lastName, a.balance, r.roleName FROM accounts AS a JOIN roles as r ON a.accountRole = r.roleID;'
        cursor.execute(query)
        accounts: list[Account] = []
        for _, row in enumerate(cursor):
            accounts.append(Account(int(row[0]), row[1], row[2], row[3], row[4], float(row[5]), row[6]))

        logging.info('All accounts retrieved from database successfully.')
        return accounts

    def get_account_by_username(self, username: str) -> Account:
        """
            This method will return account associated with provided username. 

            This method should be accessible when logging in. 

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        cursor: MySQLCursor = super().get_cursor()
        query = f'SELECT a.accountID, a.accountUsername, a.accountPassword, a.firstName, a.lastName, a.balance, r.roleName FROM accounts AS a JOIN roles AS r ON a.accountRole = r.roleID WHERE accountUsername = \'{username}\';'
        cursor.execute(query)
        tmp_account = None
        for _, row in enumerate(cursor):
            tmp_account = Account(int(row[0]), row[1], row[2], row[3], row[4], float(row[5]), row[6])
            break

        logging.info('Account retrieved from database.')
        return tmp_account

    def create_account(self, account: Account) -> bool:
        """
            This method will insert specified account into accounts table for saving.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        cursor: MySQLCursor = super().get_cursor()
        query_start = f'INSERT INTO accounts (accountID, accountUsername, accountPassword, firstName, lastName, balance, roleID) VALUES '
        query_end = f'(DEFAULT, \'{account.accountUsername}\', \'{account.accountPassword}\', \'{account.firstName}\', \'{account.lastName}\', 0.00, 2)'
        cursor.execute(query_start + query_end)
        logging.info('Account created and saved to database.')
        return True

    def update_account(self, account: Account) -> bool:
        """
            This method will update the specified account in the accounts table.

            This method can be used to update an account's role.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        roles = ['Admin', 'Patient', 'Doctor']
        new_roleID = roles.index(account.roleName)
        cursor: MySQLCursor = super().get_cursor()
        query_start = f'UPDATE accounts SET balance={account.balance}, roleID={new_roleID}'
        query_end = f' WHERE accountID={account.accountID};'
        cursor.execute(query_start + query_end)
        logging.info('Account attributes updated.')
        return True

    def delete_account_by_username(self, username: str) -> bool:
        """
            This method will delete an account with the specified username.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        try:
            cursor: MySQLCursor = super().get_cursor()
            query = f'DELETE FROM accounts WHERE accountUsername=\'{username}\''
            cursor.execute(query)

        except mysql.connector.Error as Err:
            logging.error(Err.msg)
            return False
        
        logging.info(f'Deleted {username} from accounts table in database.')
        return True        
