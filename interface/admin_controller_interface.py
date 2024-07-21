from abc import abstractmethod
from interface.menu_baseclass import MenuBaseClass

class AdminControllerInterface(MenuBaseClass):
    @abstractmethod
    def set_state(self, state_value: int) -> None:
        """
            This method must be used to set the state of this menu.
        """
        pass

    @abstractmethod
    def get_state(self) -> int:
        """
            This method is used to get the state of this menu.
        """
        pass
    
    @abstractmethod
    def display_users(self) -> None:
        """
            This method will display all users and their roles.
            For example:
            penamiguel -> Patient
            drhousemd -> Doctor
            ownermiguel -> Admin
        """
        pass
    
    @abstractmethod
    def display_orders(self) -> None:
        """
            This method will display all orders.  
        """
        pass

    @abstractmethod
    def apply_role(self) -> None:
        """
            This method will apply a role to a specified user.

            For example, an admin will be able to apply the Doctor role to a user, which grants them the ability to create prescriptions.
        """
        pass

