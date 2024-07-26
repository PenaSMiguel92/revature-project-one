from interface.input_validation_interface import InputValidation
from interface.account_service_interface import AccountServiceInterface
from custom_exceptions.account_menu_selection_invalid import AccountMenuSelectionInvalid
from implementation.data_access_classes.account_dao import AccountDAO
from implementation.data_model_classes.account import Account

from mysql.connector import Error

from enum import Enum

account_service_state = Enum('USER_STATE', [
    'INITIAL_STATE',
    'CREATING_USER_STATE',
    'LOADING_USER_STATE',
    'LOADED_USER_STATE',
    'CLOSING_STATE'
])

class AccountService(InputValidation, AccountServiceInterface):

    def __init__(self) -> None:
        self.current_state = account_service_state.INITIAL_STATE
        self.account_dao: AccountDAO = AccountDAO()
        self.current_account: Account = None

    def account_login(self) -> None:
        print('\nPlease enter your username: ')
        while self.current_account == None:
            try:
                username = input('>>>').lower()
                self.current_account = self.account_dao.get_account_by_username(username)
                self.current_state = account_service_state.LOADED_USER_STATE
                break
            except Error as mysql_error:
                print('Username does not exist. Please enter a valid username.')
        if self.current_account == None:
            print('Username does not exist. Please enter a valid username.')
            self.current_state = account_service_state.INITIAL_STATE
            return False
        
        print('\nPlease enter your password: ')
        retries = 3
        while retries > 0:
            user_password = input('>>>')
            if self.current_account.password != user_password:
                print(f"Passwords do not match, please try again ({retries - 1})")
                retries -= 1
            else:
                break

        if retries == 0:
            print('Too many attempts. Try again later.')
            self.current_account = None
            self.current_state = account_service_state.INITIAL_STATE
            return False
        
        return True
    
    def account_greeting(self) -> None:
        if self.current_account == None:
            return 
        
        print(f'\nWelcome back {self.current_account.first_name} {self.current_account.last_name}! What would you like to do? ')

    def account_register(self) -> None:
        print('Registering account.')
        self.current_state = account_service_state.LOADED_USER_STATE
        return True
    
    def display(self) -> bool:
        print('\nWould you like to register a new user or login?')
        print('(R)egister')   
        print('(L)ogin') 
        print('(E)xit')
        while self.current_state == account_service_state.INITIAL_STATE:
            try: 
                user_input = input('>>>').upper()
                if not self.validate_input(user_input, char_input = True, valid_input = 'RLE'):
                    raise AccountMenuSelectionInvalid("Please choose a valid menu option.")
                self.process_input(user_input)

            except AccountMenuSelectionInvalid as msg:
                print(msg.message)

        return True

    def process_input(self, input: str) -> None:
        match (input):
            case 'R':
                self.current_state = account_service_state.CREATING_USER_STATE
            case 'L':
                self.current_state = account_service_state.LOADING_USER_STATE
            case 'E':
                self.current_state = account_service_state.CLOSING_STATE
    
    def set_state(self, state: int) -> None:
        self.current_state = state
    
    def get_state(self) -> int:
        return self.current_state
    
    def run(self) -> bool:
        match self.current_state:
            case account_service_state.INITIAL_STATE:
                return self.display()
            case account_service_state.CREATING_USER_STATE:
                return self.account_register()
            case account_service_state.LOADING_USER_STATE:
                return self.account_login()
            case account_service_state.LOADED_USER_STATE:
                return True
            case account_service_state.CLOSING_STATE:
                return True