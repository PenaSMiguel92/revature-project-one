from abc import abstractmethod
from interface.menu_baseclass import MenuBaseClass

class MenuInterface(MenuBaseClass):

    @abstractmethod
    def set_state(self, state_value: int) -> None:
        """
            Encapsulation method for setting the current state of the menu object.

            :params: The enum menu_state holds the various valid program states.  
        """
        pass

    @abstractmethod
    def get_state(self) -> int:
        """
            Encapsulation method for getting the current state of the menu object.

            :params:
            :return: This will be an int associated with the enum menu_state
        """
        pass

    @abstractmethod
    def account_submenu(self) -> None:
        """
            Relay responsibility of handling user creation and login to another class.
        """
        pass

    @abstractmethod
    def admin_submenu(self) -> None:
        """
            Relay responsibility of handling admin menu to another class.
        """
        pass

    @abstractmethod
    def order_submenu(self) -> None:
        """
            Relay responsibility of handling orders to another class.
        """
        pass

    @abstractmethod
    def prescription_submenu(self) -> None:
        """
            Relay responsibility of handling prescriptions to another class.
        """
        pass