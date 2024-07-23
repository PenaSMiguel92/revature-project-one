from interface.input_validation_interface import InputValidation
from interface.account_service_interface import AccountServiceInterface
from enum import Enum

account_service_state = Enum('USER_STATE', [
    'INITIAL_STATE',
    'CREATING_USER_STATE',
    'LOADING_USER_STATE',
    'CLOSING_STATE'
])

class AccountService(InputValidation, AccountServiceInterface):

    def __init__(self) -> None:
        self.current_state = account_service_state.INITIAL_STATE

    def account_login(self) -> None:
        return super().account_login()
    
    def account_register(self) -> None:
        return super().account_register()
    
    def display(self) -> None:
        print('Would you like to register a new user or login?')
        print('(R)egister')   
        print('(L)ogin') 
        
    
    def run(self) -> bool:
        match self.current_state:
            case account_service_state.INITIAL_STATE:
                self.display()
                return True
            case account_service_state.CLOSING_STATE:
                return False