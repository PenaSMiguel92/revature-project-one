from interface.input_validation_interface import InputValidation
from interface.user_controller_interface import UserControllerInterface
from enum import Enum

user_state = Enum('USER_STATE', [
    'INITIAL_STATE',
    'CREATING_USER_STATE',
    'LOADING_USER_STATE',
    'CLOSING_STATE'
])

class UserController(InputValidation, UserControllerInterface):

    def __init__(self) -> None:
        self.current_state = user_state.INITIAL_STATE

    def user_login(self) -> None:
        return super().user_login()
    
    def user_register(self) -> None:
        return super().user_register()
    
    def display(self) -> None:
        print('Would you like to register a new user or login?')
        print('(R)egister')   
        print('(L)ogin') 
        
    
    def run(self) -> bool:
        match self.current_state:
            case user_state.INITIAL_STATE:
                self.display()
                return True
            case user_state.CLOSING_STATE:
                return False