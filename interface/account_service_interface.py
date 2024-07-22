from abc import abstractmethod
from interface.menu_baseclass import MenuBaseClass

class AccountServiceInterface(MenuBaseClass):
    @abstractmethod
    def account_register(self) -> None:
        """
            Method for registering a new user. It will ask the user for a username and password. 
        """
        pass
    
    @abstractmethod
    def account_login(self) -> None:
        """
            Method for login with existing username. It will ask for the username and password, and validate the password. 
        """
        pass
